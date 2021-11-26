grammar decaf;

fragment LETTER : [a-z] | [A-Z];
fragment DIGIT : [0-9] ;
ID : LETTER (LETTER | DIGIT)* ;
NUM : DIGIT (DIGIT)* ;
CHAR : '\'' LETTER '\'' ;
SPACES : [ \t\r\n\f]+ ->channel(HIDDEN) ;

program
    : 'class' 'Program' '{' (declaration)* '}' EOF
    ;

declaration
    : structDeclaration
    | varDeclaration
    | methodDeclaration
    ;

varDeclaration 
    : varType ID ';' #normalVar
    | varType ID '[' NUM ']' ';' #arrayVar
    ;

structDeclaration 
    : 'struct' ID '{' (varDeclaration)* '}' ';'
    ;

varType 
    : 'int' 
    | 'char' 
    | 'boolean' 
    | 'struct' ID 
    | structDeclaration 
    | 'void'
    ;

methodDeclaration
    : methodType ID '(' (parameter | parameter (',' parameter)*)? ')' block
    ;

methodType 
    : 'int' 
    | 'char' 
    | 'boolean'
    | 'void'
    ;

parameter 
    : parameterType ID
    | parameterType ID '[' ']'
    ;

parameterType
    : 'int' 
    | 'char' 
    | 'boolean'
    ;

block
    : '{' (varDeclaration)* (statement)* '}'
    ;

statement 
    : 'if' '(' expression ')' block1 = block ('else' block2 = block)? #ifScope
    | 'while' '(' expression ')' block #whileScope
    | 'return' (expression)? ';' #st_return
    | methodCall ';' #stmnt_methodCall
    | block #stmnt_block
    | left = location '=' right = expression #stmnt_equal
    | (expression)? ';' #stmnt_expression
    ;

location 
    : (ID | ID '[' expression ']') ('.' location)?
    ;

expression 
    : methodCall #expr_methodCall
    | location #exp_location
    | literal #expr_literal
    | left = expression pred_op right = expression #exp_predop
    | left = expression arith_op right = expression #exp_ar_op
    | left = expression rel_op right = expression #exp_relop
    | left = expression eq_op right = expression #exp_eqop
    | left = expression cond_op right = expression #exp_condop
    | '-' expression #ex_minus
    | '!' expression #ex_not
    | '(' expression ')' #ex_par
    ;

methodCall 
    : ID '(' (arg | arg (',' arg)*)? ')'
    ;

arg
    : expression
    ;

arith_op
    : '+'
    | '-'
    ;

pred_op
    : '*'
    | '/'
    | '%'
    ;

rel_op 
    : '<' 
    | '>' 
    | '<=' 
    | '>='
    ;

eq_op 
    : '==' 
    | '!='
    ;

cond_op 
    : '&&' 
    | '||'
    ;

literal 
    : int_Literal 
    | char_Literal 
    | bool_Literal
    ;

int_Literal 
    : NUM
    ;

char_Literal 
    : CHAR
    ;

bool_Literal 
    : 'true' 
    | 'false'
    ;