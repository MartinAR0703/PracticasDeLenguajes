// Martin Arce Rodriguez 22030946
grammar Expr;

root : expr EOF ;

expr : EOF ;

ID : [a-zA-Z]+;
NUM: [0-9]+ ;
IGUAL: '=' ;
INT: 'int' ;

WS: [ \t\r\n]+ -> skip; 