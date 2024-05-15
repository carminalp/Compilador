class VariableTable:
    # Constructor 
    def __init__(self):
        # Initializes the dictionary 
        self.variableTable = {}

    """
    Adds a new variable to the table

    Parameters:
    # name is a string with the variable name
    # var_type is a string with the type (int|float)
    # value is an (int|float) and it's the assigned value (defaults to None)

    """
    def add_variable(self, name, var_type, value=None):
        # Search if the name it already exist
        if name in self.variableTable:
            raise ValueError("Múltiple declaración de variable")
        self.variableTable[name] = {'type': var_type, 'value': value}

    """
    Get the variable with the key = name

    Parameters:
    # name is a string with the variable name to search

    returns the dictonary that contains the type and value of the variable, 
    or None if the variable is not found.
    """
    def get_variable(self, name):
        return self.variableTable.get(name, None)
