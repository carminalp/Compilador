from VM.Memory import Memory

"""
    Execute a list of quadruples and update memory accordingly.

    Parameters:
    - quadruples: A list of Quadruple objects to execute.
    - memory: The Memory object to update based on the quadruples.
"""
def execute_quadruples(quadruples, memory):
    
    output = []
    current_ip = 0

    while current_ip < len(quadruples):
        quad = quadruples[current_ip]
        operator, left_operand, right_operand, result = quad.operator, quad.left_operand, quad.right_operand, quad.result
        try:
            if operator == 0:  # Assign
                value = memory.get_value(left_operand)
                memory.set_value(result, value)
            elif operator == 1:  # Add
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value + right_value)
            elif operator == 2:  # Subtract
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value - right_value)
            elif operator == 3:  # Multiply
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value * right_value)
            elif operator == 4:  # Divide
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value / right_value)
            elif operator == 5:  # Not equal
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value != right_value)
            elif operator == 6:  # Less than
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value < right_value)
            elif operator == 7:  # Greater than
                left_value = memory.get_value(left_operand)
                right_value = memory.get_value(right_operand)
                memory.set_value(result, left_value > right_value)
            elif operator == 8:  # Goto
                current_ip = result - 1
            elif operator == 9:  # Goto if false
                condition_value = memory.get_value(left_operand)
                if condition_value == False:
                    current_ip = result - 1
            elif operator == 10:  # Goto if true
                condition_value = memory.get_value(left_operand)
                if condition_value == True:
                    current_ip = result - 1
            elif operator == 11:  # Print
                value = memory.get_value(result)
                if isinstance(value, str):
                    value = value.strip('"')
                output.append(f"{value}")
        except KeyError as e:
            print(f"Error executing quadruple")

        current_ip += 1

    return output
