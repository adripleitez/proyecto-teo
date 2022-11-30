import ply.lex as lex
from symbols import symbols
from symbols import getSymbol
from table import tabla
from table import first

# List of token names. Required
tokens = [
    "LPAREN",
    "RPAREN",
    "inicioBloque",
    "finBloque",
    "LBRACKET",
    "RBRACKET",
    "CONST_INT",
    "CONST_FLOAT",
    "CONST_CHAR",
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
    "finInstruccion",  # ;
    "COMMENT",
    "COMMENTBLOCK",
    "ASSIGNMENT",  # =
    "DOT",  # .
    "eof"  # $
]

reserved_words = {
    "main": "main",
    "int": "int",
    "void": "void",
    "return": "return",
    "float": "float",
    "char": "char",
    "struct": "struct",
    "if": "if",
    "else": "else",
    "do": "do",
    "while": "while",
    "for": "for",
    'break': 'break',  # se debe poner gramatica
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
t_INCREMENT = r"\+\+"
t_DECREMENT = r"\-\-"
t_DIFFERENT = r"\!\="
t_EQUALS = r"\=\="
t_LESS = r"\<"
t_GREATER = r"\>"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
t_ASSIGNMENT = r"\="
t_COMMA = r'\,'
t_DOT = r'\.'
t_eof = r'\$'


# A regular expression rule

def t_CONST_CHAR(t):
    r"(\')(.*)(\')"
    return t


def t_COMMENT(t):
    r"\/\/.*"
    pass


def t_COMMENTBLOCK(t):
    r"\/\*(.|\n)*\*\/"
    pass


def t_ID(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    t.type = reserved_words.get(t.value, "ID")  # Check for reserved words
    return t


def t_CONST_FLOAT(t):
    r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    t.value = float(t.value)
    return t


def t_CONST_INT(t):
    r"\d+(\.\d+)?"
    t.value = int(t.value)
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


stack = ['eof', 0]

# Build the lexer
lexer = lex.lex()


def miParser():
    f = open('fuente.c', 'r')
    f1 = f.read() + '\n$'
    lexer.input(f1)

    success = True
    tok = lexer.token()
    x = stack[-1]  # primer elemento de der a izq

    while True:
        flag = True
        if tok.type == x:
            expected = True

        # print("VALOR DE X")
        # print(x)
        # print("VALOR DE STACK")
        # print(stack)
        # print("--------------------------------------------------")

        if x == tok.type and x == 'eof':
            if success:
                print("\033[1;32mCadena terminada exitosamente")
            else:
                print("\u001b[31mCadena terminada con errores")
            return  # aceptar
        else:
            if x == tok.type and x != 'eof':
                # print("entró aqui")
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
                # print(tok)

            if x in tokens and x != tok.type:
                print("ERROR en línea: ", tok.lineno, " se esperaba ", symbols[x],
                      'en la posicion: ', tok.lexpos, "\n")
                f1 = getSymbol[x] + f1[tok.lexpos:]
                # print("\n", f1)
                lexer.input(f1)
                tok = lexer.token()
                flag = False
                success = False

            if x not in tokens and flag:  # es no terminal
                celda = buscar_en_tabla(x, tok.type)
                if celda is None:

                    print("ERROR en línea: ", tok.lineno, ", NO SE ESPERABA token de tipo ", tok.type,
                            "\n")

                    print("\nERROR en línea: ", tok.lineno, ", NO SE ESPERABA token de tipo ", tok.type,
                          "  se esperaba  ", x, "  en  '", tok.value, "'\n")
                    return
                    # f1 = f1[tok.lexpos + len(tok.value):]
                    # f1 = f1[f1.find('\n'):]
                    # lexer.input(f1)
                    # tok = lexer.token()
                    # success = False
                else:
                    stack.pop()
                    agregar_pila(celda)
                    x = stack[-1]
        # print("--------------------------------------------------\n\n")


def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if tabla[i][0] == no_terminal and tabla[i][1] == terminal:
            return tabla[i][2]  # retorno la celda


def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia':  # la vacía no la inserta
            stack.append(elemento)


def main():
    miParser()
    # f = open('fuente.c', 'r')
    # lexer.input(f.read())
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     # print(tok)
    #     print(tok.type, "elemento:    '", tok.value, "'      ", tok.lineno, tok.lexpos)


if __name__ == "__main__":
    main()
    # print(first)
