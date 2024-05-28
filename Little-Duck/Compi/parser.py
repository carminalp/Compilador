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
from Compi.lexer import tokens
from Compi.Directories.FuncDirectory import FuncDirectory
from Compi.IntermediateCodeActions import *
from Compi.Directories.cteDirectory import ConstantDirectory

# Initialization of stack 
PilaO = [] # Pila Operandos
POper = [] # Pila Operadores
Quad = [] # Fila cuadroplos
PJumps = []
PilaParametros = []

# Create an instance of cte Directory
const_directory = ConstantDirectory()

# Formal grammar
# Using syntax Backus-Naur Form (BNF)
#--------------------------------------------------------------------------------------------------------#
##                                     <Programa>                                                       ##
#--------------------------------------------------------------------------------------------------------#
# 1) Create an instance of Functon Directory
dir_func = FuncDirectory()

def p_program(p):
    '''PROGRAMA : PROGRAM ID PUNTO_1 SEMICOLON DEC_VARS DEC_FUNCS MAIN PUNTO_CURRENT BODY END'''
    p[0] = p[2], p[5], p[6], p[8] 

#-------------------------
# ---- NEURALGIC POINT ----
# To initialize the symbol table / Puntos neurálgicos
def p_punto_1(p):
    "PUNTO_1 :"
    # 1) Add new function 'ID'
    # Inside of this method validates if the id func already exists
    dir_func.add_function(p[-1],'NP')
    dir_func.set_current_function(p[-1])
    dir_func.set_current_global(p[-1])

#-------------------------
# ---- NEURALGIC POINT ----
# Set current function to global
def p_punto_current(p):
    "PUNTO_CURRENT :"
    global global_name

    global_name = dir_func.get_current_global()
    dir_func.set_current_function(global_name)
    

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

#-------------------------
# ---- NEURALGIC POINT ----
# To initialize the variable table
def p_punto_2(p):
    "PUNTO_2 :"
    #2) Create variable table
    dir_func.create_variable_table()

#--------------------------------------------------------------------------------------------------------#
##                                        <VARS>                                                        ##
#--------------------------------------------------------------------------------------------------------#
def p_vars(p):
    '''VARS : VAR PUNTO_2 LISTA_VAR'''
    p[0] = ('VARS', p[3])

#-------------------------
# ---- NEURALGIC POINT ----
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
    # print("Variables en 'func':", dir_func.get_current_function_vars())
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

#--------------------------------------------------------------------------------------------------------#
##                                           <Type>                                                      ##
#--------------------------------------------------------------------------------------------------------#
def p_type(p):
    '''TYPE : INT
            | FLOAT'''
    p[0] = p[1]

#--------------------------------------------------------------------------------------------------------#
##                                          <FUNCS>                                                      ##
#--------------------------------------------------------------------------------------------------------#
def p_funcs(p):
    '''FUNCS : VOID ID PUNTO_4 LEFT_PARENTHESIS PUNTO_5 PARAMETROS RIGHT_PARENTHESIS LEFT_BRACKET VARS_FUNC BODY RIGHT_BRACKET SEMICOLON PUNTO_7'''
    p[0] = ('FUNCS', p[2], p[6], p[9], p[10])

#-------------------------
# ---- NEURALGIC POINT ----
# 4) To add new function to DirFunc
def p_punto_4(p):
    "PUNTO_4 :"
    # 4) Add new function 'ID'
    # Inside of this method validates if the id func already exists
    dir_func.add_function(p[-1],p[-2]) 
    dir_func.set_current_function(p[-1])   

#-------------------------
# ---- NEURALGIC POINT ----
# 5) To create a varTable and link it to current Func
def p_punto_5(p):
    "PUNTO_5 :"
    dir_func.create_variable_table()

#-------------------------
# ---- NEURALGIC POINT ----
# 7) Delete var table and clear PilaO, POper and Quad
def p_punto_7(p):
    "PUNTO_7 :"
    dir_func.delete_variable_table(p[-11])

# <PARAMETROS>
def p_parametros(p):
    '''PARAMETROS : epsilon
                  | DEC_PARAMETROS'''
    if len(p) == 2:
        p[0] = ('PARAMETROS', p[1])
    else:
        p[0] = None

#-------------------------
# ---- NEURALGIC POINT ----
# To add variables to varTable
def p_punto_6(p):
    "PUNTO_6 :"
    # 6) Add variables to var table
    # Inside of this method validates if the variable already exists
    dir_func.add_variable_to_current_func(p[-3], p[-1])
    dir_func.add_params_to_current_func(p[-1])

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
 
