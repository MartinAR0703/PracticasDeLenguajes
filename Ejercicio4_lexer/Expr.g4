// Martin Arce Rodriguez 22030946
grammar Expr;

root : expr EOF ;

expr : EOF ;

NUM: [0-9]+ ;
ID: [a-zA-Z]+ ;
MAYOR_QUE: '>' ;
IF: 'if' ;

WS: [ \t\r\n]+ -> skip; 