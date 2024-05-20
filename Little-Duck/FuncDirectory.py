from VariableTable import VariableTable

class FuncDirectory:
    # Constructor 
    def __init__(self):
        # initializes an empty dictionary to store functions
        self.functions = {}
        # sets the current function to None (because initially there's no active function)
        self.currentFunc = None
        self.globalName = None

    """
    Adds a new function to the directory.

    Parameters:
    # name is a string with the name of the function to be added.

    """
    def add_function(self, name, tipo):
        # Search if the name already exist
        if name in self.functions:
            raise ValueError("Error Semántica: multiple declaración de función")
        # Initialize the function without a variable table
        self.functions[name] = {'tipo': tipo, 'varTab': None}
    
    """
    Sets the current function to the specified function name.

    Parameters:
    # name is a string with the name of the function to be set as current.      
    """
    def set_current_function(self, name):
        # Set de current function name
        self.currentFunc = name

    def set_current_global(self, name):   
        self.globalName = name

    def get_current_global(self):
        return self.globalName

    """
    Creates and link a variable table with the specified function.

    Parameters:
    # func_name is a string with the name of the function to create a variable table for.
    """
    def create_variable_table(self): 
        # Validate if the function doesn't have a variable table 
        if self.functions[self.currentFunc]['varTab'] is None:
            # Create and link the variable table with the specified function
            self.functions[self.currentFunc]['varTab'] = VariableTable()
        
        
    """
    Adds a variable to the variable table of the current function.

    Parameters:
    # var_name is a string with  the name of the variable to be added.
    # var_type is a string with the type of the variable.
    # value is a any (int|float) with the initial value of the variable. Defaults to None.
    """
    def add_variable_to_current_func(self, var_name, var_type, memDirection, value=None):
        # Access to the variable table of the current function (KEY) 
        # Remember: self.functions is the dictonary (for functions)
        # current_vars is an instance of the VariableTable class
        current_vars = self.functions[self.currentFunc]['varTab']
        
        # If the function isn't global, validate if the variable already exists
        if self.currentFunc != self.globalName:
            global_vars = self.functions[self.globalName]['varTab'].variableTable
            if var_name in global_vars:
                raise ValueError(f"Variable '{var_name}' ya definida en el ámbito global")

        # Add the values of the variable to the variable table
        current_vars.add_variable(var_name, var_type, value, memDirection)

    """
    Returns the variables of the current function.

    Returns a variable table of the current function.
    """
    def get_current_function_vars(self):
        # Validate if there's a current function name selected
        if self.currentFunc is None:
            raise ValueError("No current function set")
        
        # Rertuns the variable table
        return self.functions[self.currentFunc]['varTab'].variableTable
    

    """
    BORRAR
    """
    def print_directory(self):
        for func_name, func_data in self.functions.items():
            print(f"Función '{func_name}': Tipo = {func_data['tipo']}")
            var_table = func_data['varTab']
            if var_table:
                for var_name, var_info in var_table.variableTable.items():
                    print(f"  Tabla Variables '{var_name}': Tipo = {var_info['type']}, Valor = {var_info['value']}")
            else:
                print("  Sin variables")
    
    """
    Delete the var table that it's no longer required.

    Parameters:
    # func_name is a string with  the name of the function
    """
    def delete_variable_table(self, func_name):       
        # Validate if the function has a variable table to delete
        if self.functions[func_name]['varTab'] is None:
            raise ValueError("No hay tabla de variables para eliminar")
        
        self.functions[func_name]['varTab'] = None
    
    def get_current_type(self, name):
        varTable = self.functions[self.currentFunc]['varTab'].variableTable
        varTableGlobal = self.functions[self.globalName]['varTab'].variableTable
        
        if name in varTableGlobal:
            return varTableGlobal[name]['type']
        
        elif name in varTable:
            return varTable[name]['type']
        else:
            raise ValueError("No current variable")
