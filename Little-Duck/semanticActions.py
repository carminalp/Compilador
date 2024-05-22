from SemanticCube import SemanticCube
from Quadruple import Quadruple

semantic_cube = SemanticCube()
cont = 0

"""
    If any operand were a temporal space, return it to AVAIL

    Parameters:
    # operand is a variable with the operand
"""
def return_to_avail_if_temporal(operand):
    if isinstance(operand, int) and operand >= 7000 and operand <= 4001:
        AVAIL.append(operand)

"""
    Adds a new quadruple

    Parameters:
    # PilaO is a stack with the variables and types (int|float)
    # POper is a queue with the operator's 
    # Quad is the Quadruple 
"""
def semantic_operations(PilaO, POper, Quad, AVAIL):
    global cont

    # Pop of the operator, right and left operands
    right_operand, right_type = PilaO.pop()
    left_operand, left_type = PilaO.pop()
    operator = POper.pop()
    
    # Evaluate the result type with the semantic cube
    result_type = semantic_cube.get_result_type(left_type, right_type, operator)
    
    if result_type != ValueError:
        # Take the next temporary result
        result = next(AVAIL)
        quad = Quadruple(operator, left_operand, right_operand, result)
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
    - AVAIL: Iterator for available temporals
"""
def semantic_assign(PilaO, POper, Quad, AVAIL):
    global cont

    # Pop of the operator, right and left operands
    right_operand, right_type = PilaO.pop()
    left_operand, left_type = PilaO.pop()
    operator = POper.pop()
    
    # Evaluate the result type with the semantic cube
    result_type = semantic_cube.get_result_type(left_type, right_type, operator)
    
    if result_type != ValueError:
        # Take the next temporary result
        quad = Quadruple(operator, right_operand , None , left_operand)
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
    - AVAIL: Iterator for available temporals
"""
def semantic_print(PilaO, POper, Quad, AVAIL): 
    global cont

    # Pop of the operator, right and left operands
    cte_string, cte_type = PilaO.pop()
    operator = POper.pop()
    
    quad = Quadruple(operator, None , None , cte_string)
    Quad.append(quad)
    cont += 1

"""
    Handle semantic expressions.

    Parameters:
    - PilaO: Stack with operands and their types
    - POper: Stack with operators
    - Quad: List of quadruples
    - AVAIL: Iterator for available temporals
"""
def semantic_expressions(PilaO, POper, Quad, AVAIL):
    global cont

    # Pop of the operator, right and left operands
    right_operand, right_type = PilaO.pop()
    left_operand, left_type = PilaO.pop()
    operator = POper.pop()

    # Evaluate the result type with the semantic cube
    result_type = semantic_cube.get_result_type(left_type, right_type, operator)

    if result_type != ValueError:
        result = next(AVAIL)
        # Take the next temporary result
        quad = Quadruple(operator, left_operand, right_operand, result)
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
    - AVAIL: Iterator for available temporals
    - PJumps: Stack for jumps
"""
def semantic_condition_if(PilaO, POper, Quad, AVAIL, PJumps):
    global cont

    exp, exp_type = PilaO.pop()

    if (exp_type != 'bool'):
        raise ValueError("Type mismatch error")
    else: 
        result = exp
        quad = Quadruple('GotoF', result, None, None)
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
    - AVAIL: Iterator for available temporals
    - PJumps: Stack for jumps
"""
def semantic_condition_else(PilaO, POper, Quad, AVAIL, PJumps):
    global cont
    quad = Quadruple('Goto', None, None, None)
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
        raise ValueError("Type mismatch error")
    else: 
        result = condition
        returnTo = PJumps.pop()
        quad = Quadruple('GotoV', result, None, returnTo)
        Quad.append(quad)
        cont += 1

"""
    Search and store parameters(address and type), 
    either variables or constants.

    Parameters:
    - const_directory: Constant directory
    - dir_func: Function directory
    - parameter: The parameter to search for
    - PParametros: Stack for parameters
"""
def search_parameter(const_directory, dir_func, parameter, PParametros):
    try:
        variable_address = dir_func.get_current_address(parameter)
        variable_type = dir_func.get_current_type(parameter)
        PParametros.append((variable_address, variable_type))
    except ValueError:
        cte_address = const_directory.get_constant(parameter)['address']
        cte_type = const_directory.get_constant(parameter)['type']
        PParametros.append((cte_address, cte_type))

"""
    Verify that the parameters on the stack match the function parameters in the directory.

    Parameters:
    - PilaParametros: Stack with the parameters to verify
    - dirFunc: Function directory
    - func_id: The identifier of the function being called
"""
def verify_parameters(PilaParametros, dirFunc, Quad, name):
    global cont

    expected_params = dirFunc.get_parameters(name)

    if len(PilaParametros) != len(expected_params):
        raise ValueError("Parameter count mismatch")

    for i in range(len(expected_params)):
        param = PilaParametros[i]
        expected_type = expected_params[i]

        if param[1] != expected_type:
            raise ValueError(f"Type mismatch for parameter {i+1}: expected {expected_type}, got {param_type}")

        quad = Quadruple("param", param[0], None, None)
        Quad.append(quad)
        cont += 1

    quad = Quadruple("F_CALL", name, len(expected_params), None)
    Quad.append(quad)
    cont += 1

def goto_call_function(dir_func, idFunc, Quad, PJumps):
    global cont

    indexQuad = dir_func.get_start_quad(idFunc)
    
    quad = Quadruple("Goto", None, None, indexQuad)
    Quad.append(quad)
    PJumps.append(cont)
    cont += 1

def goto_function(Quad, PJumps, dir_func):
    global cont

    quad = Quadruple("Goto", None, None, None)
    Quad.append(quad)
    dir_func.set_goto_quad(cont)
    cont += 1

"""
    Complete the Goto quadruple of function.

    Parameters:
    - Quad: List of quadruples
    - PJumps: Stack for jumps
"""
def fill_Goto_Function(Quad, PJumps, dir_func, name):
    global cont
    goto_body = dir_func.get_goto_quad(name)
    Quad[goto_body].result = cont