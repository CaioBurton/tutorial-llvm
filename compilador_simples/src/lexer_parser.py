import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

# Importar classes geradas pelo ANTLR
# Você precisará gerar estas classes primeiro
try:
    from grammar.SimpleLangLexer import SimpleLangLexer
    from grammar.SimpleLangParser import SimpleLangParser
except ImportError:
    print("Erro: Classes do ANTLR não encontradas.")
    print("Execute: antlr4 -Dlanguage=Python3 grammar/SimpleLang.g4 -o src/")
    sys.exit(1)

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        error_msg = f"Erro de sintaxe na linha {line}:{column} - {msg}"
        self.errors.append(error_msg)
        print(error_msg)

def parse_code(code):
    """Parse do código fonte e retorna a árvore sintática"""
    # Criar stream de entrada
    input_stream = InputStream(code)
    
    # Criar lexer
    lexer = SimpleLangLexer(input_stream)
    
    # Criar stream de tokens
    token_stream = CommonTokenStream(lexer)
    
    # Criar parser
    parser = SimpleLangParser(token_stream)
    
    # Adicionar listener de erro
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    # Parse
    tree = parser.program()
    
    if error_listener.has_error:
        return None, error_listener.errors
    
    return tree, None

def print_tree(tree, parser):
    """Imprime a árvore sintática"""
    print("Árvore sintática:")
    print(Trees.toStringTree(tree, None, parser))