import ply.lex as lex

S = 0
D = 1
S1 = 2
I = 3
V = 4
W = 5
Q = 6
Q1 = 7
C = 8
P = 9
G = 10
E = 11
F = 12
L = 13
O = 14
V1 = 15
V2 = 16
V3 = 17
V4 = 18
V5 = 19
H = 20
N = 21
N1 = 22
R = 23
R1 = 24
B = 25
K = 26
A = 27
T1 = 28
Z = 29
T2 = 30
T3 = 31
T4 = 32
T5 = 33

# List of token names. Required
tokens = [
    "LPAREN",
    "RPAREN",
    "inicioBloque",
    "finBloque",
    "CONST_INT",
    "CONST_FLOAT",
    "EMPTY",  # empty char
    "INCREMENT",  # ++
    "DECREMENT",  # --
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MOD",
    "AND",
    "OR",
    "DIFFERENT",
    "EQUALS",
    "LESS",
    "GREATER",
    "ID",
    "COMMA",
    "APOSTROPHE",  # '
    "finInstruccion",  # ;
    "COMMENT",
    "COMMENTBLOCK",
    "ASSIGNMENT",  # =
    "DOT",  # .
    "eof"  # $
]

reserved_words = {
    "int": "INT",
    "main": "MAIN",
    "void": "VOID",
    "return": "RETURN",
    "float": "FLOAT",
    "char": "CHAR",
    "struct": "STRUCT",
    "if": "IF",
    "else": "ELSE",
    "do": "DO",
    "while": "WHILE",
    'break': 'BREAK',  # Se debe poner gramatica
    "for": "FOR"
}

