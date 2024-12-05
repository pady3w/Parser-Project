grammar D3;

// Parser rules

program: (statement NEWLINE?)* EOF;

statement
    : assignmentStatement
    | expressionStatement
    | conditionalStatement
    | loopStatement
    | COMMENT
    ;

expressionStatement
    : expression
    ;

assignmentStatement
    : IDENTIFIER assignmentOperator expression
    ;

// Expression rules
expression
    : expression arithmeticOperator expression
    | unaryOperator expression
    | IDENTIFIER
    | NUMBER
    | STRING
    | BOOL
    | list
    | '(' expression ')'
    | IDENTIFIER '(' arguments? ')' 
    | NEWLINE
    | COMMENT
    ;

conditionalStatement
    : 'if' condition ':' NEWLINE* INDENT NEWLINE* block DEDENT NEWLINE*
      ('elif' condition ':' NEWLINE* INDENT NEWLINE* block DEDENT)* NEWLINE*
      ('else' ':' NEWLINE* INDENT NEWLINE* block DEDENT)? NEWLINE*
    ;

loopStatement
    : 'while' condition ':' NEWLINE* INDENT block DEDENT
    | 'for' IDENTIFIER 'in' expression ':' NEWLINE* INDENT block DEDENT
    ;

block
    : INDENT? (statement NEWLINE*)+ DEDENT?// Expect one or more statements in a block
    ;

condition
    : logicalTerm (logicalOperator logicalTerm)*
    ;

logicalTerm
    : comparison (comparisonOperator comparison)?
    | '(' condition ')'
    ;
    
arguments
    : expression (',' expression)*             # ArgumentList
    ;

comparison
    : expression
    | unaryOperator comparison
    ;

// List expression
list
    : '[' (expression (',' expression)*)? ']'
    ;

COMMENT
    : LINE_COMMENT
    | BLOCK_COMMENT
    ;

// Comparison Operators
comparisonOperator
    : '==' | '!=' | '<=' | '>=' | '<' | '>'
    ;

// Logical Operators
logicalOperator
    : 'and' | 'or'
    ;

// Unary operators
unaryOperator
    : 'not'
    | '-'
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
    : '+' | '-' | '*' | '/' | '%'
    ;

// Single-line comments
LINE_COMMENT
    : '#' ~[\r\n]* -> skip
    ;

// Multi-line comments
BLOCK_COMMENT
    :   '\'\'\'' .*? '\'\'\'' -> skip
    ;

// Lexer rules
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
STRING: '"' ( ESC_SEQ | ~["\\] )* '"' | '\'' ( ESC_SEQ | ~['\\] )* '\'';
BOOL: 'True' | 'False';
fragment ESC_SEQ: '\\' [bfnrt"'\\];

// Handling indentation
NEWLINE: [\r\n]+ ;
INDENT: '<INDENT>'; // Will be injected by preprocessor
DEDENT: '<DEDENT>'; // Will be injected by preprocessor
WS: [ ]+ -> skip;
