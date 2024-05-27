class ConstantDirectory:
    def __init__(self):
        self.constant_directory = {}
        self.AVAIL_INT = iter(range(10001, 11001))  # Available addresses for integers
        self.AVAIL_FLOAT = iter(range(11001, 12001))  # Available addresses for floats
        self.AVAIL_STRING = iter(range(12001, 13001))  # Available addresses for strings

    """
        Get a new memory address based on the constant type.

        Parameters:
        # constant_type is a string indicating the type of the constant ('int' or 'float')

        Returns a new memory address for the specified constant type.
    """
    def get_new_address(self, constant_type):
        try:
            if constant_type == 'int':
                address = next(self.AVAIL_INT)
            elif constant_type == 'float':
                address = next(self.AVAIL_FLOAT)
            elif constant_type == 'string':
                address = next(self.AVAIL_STRING)
            else:
                raise ValueError("Unknown constant type")
            return address
        except StopIteration:
            raise ValueError("No more addresses available for type: " + constant_type)

    """
        Add a constant to the directory with its type and memory address.

        Parameters:
        # constant is the constant value to be added.
        # constant_type is a string indicating the type of the constant ('int' or 'float')
    """
    def add_constant(self, constant, constant_type):
        if constant not in self.constant_directory:
            address = self.get_new_address(constant_type)
            self.constant_directory[constant] = {'address': address, 'type': constant_type}
            #print(f"Constante {constant} ({constant_type}) almacenada en la dirección de memoria {address}")
        else:
            address = self.constant_directory[constant]['address']
            #print(f"Constante {constant} ({constant_type}) ya estaba almacenada en la dirección de memoria {address}")

    """
        Determine the type of a constant (int or float).

        Parameters:
        # constant is the constant value whose type is to be determined.

        Returns a string indicating the type of the constant ('int' or 'float').
    """
    def determine_const_type(self, constant):
        if isinstance(constant, int):
            return 'int'
        elif isinstance(constant, float):
            return 'float'
        elif isinstance(constant, str):
            return 'string'
        else:
            raise ValueError("Unknown constant type")

    """
        Get the dictionary of a constant.

        Parameters:
        # constant is the constant value whose memory address is to be retrieved.

        Returns the constant with type and address.
    """
    def get_constant(self, constant):   
        if constant in self.constant_directory:
            return self.constant_directory[constant]
        else:
            return None

    """
        Get all constants with their addresses.

        Returns a dictionary of all constants and their addresses.
    """
    def get_all_constants(self):
        all_constants = {}

        for constant, info in self.constant_directory.items():
            address = info['address']
            all_constants[constant] = address
            
        return all_constants