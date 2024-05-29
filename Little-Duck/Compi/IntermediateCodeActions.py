from Compi.SemanticCube import SemanticCube
from Compi.Quadruple import Quadruple

semantic_cube = SemanticCube()
cont = 0

# Memory address temp
AVAIL_INT = iter(range(4001,5000)) # set of Temporal spaces 
AVAIL_FLOAT = iter(range(5001,6000)) # set of float Temporal spaces 
AVAIL_BOOL= iter(range(6001,7000)) # set of Bool Temporal spaces 

operator_index = {
    '=': 0,
    '+': 1,
    '-': 2,
    '*': 3,
    '/': 4,
    '!=': 5,
    '<': 6,
    '>': 7,
    'Goto': 8,
    'GotoF': 9, 
    'GotoV': 10,
    'print': 11
}

"""
    If any operand were a temporal space, return it to AVAIL

    Parameters:
    # operand is a variable with the operand
"""
def return_to_avail_if_temporal(operand):
    if isinstance(operand, int):
        if 4001 <= operand < 5000:
            global AVAIL_INT
            AVAIL_INT = iter([operand] + list(AVAIL_INT))
        elif 5001 <= operand < 6000:
            global AVAIL_FLOAT
            AVAIL_FLOAT = iter([operand] + list(AVAIL_FLOAT))
        elif 6001 <= operand < 7000:
            global AVAIL_BOOL
            AVAIL_BOOL = iter([operand] + list(AVAIL_BOOL))

"""
    Get the next available temporal space based on the result type

    Parameters:
    - result_type: Type of the result (int, float, bool)
"""
def get_next_avail(result_type):
    if result_type == 'int':
        return next(AVAIL_INT)
    elif result_type == 'float':
        return next(AVAIL_FLOAT)
    elif result_type == 'bool':
        return next(AVAIL_BOOL)

"""
    Adds a new quadruple

    Parameters:
    # PilaO is a stack with the variables and types (int|float)
    # POper is a queue with the operator's 
    # Quad is the Quadruple 
"""
def semantic_operations(PilaO, POper, Quad):
    global cont

    # Pop of the operator, right and left operands
    right_operand, right_type = PilaO.pop()
    left_operand, left_type = PilaO.pop()
    operator = POper.pop()
    
    # Evaluate the result type with the semantic cube
    result_type = semantic_cube.get_result_type(left_type, right_type, operator)
    
    if result_type != ValueError:
        # Take the next temporary result
        result = get_next_avail(result_type)
        quad = Quadruple(operator_index[operator], left_operand, right_operand, result)
        Quad.append(quad)
        cont += 1
        PilaO.append((result, result_type))

        return_to_avail_if_temporal(right_operand)
        return_to_avail_if_temporal(left_operand)

"""
    Handle assignment operations.

    Parameters:
    - PilaO: Stack with operands and their types
    - POper: Stack with operators
    - Quad: List of quadruples
"""
def semantic_assign(PilaO, POper, Quad):
    global cont

    # Pop of the operator, right and left operands
    right_operand, right_type = PilaO.pop()
    left_operand, left_type = PilaO.pop()
    operator = POper.pop()
    
    # Evaluate the result type with the semantic cube
    result_type = semantic_cube.get_result_type(left_type, right_type, operator)
    
    if result_type != ValueError:
        quad = Quadruple(operator_index[operator], right_operand , -1 , left_operand)
        Quad.append(quad)
        cont += 1

        return_to_avail_if_temporal(right_operand)
        return_to_avail_if_temporal(left_operand)

    else:
        raise ValueError("Type mismatch error")

"""
    Handle print operations.

    Parameters:
    - PilaO: Stack with operands and their types
    - POper: Stack with operators
    - Quad: List of quadruples
"""
def semantic_print(PilaO, POper, Quad): 
    global cont
    # Pop of the operator, right and left operands
    cte_string, cte_type = PilaO.pop()
    operator = POper.pop()
    
    quad = Quadruple(operator_index[operator], -1 , -1 , cte_string)
    Quad.append(quad)
    cont += 1

