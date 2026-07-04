// Martin Arce Rodriguez 22030946
grammar Expr;

root : expr EOF ;

expr : EOF ;

NUM: [0-9]+ ;

MAS: '+' ;

WS: [ \t\r\n]+ -> skip; 