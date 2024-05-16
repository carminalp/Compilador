"""
Como primera etapa se implementó, 
el proceso de análisis de sintaxis 
usando la herramienta PLY yacc.

Este archivo contiene el Parser 
basadas en las reglas gramaticales 
previamente definidas.

@author: Carmina López Palacios
"""

import ply.yacc as yacc
from lexer import tokens
from FuncDirectory import FuncDirectory

# Define precedence and associativity
"""precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLICATION', 'DIVISION'),
)"""

# Formal grammar
# Using syntax Backus-Naur Form (BNF)

#--------------#
## <Programa> ##
#--------------#
# 1) Create an instance of Functon Directory
dir_func = FuncDirectory()

def p_program(p):
    '''PROGRAMA : PROGRAM ID PUNTO_1 SEMICOLON DEC_VARS DEC_FUNCS MAIN BODY END'''
    p[0] = p[2], p[5], p[6], p[8] 

# --- Embedded Actions ----
# To initialize the symbol table / Puntos neurálgicos
def p_punto_1(p):
    "PUNTO_1 :"
    # 1) Add new function 'ID'
    # Inside of this method validates if the id func already exists
    print("Añadiendo función")
    dir_func.add_function(p[-1],'NP')
    print("Nombre:", p[-1]) 
    dir_func.set_current_function(p[-1])
    # *BORRAR* Set global_name
    dir_func.set_current_global(p[-1])

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

# --- Embedded Actions ----
# To initialize the variable table
def p_punto_2(p):
    "PUNTO_2 :"
    #2) Create variable table
    dir_func.create_variable_table()

#----------#
## <VARS> ##
#----------#
def p_vars(p):
    '''VARS : VAR PUNTO_2 LISTA_VAR'''
    p[0] = ('VARS', p[3])

# --- Embedded Actions ----
# To initialize the variable table
def p_punto_3(p):
    "PUNTO_3 :"
    # 3) Add the variables to variable table
    # Inside of this method validates if the variable already exists
    var_names = p[-3]
    for var_name in var_names:
        dir_func.add_variable_to_current_func(var_name, p[-1])

# <LISTA_VAR>
def p_lista_var(p):
    '''LISTA_VAR : LISTA_ID COLON TYPE PUNTO_3 SEMICOLON MAS_VAR'''

    # borrar
    print("Variables en 'func':", dir_func.get_current_function_vars())
    p[0] = ('LISTA_VAR', p[1], p[3], p[6])

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
    # Created the lista ID in this form: ['yogurt', 'con', 'carmina']
    p[0] = [p[1]] + (p[2] if p[2] is not None else [])

# <MAS_ID>
def p_mas_id(p):
    '''MAS_ID : COMMA LISTA_ID
              | epsilon'''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = None

#----------#
## <Type> ##
#----------#
def p_type(p):
    '''TYPE : INT
            | FLOAT'''
    p[0] = p[1]

#-----------#
## <FUNCS> ##
#-----------#
def p_funcs(p):
    '''FUNCS : VOID ID PUNTO_4 LEFT_PARENTHESIS PUNTO_5 PARAMETROS RIGHT_PARENTHESIS LEFT_BRACKET VARS_FUNC BODY RIGHT_BRACKET SEMICOLON PUNTO_7'''
    p[0] = ('FUNCS', p[2], p[6], p[9], p[10])
    print("Directorio función")
    dir_func.print_directory()

# --- Embedded Actions ----
# To add new function to DirFunc
def p_punto_4(p):
    "PUNTO_4 :"
    
    # 4) Add new function 'ID'
    # Inside of this method validates if the id func already exists
    print("Añadiendo función")
    dir_func.add_function(p[-1],p[-2])
    print("Nombre:", p[-1]) 
    dir_func.set_current_function(p[-1])   

# --- Embedded Actions ----
# To create a varTable and link it to current Func
def p_punto_5(p):
    "PUNTO_5 :"
    
    #5) Create variable table
    dir_func.create_variable_table()
    

# --- Embedded Actions ----
# Delete var table
def p_punto_7(p):
    "PUNTO_7 :"
    
    #7) Delete variables
    dir_func.delete_variable_table(p[-11])

# <PARAMETROS>
def p_parametros(p):
    '''PARAMETROS : epsilon
                  | DEC_PARAMETROS'''
    if len(p) == 2:
        p[0] = ('PARAMETROS', p[1])
    else:
        p[0] = None

# --- Embedded Actions ----
# To add variables to varTable
def p_punto_6(p):
    "PUNTO_6 :"
    
    # 6) Add variables to var table
    # Inside of this method validates if the variable already exists
    dir_func.add_variable_to_current_func(p[-3], p[-1])
# <DEC_PARAMETROS>
def p_dec_parametros(p):
    '''DEC_PARAMETROS : ID COLON TYPE PUNTO_6 LISTA_PARAMETROS'''
    p[0] = ('DEC_PARAMETROS', p[1], p[3], p[5])

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
                 | PRINT_STMT
    '''
    p[0] = ('STATEMENT', p[1])

#------------#
## <ASSIGN> ##
#------------#
def p_assign(p):
    'ASSIGN : ID EQUAL EXPRESION SEMICOLON'
    p[0] = ('ASSIGN', p[1], p[3])

#----------------#
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
    '''CONDITION : IF LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS BODY ELSE_CONDITION SEMICOLON'''
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
    '''CYCLE : DO BODY WHILE LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS SEMICOLON'''
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

#-----------------#
## <PRINT_STMT>  ##
#----------------#
def p_print_stmt(p):
    '''PRINT_STMT : PRINT LEFT_PARENTHESIS PARAMETROS_PRINT RIGHT_PARENTHESIS SEMICOLON'''
    p[0] = ('PRINT_STMT', p[3])

# <PARAMETROS_PRINT>
def p_parametros_print(p):
    '''PARAMETROS_PRINT : CTE_STRING MAS_PRINT
                        | EXPRESION MAS_PRINT'''
    p[0] = ('PARAMETROS_PRINT', p[1], p[2])                    

# <MAS_PRINT>
def p_mas_print(p):
    '''MAS_PRINT : epsilon
                 | COMMA PARAMETROS_PRINT'''
    if len(p) > 2:
        p[0] = ('MAS_PRINT', p[2])
    else:
        p[0] = None

# Epsilon
def p_epsilon(p):
    'epsilon :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Error sintáxis")

# Define el parser
parser = yacc.yacc()

# Función para analizar la entrada
def parse_input(input_data):
    return parser.parse(input_data)

# Archivo de entrada
input_file = 'test/test3.txt'

# Abre el archivo de entrada y lee su contenido
with open(input_file, 'r') as file:
    data = file.read()

# Analiza la entrada
parsed_result = parse_input(data)

print(parsed_result)
print("Directorio sin función")
dir_func.print_directory()