#--------------------------------------------------------------------------------------------------------#
##                                            <BODY>                                                    ##
#--------------------------------------------------------------------------------------------------------#
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

#--------------------------------------------------------------------------------------------------------#
##                                          <STATEMENT>                                                  ##
#--------------------------------------------------------------------------------------------------------#
def p_statement(p):
    '''STATEMENT : ASSIGN
                 | CONDITION
                 | CYCLE
                 | F_CALL
                 | PRINT_STMT
    '''
    p[0] = ('STATEMENT', p[1])

#--------------------------------------------------------------------------------------------------------#
##                                         <ASSIGN>                                                     ##
#--------------------------------------------------------------------------------------------------------#
def p_assign(p):
    'ASSIGN : ID PUNTO_8 EQUAL PUNTO_9 EXPRESION PUNTO_18 SEMICOLON'
    p[0] = ('ASSIGN', p[1], p[5])


# -------------------------
# ---- NEURALGIC POINT ----
# save id to be assign  
def p_punto_8(p):
    "PUNTO_8 :"
    var_name = p[-1]
    var_address = dir_func.get_current_address(var_name)
    var_type = dir_func.get_current_type(var_name)

    PilaO.append((var_address, var_type))

# -------------------------
# ---- NEURALGIC POINT ----
# save operator  
def p_punto_9(p):
    "PUNTO_9 :"
    POper.append(p[-1])

# -------------------------
# ---- NEURALGIC POINT ----
# assign = expresion 
def p_punto_18(p):
    "PUNTO_18 :"
    if POper[-1] == '=':
        semantic_assign(PilaO, POper, Quad)

#--------------------------------------------------------------------------------------------------------#
##                                          <EXPRESIÓN>                                                 ##
#--------------------------------------------------------------------------------------------------------#
def p_expresion(p):
    '''EXPRESION : EXP MAS_EXPRESIONES'''
    p[0] = (p[1], p[2])
    

# <MAS_EXPRESIONES>
def p_mas_expresiones(p):
    '''MAS_EXPRESIONES : OPERADORES PUNTO_13 EXP PUNTO_13_1 
                       | epsilon'''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else: 
        p[0] = None

# -------------------------
# ---- NEURALGIC POINT ----
# 13) save operator  
def p_punto_13(p):
    "PUNTO_13 :"
    POper.append(p[-1])

# -------------------------
# ---- NEURALGIC POINT ----
# 13.1) See if there's a > or < or != at Poper
def p_punto_13_1(p):
    "PUNTO_13_1 :"
    if POper[-1] == '>' or POper[-1]  == '<' or POper[-1]  == '!=':
        semantic_expressions(PilaO, POper, Quad )


# <OPERADORES>
def p_operadores(p):
    '''OPERADORES : GREATER_THAN
                  | LESS_THAN
                  | NOT_EQUAL'''
    p[0] = p[1]

#--------------------------------------------------------------------------------------------------------#
##                                           <EXP>                                                      ##
#--------------------------------------------------------------------------------------------------------#
def p_exp(p):
    '''EXP : TERMINO PUNTO_14 MAS_EXP'''
    p[0] = p[1], p[3]

# -------------------------
# ---- NEURALGIC POINT ----
# See if there's a + or -  at Poper
def p_punto_14(p):
    "PUNTO_14 :"
    if POper: # See if poper isn't empty
        if POper[-1] == '+' or POper[-1]  == '-':
            semantic_operations(PilaO, POper, Quad )

# <MAS_EXP>
def p_mas_exp(p):
    '''MAS_EXP : OPERADORES_EXP PUNTO_12 EXP
               | epsilon'''
    if len(p) > 2:
        p[0] = p[1], p[3]
    else:
        p[0] = None

# -------------------------
# ---- NEURALGIC POINT ----
# save + / -  
def p_punto_12(p):
    "PUNTO_12 :"
    POper.append(p[-1])

# <OPERADORES_EXP>
def p_operadores_exp(p):
    '''OPERADORES_EXP : PLUS
                      | MINUS'''
    p[0] = p[1]

#--------------------------------------------------------------------------------------------------------#
## <TERMINO> ##
#--------------------------------------------------------------------------------------------------------#
def p_termino(p):
    '''TERMINO : FACTOR PUNTO_15 MAS_TERMINO'''
    p[0] = (p[1], p[3])

# -------------------------
# ---- NEURALGIC POINT ----
# See if there's a * or / at Poper
def p_punto_15(p):
    "PUNTO_15 :"
    if POper: # See if poper isn't empty
        if POper[-1] == '*' or POper[-1]  == '/':
            semantic_operations(PilaO, POper, Quad )

