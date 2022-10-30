import ply.lex as lex

# List of token names. Required
tokens = [
    "LETTER",
    "NUMBER",
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
    "LPAREN",
    "RPAREN",
    "LBRACKET",
    "RBRACKET",
    "LBRACE",
    "RBRACE",
    "ID",
    "COMMA",
    "SEMICOLON",
    "APOSTROPHE",
    "QUOTE",
    "HASHTAG",
    "COMMENT",
    "COMMENTBLOCK",
    "ASSIGNMENT"
]

reserved_words = {
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "if": "IF",
    "else": "ELSE",
    "return": "RETURN",
    "void": "VOID",
    "do": "DO",
    "while": "WHILE",
    'break': 'BREAK',
    "define": "DEFINE",
    "include": "INCLUDE",
    "for": "FOR",
    "class":"CLASS"
}

# Add words reserved to tokens array
tokens += list(reserved_words.values())

# Regular expression rules
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_MOD = r"\%"
t_AND = r"\&\&"
t_OR = r"\|\|"
t_NOT = r"\!"
t_EQUALS = r"\=\="
t_LESS = r"\<"
t_GREATER = r"\>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_COMMA = r"\,"
t_SEMICOLON = r"\;"
t_APOSTROPHE = r"\'"
t_QUOTE = r"\""
t_HASHTAG = r"\#"
t_ASSIGNMENT = r"\="

# A regular expression rule with some action code
def t_COMMENT(t):
    r"\/\/.*"
    pass


def t_COMMENTBLOCK(t):
    r"\/\*(.|\n)*\*\/"
    pass

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
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
    r"\n+"
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

def miLexer():
    f = open('fuente.cpp','r')
    #lexer.input('3+4*_a23+-20*2')
    lexer.input(f.read())
    while True:
        tok=lexer.token()
        if not tok:
            break
        print(tok)
        print(tok.type, tok.value, tok.lineno, tok.lexpos)