class SemanticCube:
    def __init__(self):
        # Initialize the semantic cube (Hashmap) with definitions for type operations
        self.semanticDictionary = {
            ('int', 'int', '='): 'int',
            ('int', 'float', '='): 'float',
            ('float', 'int', '='): 'float',
            ('float', 'float', '='): 'float',
            ('int', 'int', '+'): 'int',
            ('int', 'float', '+'): 'float',
            ('float', 'int', '+'): 'float',
            ('float', 'float', '+'): 'float',
            ('int', 'int', '-'): 'int',
            ('int', 'float', '-'): 'float',
            ('float', 'int', '-'): 'float',
            ('float', 'float', '-'): 'float',
            ('int', 'int', '*'): 'int',
            ('int', 'float', '*'): 'float',
            ('float', 'int', '*'): 'float',
            ('float', 'float', '*'): 'float',
            ('int', 'int', '/'): 'float',
            ('int', 'float', '/'): 'float',
            ('float', 'int', '/'): 'float',
            ('float', 'float', '/'): 'float',
            ('int', 'int', '=='): 'bool',
            ('int', 'float', '=='): 'bool',
            ('float', 'int', '=='): 'bool',
            ('float', 'float', '=='): 'bool',
            ('int', 'int', '!='): 'bool',
            ('int', 'float', '!='): 'bool',
            ('float', 'int', '!='): 'bool',
            ('float', 'float', '!='): 'bool',
            ('int', 'int', '<'): 'bool',
            ('int', 'float', '<'): 'bool',
            ('float', 'int', '<'): 'bool',
            ('float', 'float', '<'): 'bool',
            ('int', 'int', '>'): 'bool',
            ('int', 'float', '>'): 'bool',
            ('float', 'int', '>'): 'bool',
            ('float', 'float', '>'): 'bool',
            ('int', 'int', '<='): 'bool',
            ('int', 'float', '<='): 'bool',
            ('float', 'int', '<='): 'bool',
            ('float', 'float', '<='): 'bool',
            ('int', 'int', '>='): 'bool',
            ('int', 'float', '>='): 'bool',
            ('float', 'int', '>='): 'bool',
            ('float', 'float', '>='): 'bool',
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
             raise ValueError('Error: operación incorrecta')
