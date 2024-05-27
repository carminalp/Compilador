from Compi.Directories.VariableTable import VariableTable

class FuncDirectory:
    # Constructor 
    def __init__(self):
        # initializes 
        self.functions = {}
        self.currentFunc = None
        self.globalName = None
        # Global memory counters using iterators
        self.AVAIL_GLOBAL_INT = iter(range(1002, 2000))
        self.AVAIL_GLOBAL_FLOAT = iter(range(2001, 3000))
        # Local memory counters using iterators
        self.AVAIL_LOCAL_INT = iter(range(7001, 8000))
        self.AVAIL_LOCAL_FLOAT = iter(range(8001, 9000))

    """
    Adds a new function to the directory.

    Parameters:
    # name is a string with the name of the function to be added.

    """
    def add_function(self, name, tipo):
        if name not in self.functions:
            self.functions[name] = {'tipo': tipo, 'varTab': None, 'start_quad': None, 'goto_quad': None, 'parameters': None}
        else:
            raise ValueError(f"Multiple declaration of the function {name}")
        
    
    """
    Sets the current function to the specified function name.

    Parameters:
    # name is a string with the name of the function to be set as current.      
    """
    def set_current_function(self, name):
        self.currentFunc = name

    def get_current_function(self):
        return self.currentFunc

    """
    Sets the global name to the globalName variable.

    Parameters:
    # name is a string with the name of the program.      
    """
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
        self.functions[self.currentFunc]['varTab'] = VariableTable()
        
        
    """
    Adds a variable to the variable table of the current function.

    Parameters:
    # var_name is a string with  the name of the variable to be added.
    # var_type is a string with the type of the variable.
    # value is a any (int|float) with the initial value of the variable. Defaults to None.
    """
    def add_variable_to_current_func(self, var_name, var_type, value=None):
        current_vars = self.functions[self.currentFunc]['varTab']
        
        if self.currentFunc != self.globalName:
            global_vars = self.functions[self.globalName]['varTab'].variableTable
            if var_name in global_vars:
                raise ValueError(f"Variable '{var_name}' ya definida en el ámbito global")

        is_global = self.currentFunc == self.globalName
        memDirection = self.get_next_memory_address(var_type, is_global)
        current_vars.add_variable(var_name, var_type, memDirection, value)

    """
    Get the next available memory address based on the variable type and scope.

    Parameters:
    - var_type: The type of the variable ('int' or 'float').
    - is_global: Boolean indicating if the variable is global.

    Returns the next available memory address for the variable.
    """
    def get_next_memory_address(self, var_type, is_global):
        try:
            if is_global:
                if var_type == 'int':
                    address = next(self.AVAIL_GLOBAL_INT)
                elif var_type == 'float':
                    address = next(self.AVAIL_GLOBAL_FLOAT)
            else:
                if var_type == 'int':
                    address = next(self.AVAIL_LOCAL_INT)
                elif var_type == 'float':
                    address = next(self.AVAIL_LOCAL_FLOAT)
            return address
        except StopIteration:
            raise MemoryError("Exceeded maximum memory allocation for " + ("global" if is_global else "local") + f" {var_type} variables")

    """
    Adds the type of params of the function

    Parameters:
    # param_type is a string with the type of the variable (int|float).
    """
    def add_params_to_current_func(self, param_type):
        if self.functions[self.currentFunc]['parameters'] is None:
            self.functions[self.currentFunc]['parameters'] = []
        
        self.functions[self.currentFunc]['parameters'].append(param_type)


    """
    Returns the variables of the current function.

    Returns a variable table of the current function.
    """
    def get_current_function_vars(self):
        if self.currentFunc is None:
            raise ValueError("No current function set")
        
        return self.functions[self.currentFunc]['varTab'].variableTable
    
    """
    Delete the var table that it's no longer required.

    Parameters:
    # func_name is a string with  the name of the function
    """
    def delete_variable_table(self, func_name):       
        self.functions[func_name]['varTab'] = None
    
    """
    Get the type of the variables

    Parameters:
    # name is a string with  the name of the variable to search the type
    """
    def get_current_type(self, name):
        varTable = self.functions[self.currentFunc]['varTab'].variableTable
        varTableGlobal = self.functions[self.globalName]['varTab'].variableTable
        
        if name in varTableGlobal:
            return varTableGlobal[name]['type']
        
        elif name in varTable:
            return varTable[name]['type']
        else:
            raise NameError(f"The {name} variable is not defined")

    """
    Get the address of the variables

    Parameters:
    # name is a string with  the name of the variable to search the type
    """
    def get_current_address(self, name):
        varTable = self.functions[self.currentFunc]['varTab'].variableTable
        varTableGlobal = self.functions[self.globalName]['varTab'].variableTable
        
        if name in varTableGlobal:
            return varTableGlobal[name]['direction']
        
        elif name in varTable:
            return varTable[name]['direction']
        else:
            raise NameError(f"The {name} variable is not defined")


    """
    Get the parameters of the function

    # name is a string with  the name of the function to search the parameters
    """
    def get_parameters(self, name):
        return self.functions[name]['parameters']