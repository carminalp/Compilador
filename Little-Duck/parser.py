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
    '''PROGRAMA : PROGRAM ID SEMICOLON DEC_VARS DEC_FUNCS MAIN BODY END'''
    p[0] = p[2], p[4], p[5], p[7] 

# <DEC_VARS>
def p_dec_vars(p):
    '''DEC_VARS : epsilon
                | VARS'''
    if len(p) == 2:
        p[0] = ('DEC_VARS', p[1])
    else:
        p[0] = None

# <SOLO_FUNCS>
def p_solo_funcs(p):
    '''SOLO_FUNCS : FUNCS MAS_FUNCS'''
    p[0] = ('SOLO_FUNCS', p[1], p[2])

# <MAS_FUNCS>
def p_mas_funcs(p):
    '''MAS_FUNCS : epsilon
                 | SOLO_FUNCS'''
    if len(p) >= 2:
        p[0] = ('MAS_FUNCS', p[1])
    else:
        p[0] = None

# <DEC_FUNCS>
def p_dec_funcs(p):
    '''DEC_FUNCS : epsilon
                 | SOLO_FUNCS'''
    if len(p) == 2:
        p[0] = ('DEC_FUNCS', p[1])
    else:
        p[0] = None 

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
    '''MAS_VAR : epsilon
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
              | epsilon'''
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

#-----------#
## <FUNCS> ##
#-----------#
def p_funcs(p):
    '''FUNCS : VOID ID LEFT_PARENTHESIS PARAMETROS RIGHT_PARENTHESIS LEFT_BRACKET VARS_FUNC BODY RIGHT_BRACKET SEMICOLON'''
    p[0] = ('FUNCS', p[2], p[4], p[7], p[8])

# <PARAMETROS>
def p_parametros(p):
    '''PARAMETROS : epsilon
                  | DEC_PARAMETROS'''
    if len(p) == 2:
        p[0] = ('PARAMETROS', p[1])
    else:
        p[0] = None

# <DEC_PARAMETROS>
def p_dec_parametros(p):
    '''DEC_PARAMETROS : ID COLON TYPE LISTA_PARAMETROS'''
    p[0] = ('DEC_PARAMETROS', p[1], p[3], p[4])

# <LISTA_PARAMETROS>
def p_lista_parametros(p):
    '''LISTA_PARAMETROS : epsilon
                        | COMMA DEC_PARAMETROS'''
    if len(p) > 2:
        p[0] = ('LISTA_PARAMETROS', p[2])
    else:
        p[0] = None

# <VARS_FUNC>
def p_vars_func(p):
    '''VARS_FUNC : epsilon
                 | VARS'''
    if len(p) == 2:
        p[0] = ('VARS_FUNC', p[1])
    else:
        p[0] = None
 
#----------#
## <BODY> ##
#----------#
def p_body(p):
    '''BODY : LEFT_BRACE DEC_STATEMENTS RIGHT_BRACE'''
    p[0] = ('BODY', p[2])

# <DEC_STATEMENTS>
def p_dec_staments(p):
    '''DEC_STATEMENTS : epsilon
                      | LISTA_STATEMENTS'''
    if len(p) == 2:
        p[0] = ('DEC_STATEMENTS', p[1])
    else:
        p[0] = None

# <LISTA_STATEMENTS>
def p_lista_staments(p):
    '''LISTA_STATEMENTS : STATEMENT MAS_STATEMENTS'''
    p[0] = ('LISTA_STATEMENTS', p[1], p[2])

# <MAS_STATEMENTS>
def p_mas_staments(p):
    '''MAS_STATEMENTS : epsilon
                      | LISTA_STATEMENTS'''
    if len(p) >= 2:
        p[0] = ('MAS_STATEMENTS', p[1])
    else:
        p[0] = None

#---------------#
## <STATEMENT> ##
#---------------#
def p_statement(p):
    '''STATEMENT : ASSIGN
                 | CONDITION
                 | CYCLE
                 | F_CALL
    '''
    p[0] = ('STATEMENT', p[1])

#------------#
## <ASSIGN> ##
#------------#
def p_assign(p):
    'ASSIGN : ID EQUAL EXPRESION SEMICOLON'
    p[0] = ('ASSIGN', p[1], p[3])


## <EXPRESIÓN> ##
#---------------#
def p_expresion(p):
    '''EXPRESION : EXP MAS_EXPRESIONES'''
    p[0] = ('EXPRESION', p[1], p[2])

# <MAS_EXPRESIONES>
def p_mas_expresiones(p):
    '''MAS_EXPRESIONES : epsilon
                       | OPERADORES EXP'''
    if len(p) > 2:
        p[0] = ('MAS_EXPRESIONES', p[1], p[2])
    else:
        p[0] = None

