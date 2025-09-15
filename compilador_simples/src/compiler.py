from lexer_parser import parse_code, print_tree
from code_generator import LLVMCodeGenerator
import llvmlite.binding as llvm

class SimpleCompiler:
    def __init__(self):
        self.generator = None
        
    def compile(self, source_code, verbose=False):
        """Compila o código fonte"""
        try:
            # 1. Análise sintática
            if verbose:
                print("=== ANÁLISE SINTÁTICA ===")
            
            tree, errors = parse_code(source_code)
            
            if errors:
                print("Erros encontrados durante a análise:")
                for error in errors:
                    print(f"  {error}")
                return False
            
            if verbose:
                print("✓ Análise sintática concluída com sucesso")
                # print_tree(tree, None)  # Remover se SimpleLangParser não estiver disponível
            
            # 2. Geração de código
            if verbose:
                print("\n=== GERAÇÃO DE CÓDIGO ===")
            
            self.generator = LLVMCodeGenerator()
            llvm_module = self.generator.visitProgram(tree)
            
            if verbose:
                print("✓ Código LLVM gerado com sucesso")
                print("\n=== CÓDIGO LLVM IR ===")
                print(self.generator.get_llvm_ir())
            
            return True
            
        except Exception as e:
            print(f"Erro durante a compilação: {e}")
            return False
    
    def get_llvm_ir(self):
        """Retorna o código LLVM IR"""
        if self.generator:
            return self.generator.get_llvm_ir()
        return None
    
    def save_llvm_ir(self, filename):
        """Salva o código LLVM IR em arquivo"""
        if self.generator:
            with open(filename, 'w') as f:
                f.write(self.generator.get_llvm_ir())
            print(f"Código LLVM salvo em: {filename}")
        else:
            print("Nenhum código foi gerado ainda")