# <MAS_TERMINO>
def p_mas_termino(p):
    '''MAS_TERMINO : epsilon
                   | OPERADORES_TER PUNTO_11 TERMINO'''
    if len(p) > 2:
        p[0] = (p[1], p[3])
    else:
        p[0] = None

# -------------------------
# ---- NEURALGIC POINT ----
# save operator * or / 
def p_punto_11(p):
    "PUNTO_11 :"
    POper.append(p[-1])

# <OPERADORES_TER>
def p_operadores_ter(p):
    '''OPERADORES_TER : MULTIPLICATION
                      | DIVISION'''
    p[0] = p[1]

#--------------------------------------------------------------------------------------------------------#
## <FACTOR> ##
#--------------------------------------------------------------------------------------------------------#
def p_factor(p):
    '''FACTOR : OPERADORES_FACTOR ID_CTE
              | LEFT_PARENTHESIS PUNTO_16 EXPRESION RIGHT_PARENTHESIS PUNTO_17'''
    if len(p) >= 4:
        p[0] = p[3]
    else:
        p[0] = p[1], p[2]

# -------------------------
# ---- NEURALGIC POINT ----
# save (
def p_punto_16(p):
    "PUNTO_16 :"
    POper.append(p[-1])

# -------------------------
# ---- NEURALGIC POINT ----
# 17) pop (
def p_punto_17(p):
    "PUNTO_17 :"
    POper.pop()

# <ID_CTE>
def p_id_cte(p):
    '''ID_CTE : ID PUNTO_10
              | CTE PUNTO_CTE PUNTO_19'''
    p[0] = p[1]

# -------------------------
# ---- NEURALGIC POINT ----
# add CTE to directory
def p_punto_cte(p):
    "PUNTO_CTE :"
    const_type = const_directory.determine_const_type(p[-1])
    const_directory.add_constant(p[-1], const_type)

# -------------------------
# ---- NEURALGIC POINT ----
# 10) save id
def p_punto_10(p):
    "PUNTO_10 :"
    var_name = p[-1]
    var_address = dir_func.get_current_address(p[-1])
    var_type = dir_func.get_current_type(var_name)
    PilaO.append((var_address, var_type))

# -------------------------
# ---- NEURALGIC POINT ----
# 19) save cte
def p_punto_19(p):
    "PUNTO_19 :"
    cte_address = const_directory.get_constant(p[-2])['address']
    cte_type = const_directory.get_constant(p[-2])['type']
    PilaO.append((cte_address, cte_type))

