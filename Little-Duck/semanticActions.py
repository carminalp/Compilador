from SemanticCube import SemanticCube
from Quadruple import Quadruple

semantic_cube = SemanticCube()
"""
    If any operand were a temporal space, return it to AVAIL

    Parameters:
    # operand is a variable with the operand
"""
def return_to_avail_if_temporal(operand):
    if isinstance(operand, int) and operand >= 3200 and operand <= 2302:
        AVAIL.append(operand)

"""
    Adds a new quadruple

    Parameters:
    # PilaO is a stack with the variables and types (int|float)
    # POper is a queue with the operator's 
    # Quad is the Quadruple 
"""
def semanticOperations(PilaO, POper, Quad, AVAIL):
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
        PilaO.append((result, result_type))

        return_to_avail_if_temporal(right_operand)
        return_to_avail_if_temporal(left_operand)

    else:
        raise ValueError("Type mismatch error")

def semanticAssign(PilaO, POper, Quad, AVAIL):
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

        return_to_avail_if_temporal(right_operand)
        return_to_avail_if_temporal(left_operand)

    else:
        raise ValueError("Type mismatch error")

def semanticPrint(PilaO, POper, Quad, AVAIL): 
    # Pop of the operator, right and left operands
    cte_string, cte_type = PilaO.pop()
    operator = POper.pop()
    
    quad = Quadruple(operator, None , None , cte_string)
    Quad.append(quad)
        