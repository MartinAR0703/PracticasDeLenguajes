# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,13,
        8,0,11,0,12,0,14,1,1,4,1,18,8,1,11,1,12,1,19,1,2,1,2,1,3,1,3,1,3,
        1,4,4,4,28,8,4,11,4,12,4,29,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,
        0,3,1,0,48,57,2,0,65,90,97,122,3,0,9,10,13,13,32,32,35,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,12,1,0,0,0,3,
        17,1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,27,1,0,0,0,11,13,7,0,0,0,
        12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,2,1,0,
        0,0,16,18,7,1,0,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,
        1,0,0,0,20,4,1,0,0,0,21,22,5,62,0,0,22,6,1,0,0,0,23,24,5,105,0,0,
        24,25,5,102,0,0,25,8,1,0,0,0,26,28,7,2,0,0,27,26,1,0,0,0,28,29,1,
        0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,6,4,0,0,32,
        10,1,0,0,0,4,0,14,19,29,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    ID = 2
    MAYOR_QUE = 3
    IF = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'>'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "ID", "MAYOR_QUE", "IF", "WS" ]

    ruleNames = [ "NUM", "ID", "MAYOR_QUE", "IF", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


