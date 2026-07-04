// Martin Arce Rodriguez 22030946
grammar Expr;

root : expr EOF ;

expr : EOF ;

PRINT: 'print';
CAD: '"'~[ \r\n]*'"';

WS: [ \t\r\n]+ -> skip; 