import ply.lex as lex

# List of token names. Required
tokens = [
    "LPAREN",
    "RPAREN",
    "inicioBloque",
    "finBloque",
    "CONST_INT",
    "CONST_FLOAT",
    "EMPTY",  # empty char
    "INCREMENT",    # ++
    "DECREMENT",    # --
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MOD",
    "AND",
    "OR",
    "NOT",
    "EQUALS",
    "LESS",
    "GREATER",
    "ID",
    "COMMA",
    "APOSTROPHE",   # '
    "finInstruccion",   # ;
    "COMMENT",
    "COMMENTBLOCK",
    "ASSIGNMENT",   # =
    "vacia"
    "eof"   # $
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
t_NOT = r"\!"
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
