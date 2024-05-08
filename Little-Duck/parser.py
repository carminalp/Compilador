import ply.yacc as yacc
from lexer import tokens

# Define precedence and associativity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLICATION', 'DIVISION'),
)

# Formal grammar
# Using syntax Backus-Naur Form (BNF)

#--------------#
## <Programa> ##
#--------------#
def p_program(p):
    '''PROGRAMA : PROGRAM ID SEMICOLON DEC_VARS END'''
    p[0] = p[2], p[4]

# <DEC_VARS>
def p_dec_vars(p):
    '''DEC_VARS : empty
                | VARS'''
    if len(p) == 2:
        p[0] = ('DEC_VARS', p[1])
    else:
        p[0] = None

"""
# <SOLO_FUNCS>
def p_solo_funcs(p):
    '''SOLO_FUNCS : FUNCS MAS_FUNCS'''
    p[0] = ('SOLO_FUNCS', p[1], p[2])


# <MAS_FUNCS>
def p_mas_funcs(p):
    '''MAS_FUNCS : empty
                 | SOLO_FUNCS'''
    if len(p) > 2:
        p[0] = ('MAS_FUNCS', p[1])
    else:
        p[0] = None

# <DEC_FUNCS>
def p_dec_funcs(p):
    '''DEC_FUNCS : SOLO_FUNCS'''
    p[0] = ('DEC_FUNCS', p[1])
"""
#----------#
## <VARS> ##
#----------#
def p_vars(p):
    '''VARS : VAR LISTA_VAR'''
    p[0] = ('VARS', p[2])

# <LISTA_VAR>
def p_lista_var(p):
    '''LISTA_VAR : LISTA_ID COLON TYPE SEMICOLON MAS_VAR'''
    p[0] = ('LISTA_VAR', p[1], p[3], p[5])

# <MAS_VAR>
def p_mas_var(p):
    '''MAS_VAR : empty
               | LISTA_VAR'''
    if len(p) >= 2:
        p[0] = ('MAS_VAR', p[1])
    else:
        p[0] = None

# <LISTA_ID>
def p_lista_id(p):
    '''LISTA_ID : ID MAS_ID'''
    p[0] = ('LISTA_ID', p[1], p[2])

# <MAS_ID>
def p_mas_id(p):
    '''MAS_ID : COMMA LISTA_ID
              | empty'''
    if len(p) > 2:
        p[0] = ('MAS_ID', p[2])
    else:
        p[0] = None

#----------#
## <Type> ##
#----------#
def p_type(p):
    '''TYPE : INT
            | FLOAT'''
    p[0] = ('TYPE', p[1])
"""
#-----------#
## <FUNCS> ##
#-----------#
def p_funcs(p):
    '''FUNCS : VOID ID LEFT_PARENTHESIS PARAMETROS RIGHT_PARENTHESIS LEFT_BRACKET VARS_FUNCS BODY RIGHT_BRACKET SEMI_COLON'''
    p[0] = ('FUNCS', p[2], p[4], p[7],p[8])

# <PARAMETROS>
def p_parametros(p):
    '''PARAMETROS : empty
                  | DEC_PARAMETROS'''
    if len(p) == 2:
        p[0] = ('PARAMETROS', p[1])
    else:
        p[0] = None

# <DEC_PARAMETROS>
def p_dec_parametros(p):
    '''DEC_PARAMETROS : ID COLON TYPE LISTA_PARAMETROS'''
    p[0] = ('DEC_PARAMETROS', p[1], p[3], p[4])

def p_lista_parametros(p):
    '''LISTA_PARAMETROS : empty
                        | COMMA DEC_PARAMETROS'''
    if len(p) >= 2:
        p[0] = ('LISTA_PARAMETROS', p[2])
    else:
        p[0] = None

def p_vars_func(p):
    '''VARS_FUNC : empty
                 | VARS'''
    if len(p) == 2:
        p[0] = ('VARS_FUNC', p[1])
    else:
        p[0] = None

#-----------#
## <BODY> ##
#-----------#
def p_body(p):
    '''BODY : LEFT_PARENTHESIS RIGHT_PARENTHESIS'''
    p[0] = ('BODY')
"""
def p_empty(p):
    'empty :'
    pass
    

data = '''
program carmina;
var a : int; b, c : float;
end
'''

# Definir el parser
parser = yacc.yacc()

# Función para analizar la entrada
def parse_input(input_data):
    return parser.parse(input_data)

# Llamar a la función para analizar la entrada
parsed_result = parse_input(data)
print(parsed_result)