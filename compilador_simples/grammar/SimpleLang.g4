grammar SimpleLang;

// Regra principal
program: statement+ EOF;

// Statements
statement: assignment
         | expression ';'
         ;

assignment: ID '=' expression ';';

// Expressões
expression: expression ('*' | '/') expression   # MulDiv
          | expression ('+' | '-') expression   # AddSub
          | '(' expression ')'                  # Parentheses
          | ID                                  # Variable
          | NUMBER                              # Number
          ;

// Tokens
ID: [a-zA-Z][a-zA-Z0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;