# <OPERADORES>
def p_operadores(p):
    '''OPERADORES : GREATER_THAN
                  | LESS_THAN
                  | NOT_EQUAL'''
    p[0] = ('OPERADORES', p[1])

#---------#
## <EXP> ##
#---------#
def p_exp(p):
    '''EXP : TERMINO MAS_EXP'''
    p[0] = ('EXP', p[1], p[2])

# <MAS_EXP>
def p_mas_exp(p):
    '''MAS_EXP : OPERADORES_EXP EXP
               | epsilon'''
    if len(p) > 2:
        p[0] = ('MAS_EXP', p[1], p[2])
    else:
        p[0] = None

# <OPERADORES_EXP>
def p_operadores_exp(p):
    '''OPERADORES_EXP : PLUS
                      | MINUS'''
    p[0] = ('OPERADORES_EXP', p[1])

#--------------#
## <TERMINO> ##
#-------------#
def p_termino(p):
    '''TERMINO : FACTOR MAS_TERMINO'''
    p[0] = ('TERMINO', p[1], p[2])

# <MAS_TERMINO>
def p_mas_termino(p):
    '''MAS_TERMINO : epsilon
                   | OPERADORES_TER TERMINO'''
    if len(p) > 2:
        p[0] = ('MAS_TERMINO', p[1], p[2])
    else:
        p[0] = None

# <OPERADORES_TER>
def p_operadores_ter(p):
    '''OPERADORES_TER : MULTIPLICATION
                      | DIVISION'''
    p[0] = ('OPERADORES_TER', p[1])

#------------#
## <FACTOR> ##
#------------#
def p_factor(p):
    '''FACTOR : OPERADORES_FACTOR ID_CTE
              | LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS'''
    if len(p) == 4:
        p[0] = ('FACTOR', p[2])
    else:
        p[0] = ('FACTOR', p[1], p[2])
    
# <ID_CTE>
def p_id_cte(p):
    '''ID_CTE : ID
              | CTE'''
    p[0] = ('ID_CTE', p[1])

# <OPERADORES_FACTOR>
def p_operadores_factor(p):
    '''OPERADORES_FACTOR : PLUS
                         | MINUS
                         | epsilon'''
    if len(p) == 2:
        p[0] = ('OPERADORES_FACTOR', p[1])
    else:
        p[0] = None

#---------#
## <CTE> ##
#---------#
def p_cte(p):
    '''CTE : CTE_INT
           | CTE_FLOAT'''
    p[0] = ('CTE', p[1])

#---------------#
## <CONDITION> ##
#---------------#
def p_condition(p):
    '''CONDITION : IF LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS BODY ELSE_CONDITION'''
    p[0] = ('CONDITION', p[3], p[5], p[6])

# <ELSE_CONDITION>
def p_else(p):
    '''ELSE_CONDITION : epsilon
                      | ELSE BODY'''
    if len(p) == 3:
        p[0] = ('ELSE_CONDITION', p[2])
    else:
        p[0] = None

#-----------#
## <CYCLE> ##
#-----------#
def p_cycle(p):
    '''CYCLE : WHILE BODY DO LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS SEMICOLON'''
    p[0] = ('CYCLE', p[2], p[5])

#-----------#
## <F_CALL> ##
#-----------#
def p_f_call(p):
    '''F_CALL : ID LEFT_PARENTHESIS EXPRESIONES RIGHT_PARENTHESIS SEMICOLON'''
    p[0] = ('F_CALL', p[1], p[3])

# <EXPRESIONES>
def p_expresiones(p):
    '''EXPRESIONES : epsilon
                   | EXPRESIONES_F'''
    if len(p) == 2:
        p[0] = ('EXPRESIONES', p[1])
    else:
        p[0] = None

# <EXPRESIONES_F>
def p_expresiones_f(p):
    '''EXPRESIONES_F : EXPRESION LISTA_EXP'''
    p[0] = ('EXPRESIONES_F', p[1], p[2])

# <LISTA_EXP>
def p_lista_exp(p):
    '''LISTA_EXP : epsilon
                 | COMMA EXPRESIONES_F'''
    if len(p) > 2:
        p[0] = ('LISTA_EXP', p[2])
    else:
        p[0] = None

# Epsilon
def p_epsilon(p):
    'epsilon :'
    pass
    

data = '''
program carmina;
void caca (kk:int)[ 
    var carmina:int; 
    {ll = kk + i;}
];
main
{ 
    intento = yo+tu > ola;
    tu = kk;
    assignacion = factor * otro_factor + termino > uno; 
    factor = (1 * 30 + 5.0);
    factor = (1 * 30 + 5.0 > 6);

    if (5 > 2) {

    }

    while {lol = yolo;} do (ll);
    jojo(b,50);
}
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