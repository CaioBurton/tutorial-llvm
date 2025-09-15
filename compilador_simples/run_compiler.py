#!/usr/bin/env python3

import sys
import os

# Adicionar a pasta src ao path do Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from compiler import SimpleCompiler

def main():
    if len(sys.argv) != 2:
        print("Uso: python run_compiler.py <simple.sl>")
        print("Exemplo: python run_compiler.py examples/simple.sl")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    if not os.path.exists(filename):
        print(f"Erro: Arquivo '{filename}' não encontrado")
        sys.exit(1)
    
    # Ler código fonte
    with open(filename, 'r') as f:
        source_code = f.read()
    
    print(f"Compilando: {filename}")
    print("=" * 50)
    print("Código fonte:")
    print(source_code)
    print("=" * 50)
    
    # Compilar
    compiler = SimpleCompiler()
    success = compiler.compile(source_code, verbose=True)
    
    if success:
        # Salvar código LLVM
        output_file = filename.replace('.sl', '.ll')
        compiler.save_llvm_ir(output_file)
        print(f"\n✓ Compilação concluída com sucesso!")
        print(f"  Código LLVM salvo em: {output_file}")
    else:
        print("\n✗ Falha na compilação")
        sys.exit(1)

if __name__ == "__main__":
    main()