# Add words reserved to tokens array
tokens += list(reserved_words.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r"\%"
t_AND = r"\&\&"
t_OR = r"\|\|"
t_DIFFERENT = r"\!\="
t_EQUALS = r"\=\="
t_LESS = r"\<"
t_GREATER = r"\>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
T_ASSIGNMENT = r'\='
t_APOSTROPHE = r"\'"
t_COMMA = r'\,'
t_DOT = r'\.'
t_eof = r'\$'


# A regular expression rule
def t_COMMENT(t):
    r"\/\/.*"
    pass


def t_COMMENTBLOCK(t):
    r"\/\*(.|\n)*\*\/"
    pass


def t_STRING(t):
    r'\".*\"'
    return t


def t_ID(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    t.type = reserved_words.get(t.value, "ID")  # Check for reserved words
    return t


def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = int(t.value)
    return t


def t_LETTER(t):
    r"\'.\'"
    t.value = t.value.replace("'", "")
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t


tabla2 = [
    [D, 'int', ['int']],
    [D, 'main', None],
    [D, 'LPAREN', None],
    [D, 'RPAREN', None],
    [D, 'void', None],
    [D, 'inicioBloque', None],
    [D, 'return', None],
    [D, 'finBloque', None],
    [D, 'CONST_INT', None],
    [D, 'CONST_FLOAT', None],
    [D, 'EMPTY', None],
    [D, 'char', ['char']],
    [D, 'struct', None],
    [D, 'float', ['float']],
    [D, 'MOD', None],
    [D, 'if', None],
    [D, 'else', None],
    [D, 'do', None],
    [D, 'while', None],
    [D, 'ID', None],
    [D, 'COMMA', None],
    [D, 'finInstruccion', None],
    [D, 'DECREMENT', None],
    [D, 'INCREMENT', None],
    [D, 'PLUS', None],
    [D, 'MINUS', None],
    [D, 'TIMES', None],
    [D, 'DIVIDE', None],
    [D, 'LESS', None],
    [D, 'GREATER', None],
    [D, 'ASSIGNMENT', None],
    [D, 'EQUALS', None],
    [D, 'DIFFERENT', None],
    [D, 'AND', None],
    [D, 'OR', None],
    [D, 'DOT', None],
    [D, 'APOSTROPHE', None],
    [D, 'for', None],
    [D, 'eof', None],

    [S, 'int', ['int', 'main', 'LPAREN', 'RPAREN', 'inicioBloque', S1, 'return', 'CONST_INT', 'finBloque']],
    [S, 'main', None],
    [S, 'LPAREN', None],
    [S, 'RPAREN', None],
    [S, 'void', None],
    [S, 'inicioBloque', None],
    [S, 'return', None],
    [S, 'finBloque', None],
    [S, 'CONST_INT', None],
    [S, 'CONST_FLOAT', None],
    [S, 'EMPTY', None],
    [S, 'char', None],
    [S, 'struct', None],
    [S, 'float', None],
    [S, 'MOD', None],
    [S, 'if', None],
    [S, 'else', None],
    [S, 'do', None],
    [S, 'while', None],
    [S, 'ID', None],
    [S, 'COMMA', None],
    [S, 'finInstruccion', None],
    [S, 'DECREMENT', None],
    [S, 'INCREMENT', None],
    [S, 'PLUS', None],
    [S, 'MINUS', None],
    [S, 'TIMES', None],
    [S, 'DIVIDE', None],
    [S, 'LESS', None],
    [S, 'GREATER', None],
    [S, 'ASSIGNMENT', None],
    [S, 'EQUALS', None],
    [S, 'DIFFERENT', None],
    [S, 'AND', None],
    [S, 'OR', None],
    [S, 'DOT', None],
    [S, 'APOSTROPHE', None],
    [S, 'for', None],
    [S, 'eof', ['int', 'main', 'LPAREN', 'RPAREN', 'inicioBloque', S1, 'return', 'CONST_INT', 'finBloque']],

    [S1, 'int', [V, S1]],
    [S1, 'main', None],
    [S1, 'LPAREN', None],
    [S1, 'RPAREN', None],
    [S1, 'void', None],
    [S1, 'inicioBloque', None],
    [S1, 'return', ['vacia']],
    [S1, 'finBloque', ['vacia']],
    [S1, 'CONST_INT', None],
    [S1, 'CONST_FLOAT', None],
    [S1, 'EMPTY', None],
    [S1, 'char', [V, S1]],
    [S1, 'struct', ['struct', 'ID', 'DOT', 'ID', 'ASSIGNMENT', B, 'finInstruccion', S1]],
    [S1, 'float', [V, S1]],
    [S1, 'MOD', None],
    [S1, 'if', [I, S1]],
    [S1, 'else', None],
    [S1, 'do', [G, S1]],
    [S1, 'while', [W, S1]],
    [S1, 'ID', ['ID', 'LPAREN', T2, 'RPAREN', 'finInstruccion', S1]],
    [S1, 'COMMA', None],
    [S1, 'finInstruccion', None],
    [S1, 'DECREMENT', None],
    [S1, 'INCREMENT', None],
    [S1, 'PLUS', None],
    [S1, 'MINUS', None],
    [S1, 'TIMES', None],
    [S1, 'DIVIDE', None],
    [S1, 'LESS', None],
    [S1, 'GREATER', None],
    [S1, 'ASSIGNMENT', None],
    [S1, 'EQUALS', None],
    [S1, 'DIFFERENT', None],
    [S1, 'AND', None],
    [S1, 'OR', None],
    [S1, 'DOT', None],
    [S1, 'APOSTROPHE', None],
    [S1, 'for', [Q, S1]],
    [S1, 'eof', None],

    [I, 'int', None],
    [I, 'main', None],
    [I, 'LPAREN', None],
    [I, 'RPAREN', None],
    [I, 'void', None],
    [I, 'inicioBloque', None],
    [I, 'return', None],
    [I, 'finBloque', None],
    [I, 'CONST_INT', None],
    [I, 'CONST_FLOAT', None],
    [I, 'EMPTY', None],
    [I, 'char', None],
    [I, 'struct', None],
    [I, 'float', None],
    [I, 'MOD', None],
    [I, 'if', ['if', 'LPAREN', C, 'RPAREN', 'inicioBloque', S1, 'finBloque', E]],
    [I, 'else', None],
    [I, 'do', None],
    [I, 'while', None],
    [I, 'ID', None],
    [I, 'COMMA', None],
    [I, 'finInstruccion', None],
    [I, 'DECREMENT', None],
    [I, 'INCREMENT', None],
    [I, 'PLUS', None],
    [I, 'MINUS', None],
    [I, 'TIMES', None],
    [I, 'DIVIDE', None],
    [I, 'LESS', None],
    [I, 'GREATER', None],
    [I, 'ASSIGNMENT', None],
    [I, 'EQUALS', None],
    [I, 'DIFFERENT', None],
    [I, 'AND', None],
    [I, 'OR', None],
    [I, 'DOT', None],
    [I, 'APOSTROPHE', None],
    [I, 'for', None],
    [I, 'eof', None],

    [V, 'int', [D, 'ID', V1]],
    [V, 'main', None],
    [V, 'LPAREN', None],
    [V, 'RPAREN', None],
    [V, 'void', None],
    [V, 'inicioBloque', None],
    [V, 'return', None],
    [V, 'finBloque', None],
    [V, 'CONST_INT', None],
    [V, 'CONST_FLOAT', None],
    [V, 'EMPTY', None],
    [V, 'char', [D, 'ID', V1]],
    [V, 'struct', None],
    [V, 'float', [D, 'ID', V1]],
    [V, 'MOD', None],
    [V, 'if', None],
    [V, 'else', None],
    [V, 'do', None],
    [V, 'while', None],
    [V, 'ID', None],
    [V, 'COMMA', None],
    [V, 'finInstruccion', None],
    [V, 'DECREMENT', None],
    [V, 'INCREMENT', None],
    [V, 'PLUS', None],
    [V, 'MINUS', None],
    [V, 'TIMES', None],
    [V, 'DIVIDE', None],
    [V, 'LESS', None],
    [V, 'GREATER', None],
    [V, 'ASSIGNMENT', None],
    [V, 'EQUALS', None],
    [V, 'DIFFERENT', None],
    [V, 'AND', None],
    [V, 'OR', None],
    [V, 'DOT', None],
    [V, 'APOSTROPHE', None],
    [V, 'for', None],
    [V, 'eof', None],

    [W, 'int', None],
    [W, 'main', None],
    [W, 'LPAREN', None],
    [W, 'RPAREN', None],
    [W, 'void', None],
    [W, 'inicioBloque', None],
    [W, 'return', None],
    [W, 'finBloque', None],
    [W, 'CONST_INT', None],
    [W, 'CONST_FLOAT', None],
    [W, 'EMPTY', None],
    [W, 'char', None],
    [W, 'struct', None],
    [W, 'float', None],
    [W, 'MOD', None],
    [W, 'if', None],
    [W, 'else', None],
    [W, 'do', None],
    [W, 'while', ['while', 'LPAREN', C, 'RPAREN', 'inicioBloque', S1, 'finBloque']],
    [W, 'ID', None],
    [W, 'COMMA', None],
    [W, 'finInstruccion', None],
    [W, 'DECREMENT', None],
    [W, 'INCREMENT', None],
    [W, 'PLUS', None],
    [W, 'MINUS', None],
    [W, 'TIMES', None],
    [W, 'DIVIDE', None],
    [W, 'LESS', None],
    [W, 'GREATER', None],
    [W, 'ASSIGNMENT', None],
    [W, 'EQUALS', None],
    [W, 'DIFFERENT', None],
    [W, 'AND', None],
    [W, 'OR', None],
    [W, 'DOT', None],
    [W, 'APOSTROPHE', None],
    [W, 'for', None],
    [W, 'eof', None],

    [Q, 'int', None],
    [Q, 'main', None],
    [Q, 'LPAREN', None],
    [Q, 'RPAREN', None],
    [Q, 'void', None],
    [Q, 'inicioBloque', None],
    [Q, 'return', None],
    [Q, 'finBloque', None],
    [Q, 'CONST_INT', None],
    [Q, 'CONST_FLOAT', None],
    [Q, 'EMPTY', None],
    [Q, 'char', None],
    [Q, 'struct', None],
    [Q, 'float', None],
    [Q, 'MOD', None],
    [Q, 'if', None],
    [Q, 'else', None],
    [Q, 'do', None],
    [Q, 'while', None],
    [Q, 'ID', None],
    [Q, 'COMMA', None],
    [Q, 'finInstruccion', None],
    [Q, 'DECREMENT', None],
    [Q, 'INCREMENT', None],
    [Q, 'PLUS', None],
    [Q, 'MINUS', None],
    [Q, 'TIMES', None],
    [Q, 'DIVIDE', None],
    [Q, 'LESS', None],
    [Q, 'GREATER', None],
    [Q, 'ASSIGNMENT', None],
    [Q, 'EQUALS', None],
    [Q, 'DIFFERENT', None],
    [Q, 'AND', None],
    [Q, 'OR', None],
    [Q, 'DOT', None],
    [Q, 'APOSTROPHE', None],
    [Q, 'for',
     ['for', 'LPAREN', 'ID', 'ASSIGNMENT', 'CONST_INT', 'finInstruccion', 'ID', O, F, 'finInstruccion', 'ID', P,
      'RPAREN', 'inicioBloque', S1, 'finBloque']],
    [Q, 'eof', None],

    # Isma
    [Q1, 'int', None],
    [Q1, 'main', None],
    [Q1, 'LPAREN', None],
    [Q1, 'RPAREN', None],
    [Q1, 'void', None],
    [Q1, 'inicioBloque', None],
    [Q1, 'return', None],
    [Q1, 'finBloque', None],
    [Q1, 'CONST_INT', None],
    [Q1, 'CONST_FLOAT', None],
    [Q1, 'EMPTY', None],
    [Q1, 'char', None],
    [Q1, 'struct', None],
    [Q1, 'float', None],
    [Q1, 'MOD', None],
    [Q1, 'if', None],
    [Q1, 'else', None],
    [Q1, 'do', None],
    [Q1, 'while', None],
    [Q1, 'ID', [T1, Z]],
    [Q1, 'COMMA', None],
    [Q1, 'finInstruccion', None],
    [Q1, 'DECREMENT', None],
    [Q1, 'INCREMENT', None],
    [Q1, 'PLUS', None],
    [Q1, 'MINUS', None],
    [Q1, 'TIMES', None],
    [Q1, 'DIVIDE', None],
    [Q1, 'LESS', None],
    [Q1, 'GREATER', None],
    [Q1, 'ASSIGNMENT', None],
    [Q1, 'EQUALS', None],
    [Q1, 'DIFFERENT', None],
    [Q1, 'AND', None],
    [Q1, 'OR', None],
    [Q1, 'DOT', None],
    [Q1, 'APOSTROPHE', None],
    [Q1, 'for', None],
    [Q1, 'eof', None],

    [C, 'int', None],
    [C, 'main', None],
    [C, 'LPAREN', None],
    [C, 'RPAREN', None],
    [C, 'void', None],
    [C, 'inicioBloque', None],
    [C, 'return', None],
    [C, 'finBloque', None],
    [C, 'CONST_INT', [F, O, F, L]],
    [C, 'CONST_FLOAT', None],
    [C, 'EMPTY', None],
    [C, 'char', None],
    [C, 'struct', None],
    [C, 'float', None],
    [C, 'MOD', None],
    [C, 'if', None],
    [C, 'else', None],
    [C, 'do', None],
    [C, 'while', None],
    [C, 'ID', [F, O, F, L]],
    [C, 'COMMA', None],
    [C, 'finInstruccion', None],
    [C, 'DECREMENT', None],
    [C, 'INCREMENT', None],
    [C, 'PLUS', None],
    [C, 'MINUS', None],
    [C, 'TIMES', None],
    [C, 'DIVIDE', None],
    [C, 'LESS', None],
    [C, 'GREATER', None],
    [C, 'ASSIGNMENT', None],
    [C, 'EQUALS', None],
    [C, 'DIFFERENT', None],
    [C, 'AND', None],
    [C, 'OR', None],
    [C, 'DOT', None],
    [C, 'APOSTROPHE', None],
    [C, 'for', None],
    [C, 'eof', None],

    [P, 'int', None],
    [P, 'main', None],
    [P, 'LPAREN', None],
    [P, 'RPAREN', None],
    [P, 'void', None],
    [P, 'inicioBloque', None],
    [P, 'return', None],
    [P, 'finBloque', None],
    [P, 'CONST_INT', None],
    [P, 'CONST_FLOAT', None],
    [P, 'EMPTY', None],
    [P, 'char', None],
    [P, 'struct', None],
    [P, 'float', None],
    [P, 'MOD', None],
    [P, 'if', None],
    [P, 'else', None],
    [P, 'do', None],
    [P, 'while', None],
    [P, 'ID', None],
    [P, 'COMMA', None],
    [P, 'finInstruccion', None],
    [P, 'DECREMENT', ['DECREMENT']],
    [P, 'INCREMENT', ['INCREMENT']],
    [P, 'PLUS', None],
    [P, 'MINUS', None],
    [P, 'TIMES', None],
    [P, 'DIVIDE', None],
    [P, 'LESS', None],
    [P, 'GREATER', None],
    [P, 'ASSIGNMENT', None],
    [P, 'EQUALS', None],
    [P, 'DIFFERENT', None],
    [P, 'AND', None],
    [P, 'OR', None],
    [P, 'DOT', None],
    [P, 'APOSTROPHE', None],
    [P, 'for', None],
    [P, 'eof', None],

    [G, 'int', None],
    [G, 'main', None],
    [G, 'LPAREN', None],
    [G, 'RPAREN', None],
    [G, 'void', None],
    [G, 'inicioBloque', None],
    [G, 'return', None],
    [G, 'finBloque', None],
    [G, 'CONST_INT', None],
    [G, 'CONST_FLOAT', None],
    [G, 'EMPTY', None],
    [G, 'char', None],
    [G, 'struct', None],
    [G, 'float', None],
    [G, 'MOD', None],
    [G, 'if', None],
    [G, 'else', None],
    [G, 'do', ['do', 'inicioBloque', S1, 'finBloque', 'while', 'LPAREN', C, 'RPAREN']],
    [G, 'while', None],
    [G, 'ID', None],
    [G, 'COMMA', None],
    [G, 'finInstruccion', None],
    [G, 'DECREMENT', None],
    [G, 'INCREMENT', None],
    [G, 'PLUS', None],
    [G, 'MINUS', None],
    [G, 'TIMES', None],
    [G, 'DIVIDE', None],
    [G, 'LESS', None],
    [G, 'GREATER', None],
    [G, 'ASSIGNMENT', None],
    [G, 'EQUALS', None],
    [G, 'DIFFERENT', None],
    [G, 'AND', None],
    [G, 'OR', None],
    [G, 'DOT', None],
    [G, 'APOSTROPHE', None],
    [G, 'for', None],
    [G, 'eof', None],

    [E, 'int', ['vacia']],
    [E, 'main', None],
    [E, 'LPAREN', None],
    [E, 'RPAREN', None],
    [E, 'void', None],
    [E, 'inicioBloque', None],
    [E, 'return', None],
    [E, 'finBloque', None],
    [E, 'CONST_INT', None],
    [E, 'CONST_FLOAT', None],
    [E, 'EMPTY', None],
    [E, 'char', ['vacia']],
    [E, 'struct', None],
    [E, 'float', ['vacia']],
    [E, 'MOD', None],
    [E, 'if', ['vacia']],
    [E, 'else', ['else', 'inicioBloque', S1, 'finBloque']],
    [E, 'do', ['vacia']],
    [E, 'while', ['vacia']],
    [E, 'ID', ['vacia']],
    [E, 'COMMA', None],
    [E, 'finInstruccion', None],
    [E, 'DECREMENT', None],
    [E, 'INCREMENT', None],
    [E, 'PLUS', None],
    [E, 'MINUS', None],
    [E, 'TIMES', None],
    [E, 'DIVIDE', None],
    [E, 'LESS', None],
    [E, 'GREATER', None],
    [E, 'ASSIGNMENT', None],
    [E, 'EQUALS', None],
    [E, 'DIFFERENT', None],
    [E, 'AND', None],
    [E, 'OR', None],
    [E, 'DOT', None],
    [E, 'APOSTROPHE', None],
    [E, 'for', ['vacia']],
    [E, 'eof', None],

    [F, 'int', None],
    [F, 'main', None],
    [F, 'LPAREN', None],
    [F, 'RPAREN', None],
    [F, 'void', None],
    [F, 'inicioBloque', None],
    [F, 'return', None],
    [F, 'finBloque', None],
    [F, 'CONST_INT', ['CONST_INT']],
    [F, 'CONST_FLOAT', None],
    [F, 'EMPTY', None],
    [F, 'char', None],
    [F, 'struct', None],
    [F, 'float', None],
    [F, 'MOD', None],
    [F, 'if', None],
    [F, 'else', None],
    [F, 'do', None],
    [F, 'while', None],
    [F, 'ID', 'ID'],
    [F, 'COMMA', None],
    [F, 'finInstruccion', None],
    [F, 'DECREMENT', None],
    [F, 'INCREMENT', None],
    [F, 'PLUS', None],
    [F, 'MINUS', None],
    [F, 'TIMES', None],
    [F, 'DIVIDE', None],
    [F, 'LESS', None],
    [F, 'GREATER', None],
    [F, 'ASSIGNMENT', None],
    [F, 'EQUALS', None],
    [F, 'DIFFERENT', None],
    [F, 'AND', None],
    [F, 'OR', None],
    [F, 'DOT', None],
    [F, 'APOSTROPHE', None],
    [F, 'for', None],
    [F, 'eof', None],

    [L, 'int', None],
    [L, 'main', None],
    [L, 'LPAREN', None],
    [L, 'RPAREN', ['vacia']],
    [L, 'void', None],
    [L, 'inicioBloque', None],
    [L, 'return', None],
    [L, 'finBloque', None],
    [L, 'CONST_INT', None],
    [L, 'CONST_FLOAT', None],
    [L, 'EMPTY', None],
    [L, 'char', None],
    [L, 'struct', None],
    [L, 'float', None],
    [L, 'MOD', None],
    [L, 'if', None],
    [L, 'else', None],
    [L, 'do', None],
    [L, 'while', None],
    [L, 'ID', 'ID'],
    [L, 'COMMA', None],
    [L, 'finInstruccion', None],
    [L, 'DECREMENT', None],
    [L, 'INCREMENT', None],
    [L, 'PLUS', None],
    [L, 'MINUS', None],
    [L, 'TIMES', None],
    [L, 'DIVIDE', None],
    [L, 'LESS', [O, F, L]],
    [L, 'GREATER', [O, F, L]],
    [L, 'ASSIGNMENT', None],
    [L, 'EQUALS', [O, F, L]],
    [L, 'DIFFERENT', [O, F, L]],
    [L, 'AND', [O, F, L]],
    [L, 'OR', [O, F, L]],
    [L, 'DOT', None],
    [L, 'APOSTROPHE', None],
    [L, 'for', None],
    [L, 'eof', None],

    # Plei
    [O, 'int', None],
    [O, 'main', None],
    [O, 'LPAREN', None],
    [O, 'RPAREN', None],
    [O, 'void', None],
    [O, 'inicioBloque', None],
    [O, 'return', None],
    [O, 'finBloque', None],
    [O, 'CONST_INT', None],
    [O, 'CONST_FLOAT', None],
    [O, 'EMPTY', None],
    [O, 'char', None],
    [O, 'struct', None],
    [O, 'float', None],
    [O, 'if', None],
    [O, 'else', None],
    [O, 'do', None],
    [O, 'while', None],
    [O, 'ID', None],
    [O, 'COMMA', None],
    [O, 'finInstruccion', None],
    [O, 'DECREMENT', None],
    [O, 'INCREMENT', None],
    [O, 'TIMES', None],
    [O, 'MINUS', None],
    [O, 'PLUS', None],
    [O, 'DIVIDE', None],
    [O, 'LESS', ['LESS']],
    [O, 'GREATER', ['GREATER']],
    [O, 'ASSIGNMENT', None],
    [O, 'EQUALS', ['EQUALS']],
    [O, 'DIFFERENT', ['DIFFERENT']],
    [O, 'AND', ['AND']],
    [O, 'OR', ['OR']],
    [O, 'DOT', None],
    [O, 'APOSTROPHE', None],
    [O, 'for', None],
    [O, 'eof', None],
    [V1, 'int', None],
    [V1, 'main', None],
    [V1, 'LPAREN', None],
    [V1, 'RPAREN', None],
    [V1, 'void', None],
    [V1, 'inicioBloque', None],
    [V1, 'return', None],
    [V1, 'finBloque', None],
    [V1, 'CONST_INT', None],
    [V1, 'CONST_FLOAT', None],
    [V1, 'EMPTY', None],
    [V1, 'char', None],
    [V1, 'struct', None],
    [V1, 'float', None],
    [V1, 'if', None],
    [V1, 'else', None],
    [V1, 'do', None],
    [V1, 'while', None],
    [V1, 'ID', None],
    [V1, 'COMMA', ['COMMA', 'ID', V1]],
    [V1, 'finInstruccion', ['finInstruccion']],
    [V1, 'DECREMENT', None],
    [V1, 'INCREMENT', None],
    [V1, 'TIMES', None],
    [V1, 'MINUS', None],
    [V1, 'PLUS', None],
    [V1, 'DIVIDE', None],
    [V1, 'LESS', None],
    [V1, 'GREATER', None],
    [V1, 'ASSIGNMENT', None],
    [V1, 'EQUALS', ['EQUALS', V2]],
    [V1, 'DIFFERENT', None],
    [V1, 'AND', None],
    [V1, 'OR', None],
    [V1, 'DOT', None],
    [V1, 'APOSTROPHE', None],
    [V1, 'for', None],
    [V1, 'eof', None],
    [V2, 'int', None],
    [V2, 'main', None],
    [V2, 'LPAREN', None],
    [V2, 'RPAREN', None],
    [V2, 'void', None],
    [V2, 'inicioBloque', None],
    [V2, 'return', None],
    [V2, 'finBloque', None],
    [V2, 'CONST_INT', [V3, V4]],
    [V2, 'CONST_FLOAT', [V3, V4]],
    [V2, 'EMPTY', [V3, V4]],
    [V2, 'char', None],
    [V2, 'struct', None],
    [V2, 'float', None],
    [V2, 'if', None],
    [V2, 'else', None],
    [V2, 'do', None],
    [V2, 'while', None],
    [V2, 'ID', None],
    [V2, 'COMMA', None],
    [V2, 'finInstruccion', None],
    [V2, 'DECREMENT', None],
    [V2, 'INCREMENT', None],
    [V2, 'TIMES', None],
    [V2, 'MINUS', None],
    [V2, 'PLUS', None],
    [V2, 'DIVIDE', None],
    [V2, 'LESS', None],
    [V2, 'GREATER', None],
    [V2, 'ASSIGNMENT', None],
    [V2, 'EQUALS', None],
    [V2, 'DIFFERENT', None],
    [V2, 'AND', None],
    [V2, 'OR', None],
    [V2, 'DOT', None],
    [V2, 'APOSTROPHE', ['APOSTROPHE', 'ID', 'APOSTROPHE', V5]],
    [V2, 'for', None],
    [V2, 'eof', None],
    [V3, 'int', None],
    [V3, 'main', None],
    [V3, 'LPAREN', None],
    [V3, 'RPAREN', None],
    [V3, 'void', None],
    [V3, 'inicioBloque', None],
    [V3, 'return', None],
    [V3, 'finBloque', None],
    [V3, 'CONST_INT', ['CONST_INT']],
    [V3, 'CONST_FLOAT', ['CONST_FLOAT']],
    [V3, 'EMPTY', ['EMPTY']],
    [V3, 'char', None],
    [V3, 'struct', None],
    [V3, 'float', None],
    [V3, 'if', None],
    [V3, 'else', None],
    [V3, 'do', None],
    [V3, 'while', None],
    [V3, 'ID', None],
    [V3, 'COMMA', None],
    [V3, 'finInstruccion', None],
    [V3, 'DECREMENT', None],
    [V3, 'INCREMENT', None],
    [V3, 'TIMES', None],
    [V3, 'MINUS', None],
    [V3, 'PLUS', None],
    [V3, 'DIVIDE', None],
    [V3, 'LESS', None],
    [V3, 'GREATER', None],
    [V3, 'ASSIGNMENT', None],
    [V3, 'EQUALS', None],
    [V3, 'DIFFERENT', None],
    [V3, 'AND', None],
    [V3, 'OR', None],
    [V3, 'DOT', None],
    [V3, 'APOSTROPHE', None],
    [V3, 'for', None],
    [V3, 'eof', None],
    [V4, 'int', None],
    [V4, 'main', None],
    [V4, 'LPAREN', None],
    [V4, 'RPAREN', None],
    [V4, 'void', None],
    [V4, 'inicioBloque', None],
    [V4, 'return', None],
    [V4, 'finBloque', None],
    [V4, 'CONST_INT', None],
    [V4, 'CONST_FLOAT', None],
    [V4, 'EMPTY', None],
    [V4, 'char', None],
    [V4, 'struct', None],
    [V4, 'float', None],
    [V4, 'if', None],
    [V4, 'else', None],
    [V4, 'do', None],
    [V4, 'while', None],
    [V4, 'ID', None],
    [V4, 'COMMA', ['COMMA', 'ID', V1]],
    [V4, 'finInstruccion', ['finInstruccion']],
    [V4, 'DECREMENT', None],
    [V4, 'INCREMENT', None],
    [V4, 'TIMES', None],
    [V4, 'MINUS', None],
    [V4, 'PLUS', None],
    [V4, 'DIVIDE', None],
    [V4, 'LESS', None],
    [V4, 'GREATER', None],
    [V4, 'ASSIGNMENT', None],
    [V4, 'EQUALS', None],
    [V4, 'DIFFERENT', None],
    [V4, 'AND', None],
    [V4, 'OR', None],
    [V4, 'DOT', None],
    [V4, 'APOSTROPHE', None],
    [V4, 'for', None],
    [V4, 'eof', None],
    [V5, 'int', None],
    [V5, 'main', None],
    [V5, 'LPAREN', None],
    [V5, 'RPAREN', None],
    [V5, 'void', None],
    [V5, 'inicioBloque', None],
    [V5, 'return', None],
    [V5, 'finBloque', None],
    [V5, 'CONST_INT', None],
    [V5, 'CONST_FLOAT', None],
    [V5, 'EMPTY', None],
    [V5, 'char', None],
    [V5, 'struct', None],
    [V5, 'float', None],
    [V5, 'if', None],
    [V5, 'else', None],
    [V5, 'do', None],
    [V5, 'while', None],
    [V5, 'ID', None],
    [V5, 'COMMA', ['COMMA', 'ID', V1]],
    [V5, 'finInstruccion', ['finInstruccion']],
    [V5, 'DECREMENT', None],
    [V5, 'INCREMENT', None],
    [V5, 'TIMES', None],
    [V5, 'MINUS', None],
    [V5, 'PLUS', None],
    [V5, 'DIVIDE', None],
    [V5, 'LESS', None],
    [V5, 'GREATER', None],
    [V5, 'ASSIGNMENT', None],
    [V5, 'EQUALS', None],
    [V5, 'DIFFERENT', None],
    [V5, 'AND', None],
    [V5, 'OR', None],
    [V5, 'DOT', None],
    [V5, 'APOSTROPHE', None],
    [V5, 'for', None],
    [V5, 'eof', None],
    [H, 'int', None],
    [H, 'main', None],
    [H, 'LPAREN', None],
    [H, 'RPAREN', None],
    [H, 'void', None],
    [H, 'inicioBloque', None],
    [H, 'return', None],
    [H, 'finBloque', None],
    [H, 'CONST_INT', None],
    [H, 'CONST_FLOAT', None],
    [H, 'EMPTY', None],
    [H, 'char', None],
    [H, 'struct', ['struct', 'inicioBloque', V, 'finBloque', N]],
    [H, 'float', None],
    [H, 'if', None],
    [H, 'else', None],
    [H, 'do', None],
    [H, 'while', None],
    [H, 'ID', None],
    [H, 'COMMA', None],
    [H, 'finInstruccion', None],
    [H, 'DECREMENT', None],
    [H, 'INCREMENT', None],
    [H, 'TIMES', None],
    [H, 'MINUS', None],
    [H, 'PLUS', None],
    [H, 'DIVIDE', None],
    [H, 'LESS', None],
    [H, 'GREATER', None],
    [H, 'ASSIGNMENT', None],
    [H, 'EQUALS', None],
    [H, 'DIFFERENT', None],
    [H, 'AND', None],
    [H, 'OR', None],
    [H, 'DOT', None],
    [H, 'APOSTROPHE', None],
    [H, 'for', None],
    [H, 'eof', ['struct', 'inicioBloque', V, 'finBloque', N]]

]

# Build the lexer
lexer = lex.lex()


def main():
    f = open('fuente.cpp', 'r')
    lexer.input(f.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        print(tok.type, tok.value, tok.lineno, tok.lexpos)


if __name__ == "__main__":
    main()
