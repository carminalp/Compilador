class SemanticCube:
    def __init__(self):
        # Initialize the semantic cube (Hashmap) with definitions for type operations
        self.semanticDictionary = {
            ('INT', 'INT', 'PLUS'): 'INT',
            ('INT', 'FLOAT', 'PLUS'): 'FLOAT',
            ('FLOAT', 'INT', 'PLUS'): 'FLOAT',
            ('FLOAT', 'FLOAT', 'PLUS'): 'FLOAT',
            ('INT', 'INT', 'MINUS'): 'INT',
            ('INT', 'FLOAT', 'MINUS'): 'FLOAT',
            ('FLOAT', 'INT', 'MINUS'): 'FLOAT',
            ('FLOAT', 'FLOAT', 'MINUS'): 'FLOAT',
            ('INT', 'INT', 'MULTIPLICATION'): 'INT',
            ('INT', 'FLOAT', 'MULTIPLICATION'): 'FLOAT',
            ('FLOAT', 'INT', 'MULTIPLICATION'): 'FLOAT',
            ('FLOAT', 'FLOAT', 'MULTIPLICATION'): 'FLOAT',
            ('INT', 'INT', 'DIVISION'): 'FLOAT',
            ('INT', 'FLOAT', 'DIVISION'): 'FLOAT',
            ('FLOAT', 'INT', 'DIVISION'): 'FLOAT',
            ('FLOAT', 'FLOAT', 'DIVISION'): 'FLOAT',
            ('INT', 'INT', 'EQUAL'): 'BOOL',
            ('INT', 'FLOAT', 'EQUAL'): 'BOOL',
            ('FLOAT', 'INT', 'EQUAL'): 'BOOL',
            ('FLOAT', 'FLOAT', 'EQUAL'): 'BOOL',
            ('INT', 'INT', 'NOT_EQUAL'): 'BOOL',
            ('INT', 'FLOAT', 'NOT_EQUAL'): 'BOOL',
            ('FLOAT', 'INT', 'NOT_EQUAL'): 'BOOL',
            ('FLOAT', 'FLOAT', 'NOT_EQUAL'): 'BOOL',
            ('INT', 'INT', 'LESS_THAN'): 'BOOL',
            ('INT', 'FLOAT', 'LESS_THAN'): 'BOOL',
            ('FLOAT', 'INT', 'LESS_THAN'): 'BOOL',
            ('FLOAT', 'FLOAT', 'LESS_THAN'): 'BOOL',
            ('INT', 'INT', 'GREATER_THAN'): 'BOOL',
            ('INT', 'FLOAT', 'GREATER_THAN'): 'BOOL',
            ('FLOAT', 'INT', 'GREATER_THAN'): 'BOOL',
            ('FLOAT', 'FLOAT', 'GREATER_THAN'): 'BOOL',
            ('INT', 'INT', 'LESS_EQUAL'): 'BOOL',
            ('INT', 'FLOAT', 'LESS_EQUAL'): 'BOOL',
            ('FLOAT', 'INT', 'LESS_EQUAL'): 'BOOL',
            ('FLOAT', 'FLOAT', 'LESS_EQUAL'): 'BOOL',
            ('INT', 'INT', 'GREATER_EQUAL'): 'BOOL',
            ('INT', 'FLOAT', 'GREATER_EQUAL'): 'BOOL',
            ('FLOAT', 'INT', 'GREATER_EQUAL'): 'BOOL',
            ('FLOAT', 'FLOAT', 'GREATER_EQUAL'): 'BOOL',
        }
    
    """
    get the type of the result

    Parameters:
    # op1_type is a string with the type name
    # op2_type is a string with the type name 
    # operator is a string with the name of the operator

    Return the resulting type of the operation
    """
    def get_result_type(self, op1_type, op2_type, operator):
        key = (op1_type, op2_type, operator)
        if key in self.semanticDictionary:
            return self.semanticDictionary[key]
        else:
            return 'Error: operación incorrecta'

# Usage of the class
semantic_cube = SemanticCube()
result_type = semantic_cube.get_result_type('INT', 'FLOAT', 'PLUS')
print(f"The resulting type of INT and FLOAT with operator PLUS is: {result_type}")