"""
    Handle semantic expressions.

    Parameters:
    - PilaO: Stack with operands and their types
    - POper: Stack with operators
    - Quad: List of quadruples
"""
def semantic_expressions(PilaO, POper, Quad):
    global cont

    # Pop of the operator, right and left operands
    right_operand, right_type = PilaO.pop()
    left_operand, left_type = PilaO.pop()
    operator = POper.pop()

    # Evaluate the result type with the semantic cube
    result_type = semantic_cube.get_result_type(left_type, right_type, operator)

    if result_type != ValueError:
        result = get_next_avail(result_type)
        # Take the next temporary result
        quad = Quadruple(operator_index[operator], left_operand, right_operand, result)
        Quad.append(quad)
        cont += 1

        PilaO.append((result, result_type))

        return_to_avail_if_temporal(right_operand)
        return_to_avail_if_temporal(left_operand)

    else:
        raise ValueError("Type mismatch error") 

"""
    Handle 'if' conditions semantic.

    Parameters:
    - PilaO: Stack with operands and their types
    - POper: Stack with operators
    - Quad: List of quadruples
    - PJumps: Stack for jumps
"""
def semantic_condition_if(PilaO, POper, Quad, PJumps):
    global cont

    exp, exp_type = PilaO.pop()

    if (exp_type != 'bool'):
        raise ValueError("Type mismatch error")
    else: 
        result = exp
        quad = Quadruple(operator_index['GotoF'], result, -1, None)
        Quad.append(quad)
        PJumps.append(cont)
        cont += 1

"""
    Complete the GotoF quadruple.

    Parameters:
    - Quad: List of quadruples
    - PJumps: Stack for jumps
"""
def fill_GotoFF(Quad, PJumps):
    global cont
    if PJumps:
        end = PJumps.pop()
        Quad[end].result = cont

"""
    Handle 'else' conditions.

    Parameters:
    - PilaO: Stack with operands and their types
    - POper: Stack with operators
    - Quad: List of quadruples
    - PJumps: Stack for jumps
"""
def semantic_condition_else(PilaO, POper, Quad, PJumps):
    global cont
    quad = Quadruple(operator_index['Goto'], -1, -1, None)
    Quad.append(quad)
    cont += 1
    fill_GotoFF(Quad, PJumps)
    PJumps.append(cont-1)

"""
    Complete the Goto quadruple.

    Parameters:
    - Quad: List of quadruples
    - PJumps: Stack for jumps
"""
def fill_GotoF(Quad, PJumps):
    global cont
    if PJumps:
        # PREGUNTAR
        false = PJumps.pop()
        Quad[false].result = cont

"""
    Handle the start of a 'do' cycle.

    Parameters:
    - PJumps: Stack for jumps
"""
def semantic_cycle_do(PJumps):
    PJumps.append(cont)

"""
    Handle the semantic of a cycle.

    Parameters:
    - PilaO: Stack with operands and their types
    - Quad: List of quadruples
    - PJumps: Stack for jumps
"""
def semantic_cycle(PilaO, Quad, PJumps):
    global cont

    condition, condition_type = PilaO.pop()

    if (condition_type != 'bool'):
        raise ValueError("Type mismatch error (it's not bool)")
    else: 
        result = condition
        returnTo = PJumps.pop()
        quad = Quadruple(operator_index['GotoV'], result, -1, returnTo)
        Quad.append(quad)
        cont += 1

def reset_globals():
    global cont, AVAIL_INT, AVAIL_FLOAT, AVAIL_BOOL
    cont = 0
    AVAIL_INT = iter(range(4001, 5000)) 
    AVAIL_FLOAT = iter(range(5001, 6000)) 
    AVAIL_BOOL = iter(range(6001, 7000)) 