# <OPERADORES_FACTOR>
def p_operadores_factor(p):
    '''OPERADORES_FACTOR : PLUS
                         | MINUS
                         | epsilon'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = None

#--------------------------------------------------------------------------------------------------------#
## <CTE> ##
#--------------------------------------------------------------------------------------------------------#
def p_cte(p):
    '''CTE : CTE_INT
           | CTE_FLOAT'''
    p[0] = p[1]
    

#--------------------------------------------------------------------------------------------------------#
## <CONDITION> ##
#--------------------------------------------------------------------------------------------------------#
def p_condition(p):
    '''CONDITION : IF LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS PUNTO_24 BODY ELSE_CONDITION SEMICOLON PUNTO_25'''
    p[0] = ('CONDITION', p[3], p[6], p[7])

# -------------------------
# ---- NEURALGIC POINT ----
# 24) GotoF 
def p_punto_24(p):
    "PUNTO_24 :"
    semantic_condition_if(PilaO, POper, Quad , PJumps)

# -------------------------
# ---- NEURALGIC POINT ----
# 25) Fill Quadruples GotoF
def p_punto_25(p):
    "PUNTO_25 :"
    if p[-2] == None:
        fill_GotoFF(Quad, PJumps)

# -------------------------
# ---- NEURALGIC POINT ----
# 26) Goto 
def p_punto_26(p):
    "PUNTO_26 :"
    semantic_condition_else(PilaO, POper, Quad , PJumps)  

# <ELSE_CONDITION>
def p_else(p):
    '''ELSE_CONDITION : epsilon
                      | ELSE PUNTO_26 BODY PUNTO_27'''
    if len(p) >= 3:
        p[0] = p[3]
    else:
        p[0] = None
# -------------------------
# ---- NEURALGIC POINT ----
# 27) Fill Quadruples Goto
def p_punto_27(p):
    "PUNTO_27 :"
    fill_GotoF(Quad, PJumps)
    #fill_GotoFF(Quad, PJumps)

#--------------------------------------------------------------------------------------------------------#
## <CYCLE> ##
#--------------------------------------------------------------------------------------------------------#
def p_cycle(p):
    '''CYCLE : DO PUNTO_28 BODY WHILE LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS SEMICOLON PUNTO_29'''
    p[0] = ('CYCLE', p[2], p[5])

# -------------------------
# ---- NEURALGIC POINT ----
# 28) Add 'migajita de pan'
def p_punto_28(p):
    "PUNTO_28 :"
    semantic_cycle_do(PJumps)

# -------------------------
# ---- NEURALGIC POINT ----
# 29) go to V
def p_punto_29(p):
    "PUNTO_29 :"
    semantic_cycle(PilaO, Quad, PJumps)

#--------------------------------------------------------------------------------------------------------#
## <F_CALL> ##
#--------------------------------------------------------------------------------------------------------#
def p_f_call(p):
    '''F_CALL : ID LEFT_PARENTHESIS EXPRESIONES RIGHT_PARENTHESIS SEMICOLON'''
    p[0] = ('F_CALL', p[1], p[3])

# <EXPRESIONES>
def p_expresiones(p):
    '''EXPRESIONES : EXPRESIONES_F
                   | epsilon'''
    if len(p) == 2:
        p[0] = p[1]
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
        p[0] = p[2]
    else:
        p[0] = None

#--------------------------------------------------------------------------------------------------------#
##                                          <PRINT_STMT>                                                 ##
#--------------------------------------------------------------------------------------------------------#
def p_print_stmt(p):
    '''PRINT_STMT : PRINT PUNTO_20 LEFT_PARENTHESIS PARAMETROS_PRINT RIGHT_PARENTHESIS SEMICOLON'''
    p[0] = ('PRINT_STMT', p[4])

# -------------------------
# ---- NEURALGIC POINT ----
# 20) save 'print'  
def p_punto_20(p):
    "PUNTO_20 :"
    POper.append(p[-1])

# <PARAMETROS_PRINT>
def p_parametros_print(p):
    '''PARAMETROS_PRINT : CTE_STRING PUNTO_CTE_STR PUNTO_21 PUNTO_22 MAS_PRINT
                        | EXPRESION PUNTO_22 MAS_PRINT'''
    p[0] = (p[1], p[2])                    

# -------------------------
# ---- NEURALGIC POINT ----
# add CTE_STRING to directory
def p_punto_cte_str(p):
    "PUNTO_CTE_STR :"
    const_type = const_directory.determine_const_type(p[-1])
    const_directory.add_constant(p[-1], const_type)

# -------------------------
# ---- NEURALGIC POINT ----
# 21) push cte string
def p_punto_21(p):
    "PUNTO_21 :"
    cte_address = const_directory.get_constant(p[-2])['address']
    cte_type = const_directory.get_constant(p[-2])['type']
    PilaO.append((cte_address, cte_type))

# -------------------------
# ---- NEURALGIC POINT ----
# 22) save 'print'
def p_punto_22(p):
    "PUNTO_22 :"
    if POper[-1] == 'print':
        semantic_print(PilaO, POper, Quad )


# <MAS_PRINT>
def p_mas_print(p):
    '''MAS_PRINT : epsilon
                 | COMMA PUNTO_23 PARAMETROS_PRINT'''
    if len(p) > 2:
        p[0] = ('MAS_PRINT', p[2])
    else:
        p[0] = None


# -------------------------
# ---- NEURALGIC POINT ----
# 23) save 'print'  
def p_punto_23(p):
    "PUNTO_23 :"
    POper.append('print')

#--------------------------------------------------------------------------------------------------------#
##                                          <EPSILON>                                                   ##
#-------------------------------------------------------------------------------------------------------#
def p_epsilon(p):
    'epsilon :'
    pass

# Error rule for syntax errors
def p_error(p):
    raise ValueError("Syntax Error")

# Define el parser
parser = yacc.yacc()

# Función para analizar la entrada y devolver el directorio de constantes y los cuádruplos
def parse_input(input_data):
    global PilaO, POper, Quad, PJumps, PilaParametros, const_directory, dir_func

    # Resetear las estructuras globales
    PilaO = [] 
    POper = [] 
    Quad = [] 
    PJumps = []
    PilaParametros = []
    Const_directory = ConstantDirectory()
    dir_func = FuncDirectory()
    parser.parse(input_data)
    return const_directory.get_all_constants(), Quad

# Función de compilación que se integrará con el IDE
def compile_code(source_code):
    cte_directory, quadruples = parse_input(source_code)
    return cte_directory, quadruples