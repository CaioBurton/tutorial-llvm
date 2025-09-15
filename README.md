# SimpleLang Compiler 🚀

Um compilador simples para a linguagem SimpleLang que gera código LLVM IR. Este projeto demonstra os conceitos básicos de construção de compiladores usando ANTLR para análise sintática e LLVM para geração de código.

## 📋 Características

- **Linguagem SimpleLang**: Uma linguagem simples com variáveis, expressões aritméticas e atribuições
- **Análise Sintática**: Usando ANTLR4 para gerar lexer e parser
- **Geração de Código**: Produz código LLVM IR otimizado
- **Suporte a Operações**: Adição, subtração, multiplicação, divisão e parênteses
- **Variáveis**: Declaração e uso de variáveis inteiras

## 🎯 Sintaxe da Linguagem

A linguagem SimpleLang suporta:

```
// Atribuições
x = 10;
y = 20;

// Expressões aritméticas
z = x + y * 2;
result = (x + y) / 2;

// Operadores suportados: +, -, *, /, ()
```

## 🛠️ Pré-requisitos

- Python 3.7+
- ANTLR 4.13.2 (incluído em `tools/antlr/`)
- Java Runtime Environment (para ANTLR)

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd compilador_simples
   ```

2. **Instale as dependências Python:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verifique se o Java está instalado:**
   ```bash
   java -version
   ```

## 🚀 Como Usar

### Compilação Básica

```bash
python run_compiler.py examples/simple.sl
```

### Exemplo de Uso

1. **Crie um arquivo `.sl` com código SimpleLang:**
   ```
   # arquivo: meu_programa.sl
   a = 5;
   b = 10;
   resultado = a + b * 2;
   ```

2. **Compile o arquivo:**
   ```bash
   python run_compiler.py meu_programa.sl
   ```

3. **Saída esperada:**
   ```
   Compilando: meu_programa.sl
   ==================================================
   Código fonte:
   a = 5;
   b = 10;
   resultado = a + b * 2;
   ==================================================
   === ANÁLISE SINTÁTICA ===
   ✓ Análise sintática concluída com sucesso
   
   === GERAÇÃO DE CÓDIGO ===
   ✓ Código LLVM gerado com sucesso
   
   === CÓDIGO LLVM IR ===
   [código LLVM gerado aqui]
   
   ✓ Compilação concluída com sucesso!
     Código LLVM salvo em: meu_programa.ll
   ```

## 📁 Estrutura do Projeto

```
compilador_simples/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
├── run_compiler.py          # Script principal do compilador
├── .gitignore               # Arquivo de ignore do Git
│
├── examples/                # Exemplos de código
│   ├── simple.sl           # Programa exemplo
│   └── simple.ll           # Código LLVM gerado
│
├── grammar/                 # Gramática ANTLR
│   └── SimpleLang.g4       # Definição da gramática
│
├── src/                     # Código fonte do compilador
│   ├── __init__.py
│   ├── compiler.py         # Classe principal do compilador
│   ├── lexer_parser.py     # Interface para ANTLR
│   ├── code_generator.py   # Gerador de código LLVM
│   └── grammar/            # Arquivos gerados pelo ANTLR
│       ├── __init__.py
│       ├── SimpleLangLexer.py
│       ├── SimpleLangParser.py
│       └── SimpleLangVisitor.py
│
└── tools/                   # Ferramentas auxiliares
    └── antlr/
        └── antlr-4.13.2-complete.jar
```

## 🔧 Desenvolvimento

### Regenerar o Parser ANTLR

Se você modificar a gramática (`grammar/SimpleLang.g4`), precisa regenerar os arquivos do parser:

```bash
# Windows
java -jar tools/antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/grammar grammar/SimpleLang.g4

# Linux/Mac
java -jar tools/antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/grammar grammar/SimpleLang.g4
```

### Estrutura do Compilador

1. **Análise Léxica/Sintática** (`lexer_parser.py`):
   - Usa ANTLR para tokenizar e fazer parsing do código
   - Gera uma árvore sintática abstrata (AST)

2. **Geração de Código** (`code_generator.py`):
   - Visita a AST usando o padrão Visitor
   - Gera código LLVM IR equivalente

3. **Compilador Principal** (`compiler.py`):
   - Coordena o processo de compilação
   - Gerencia erros e saída

## 📚 Exemplos

### Exemplo 1: Operações Básicas
```
x = 42;
y = x + 8;
```

### Exemplo 2: Expressões Complexas
```
a = 10;
b = 20;
c = 30;
resultado = (a + b) * c / 2;
```

### Exemplo 3: Precedência de Operadores
```
valor = 2 + 3 * 4;  // resultado: 14 (não 20)
```

## 🐛 Solução de Problemas

### Erro "Java não encontrado"
```bash
# Instale o Java Runtime Environment
# Windows: baixe do site oficial da Oracle
# Ubuntu: sudo apt install default-jre
# Mac: brew install openjdk
```

### Erro de dependências Python
```bash
# Reinstale as dependências
pip install --upgrade -r requirements.txt
```

### Problemas com ANTLR
```bash
# Verifique se o arquivo JAR existe
ls tools/antlr/antlr-4.13.2-complete.jar

# Regenere os arquivos do parser
java -jar tools/antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/grammar grammar/SimpleLang.g4
```

## 📄 Licença

Este projeto é licenciado sob a MIT License.

## 🔗 Recursos Úteis

- [ANTLR Documentation](https://www.antlr.org/)
- [LLVM Documentation](https://llvm.org/docs/)
- [llvmlite Documentation](https://llvmlite.readthedocs.io/)
- [Compiler Design Tutorial](https://www.tutorialspoint.com/compiler_design/)

**Desenvolvido como projeto educacional para aprender conceitos de compiladores** 📖
