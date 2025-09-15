import llvmlite.ir as ir
import llvmlite.binding as llvm
from grammar.SimpleLangParser import SimpleLangParser
from grammar.SimpleLangVisitor import SimpleLangVisitor

class LLVMCodeGenerator(SimpleLangVisitor):
    def __init__(self):
        # Inicializar LLVM
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        
        # Criar módulo LLVM
        self.module = ir.Module(name="simple_lang_module")
        
        # Criar função main
        func_type = ir.FunctionType(ir.IntType(32), [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        
        # Criar bloco básico
        self.block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(self.block)
        
        # Tabela de símbolos (variáveis)
        self.variables = {}
        
    def visitProgram(self, ctx):
        """Visita o programa principal"""
        # Visitar todos os statements
        for statement in ctx.statement():
            self.visit(statement)
        
        # Retornar 0 da função main
        self.builder.ret(ir.Constant(ir.IntType(32), 0))
        
        return self.module
    
    def visitAssignment(self, ctx):
        """Visita atribuição de variável"""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        
        # Alocar espaço para a variável se não existir
        if var_name not in self.variables:
            # Criar alloca na entrada da função
            with self.builder.goto_entry_block():
                var_ptr = self.builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = var_ptr
        
        # Armazenar o valor
        self.builder.store(value, self.variables[var_name])
        
        return value
    
    def visitNumber(self, ctx):
        """Visita um número literal"""
        value = int(ctx.NUMBER().getText())
        return ir.Constant(ir.IntType(32), value)
    
    def visitVariable(self, ctx):
        """Visita uma variável"""
        var_name = ctx.ID().getText()
        
        if var_name not in self.variables:
            raise Exception(f"Variável '{var_name}' não foi declarada")
        
        # Carregar o valor da variável
        return self.builder.load(self.variables[var_name], name=var_name)
    
    def visitAddSub(self, ctx):
        """Visita operação de adição/subtração"""
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        
        op = ctx.getChild(1).getText()
        
        if op == '+':
            return self.builder.add(left, right, name="addtmp")
        elif op == '-':
            return self.builder.sub(left, right, name="subtmp")
    
    def visitMulDiv(self, ctx):
        """Visita operação de multiplicação/divisão"""
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        
        op = ctx.getChild(1).getText()
        
        if op == '*':
            return self.builder.mul(left, right, name="multmp")
        elif op == '/':
            return self.builder.sdiv(left, right, name="divtmp")
    
    def visitParentheses(self, ctx):
        """Visita expressão entre parênteses"""
        return self.visit(ctx.expression())
    
    def get_llvm_ir(self):
        """Retorna o código LLVM IR como string"""
        return str(self.module)