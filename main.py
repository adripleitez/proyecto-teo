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


    [S, 'int', ['int', 'main', 'LPAREN', 'RPAREN', 'inicioBloque', S1, 'return', 'CONST_INT','finBloque']],
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
    [I, 'if', ['if', 'LPAREN', C, 'RPAREN', 'inicioBloque', S1, '"finBloque",', E]],
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
    [Q, 'for', ['for', 'LPAREN', 'ID', 'ASSIGNMENT', 'CONST_INT', 'finInstruccion', 'ID', O, F, 'finInstruccion', 'ID', P, 'RPAREN', 'inicioBloque', S1,'finBloque']],
    [Q, 'eof', None],
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
