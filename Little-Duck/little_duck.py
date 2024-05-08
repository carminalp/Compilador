"""
Como primera etapa se implementó, 
el proceso de análisis léxico y sintaxis 
usando la herramienta PLY.

Este archivo contiene el Scanner y el Parser 
basadas en las reglas gramaticales y expresiones 
regulares previamente definidas.

@author: Carmina López Palacios
"""
import ply.lex as lex

# Reserved Words
reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'end': 'END',
    'void': 'VOID',
    'var': 'VAR',
    'print': 'PRINT',
    'while': 'WHILE',
    'do': 'DO',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT'
}

# List of Tokens
tokens = [
    # Operadores
    'EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'NOT_EQUAL',
    'PLUS',
    'MINUS',
    'MULTIPLICATION',
    'DIVISION',
    # Separadores
    'COMMA',
    'SEMICOLON',
    # Delimitadores
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_PARENTHESIS',
    'RIGHT_PARENTHESIS',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    # Constantes y ID
    'ID',
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_STRING'
] + list(reserved.values())

# Regular expression rules for simple tokens

# Defines a token (USSING the prefix t_)
# And they are written using Python raw strings
t_EQUAL = r'='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_NOT_EQUAL = r'!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_COMMA = r','
t_SEMICOLON = r';'
t_LEFT_BRACE = r'{'
t_RIGHT_BRACE = r'}'
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'

# Regular expression rule for ID
def t_ID(t):
    r'[a-z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Revisar si es una palabra reservada
    return t

# Regular expression rule for float numbers
def t_CTE_FLOAT(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

# Regular expression rule for Int numbers
def t_CTE_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Regular expression rule for strings
def t_CTE_STRING(t):
    r'"[^"]*"'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test
data = '''
program main;
var a, b;
a = 10;
b = 20;
print("La suma es:", a + b);
end
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
