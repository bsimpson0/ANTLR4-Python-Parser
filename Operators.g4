grammar Operators;

program: statement+;

statement: assignment
         | ifStatement
         | elifStatement
         | elseStatement
         | whileStatement
         | forStatement
         | array
         | ID
         | STRING
         | INTEGER
         | COMMENT
         | MLCOMMENT;

assignment: ID (assignmentOperator expression)?;


expression: ID
            | STRING
            | INTEGER
            | array
            | '(' logicalOperator? expression ')'
            | expression assignmentOperator expression
            | expression arithmeticOperator expression
            | expression comparisonOperator expression
            | expression logicalOperator expression;


assignmentOperator: EQUALS
                    | PLUSEQUALS
                    | MINUSEQUALS
                    | TIMESEQUALS
                    | DIVEQUALS
                    | NOTEQUALS
                    | COMPEQUALS;

arithmeticOperator: PLUS
                    | MINUS
                    | MULT
                    | DIV
                    | MOD;

comparisonOperator: GT
                    | LT
                    | GTE
                    | LTE;

logicalOperator: logicalAnd
                | logicalOr
                | logicalNot;

conditionalStatement: ifStatement
                    | elifStatement
                    | elseStatement
                    | whileStatement
                    | forStatement;



ifStatement: 'if' expression+ ':' (expression | statement | elifStatement | elseStatement) expression*;

elifStatement: 'elif' expression ':' (expression | statement | elseStatement) expression*;

elseStatement: 'else:' (expression | statement) expression*;

whileStatement: 'while' expression+ ':' (expression | whileStatement | elifStatement | ifStatement)*;

forStatement: 'for' expression forIn (expression | forRange) ':' (expression | statement) expression*;

logicalAnd: 'and';

logicalOr: 'or';

logicalNot: 'not';

forIn: 'in';

forRange: 'range' range;

range: ('(' INTEGER ',' INTEGER ')') | ('(' INTEGER ')');
      
array: '[' (expression (',' expression)*)? ']';


COMMENT: '#' ~[\r\n]* -> skip;
MLCOMMENT: '\'\'\'' .*? '\'\'\'' -> skip;
WS: [ \t\r\n]+ -> skip;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '\'' ( ~('\'' | '\\' | '\r' | '\n') | '\\' . | '\'\'' | '\\\'')* '\''
      | '"' ( ~('"' | '\\' | '\r' | '\n') | '\\' . | '""' | '\\"')* '"';

INTEGER: '-'? [0-9]+ ('.' [0-9]+)?;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQUALS: '=';
NOTEQUALS: '!=';
PLUSEQUALS: '+=';
MINUSEQUALS: '-=';
TIMESEQUALS: '*=';
DIVEQUALS: '/=';
COMPEQUALS: '==';
PARENTHESIS: '(' | ')';
BRACKET: '[' | ']';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';
