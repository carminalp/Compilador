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
    def add_function(self, name):
        # Search if the name it already exist
        if name in self.functions:
            raise ValueError("Multiple declaración de función")
        # Initialize the function without a variable table
        self.functions[name] = None
        # Set the newly created function as the current function (to work whit it)
        self.currentFunc = name
    
    """
    Sets the current function to the specified function name.

    Parameters:
    # name is a string with the name of the function to be set as current.      
    """
    def set_current_function(self, name):
        
        # Search if the name exist
        if name not in self.functions:
            # Error if the function does not exist.
            raise ValueError("Function does not exist")
        # Set de current function name
        self.currentFunc = name

    def set_current_global(self, name):   
        self.globalName = name

    """
    Creates and link a variable table with the specified function.

    Parameters:
    # func_name is a string with the name of the function to create a variable table for.
    """
    def create_variable_table(self): 
        # Validate if the func_name exist      
        if self.currentFunc not in self.functions:
            raise ValueError("Función no existe")
        
        # Validate if the function doesn't have a variable table 
        if self.functions[self.currentFunc] is None:
            # Create and link the variable table with the specified function
            # Instancia de VariableTable (class)
            self.functions[self.currentFunc] = VariableTable()
        
        

    """
    Adds a variable to the variable table of the current function.

    Parameters:
    # var_name is a string with  the name of the variable to be added.
    # var_type is a string with the type of the variable.
    # value is a any (int|float) with the initial value of the variable. Defaults to None.
    """
    def add_variable_to_current_func(self, var_name, var_type, value=None):
        # Check if there's a current function selected
        if self.currentFunc is None:
            raise ValueError("No current function set")

        # Access to the variable table of the current function (KEY) 
        # Remember: self.functions is the dictonary (for functions)
        # current_vars is an instance of the VariableTable class
        current_vars = self.functions[self.currentFunc]
        
        """# Si la función no es global, comprobar si la variable ya existe en el ámbito global
        if self.currentFunc != self.globalName:
            global_vars = self.functions[self.globalName]['vars'].variableTable
            if var_name in global_vars:
                raise ValueError(f"Variable '{var_name}' ya definida en el ámbito global")"""

        # Add the values of the variable to the variable table
        current_vars.add_variable(var_name, var_type, value)

    """
    Returns the variables of the current function.

    Returns a variable table of the current function.
    """
    def get_current_function_vars(self):
        # Validate if there's a current function name selected
        if self.currentFunc is None:
            raise ValueError("No current function set")
        
        # Check if the current function doesn't have a VarTable
        if self.functions[self.currentFunc] is None:
            raise ValueError("No variable table for current function")
        
        # Rertuns the variable table
        return self.functions[self.currentFunc].variableTable
    
    """
    BORRAR
    """
    def print_directory(self):
        for func_name, var_table in self.functions.items():
            print(f"Función '{func_name}':")
            if var_table:
                for var_name, var_info in var_table.variableTable.items():
                    print(f"  Variable '{var_name}': Tipo = {var_info['type']}, Valor = {var_info['value']}")
            else:
                print("Sin variables")
    
    """
    Delete the var table that it's no longer required.

    Parameters:
    # func_name is a string with  the name of the function
    """
    def delete_variable_table(self, func_name):       
        if self.functions[func_name] is None:
            raise ValueError("No hay tabla de variables para eliminar")
        
        self.functions[func_name] = None
        
        # BORRAR
        print(f"Tabla de variables para la función '{func_name}' eliminada.")