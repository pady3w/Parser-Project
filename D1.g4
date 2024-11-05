grammar D1;

// Parser rules
program: statement* EOF;

statement
    : assignmentStatement
    | expressionStatement
    ;

expressionStatement
    : expression // No semicolon required
    ;

assignmentStatement
    : IDENTIFIER assignmentOperator expression
    ;

// Expression rules
expression
    : expression arithmeticOperator expression    // For arithmetic expressions
    | IDENTIFIER                                  // Variable identifier
    | NUMBER                                      // Integer or floating-point
    | STRING                                      // String literal
    | list                                        // List expression
    | '(' expression ')'                          // Parentheses
    ;

// List expression
list
    : '[' (expression (',' expression)*)? ']'    // List of expressions, optional
    ;

// Assignment operators
assignmentOperator
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    ;

// Arithmetic operators
arithmeticOperator
    : '+'
    | '-'
    | '*'
    | '/'
    | '%'
    ;

// Lexer rules
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?; // Support for integers and floating-point numbers
STRING: '"' ( ESC_SEQ | ~["\\] )* '"' | '\'' ( ESC_SEQ | ~['\\] )* '\''; // Enhanced string handling
fragment ESC_SEQ: '\\' [bfnrt"'\\]; // Escape sequences
WS: [ \t\r\n]+ -> skip; // Ignore whitespace