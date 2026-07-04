// Martin Arce Rodriguez 22030946
grammar Expr;

root : expr EOF ;

expr : EOF ;

NUM: [0-9]+;
MAYOR: '>' ;
ID: [a-zA-Z]+;
IF: 'if' ;
PARENTESIS_IZQUIERDO: '(';
PARENTESIS_DERECHO: ')';

WS: [ \t\r\n]+ -> skip; 