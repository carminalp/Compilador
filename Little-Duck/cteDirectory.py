class ConstantDirectory:
    """
        Constructor
        Initialize the ConstantDirectory with separate address spaces for integers and floats.
    """
    def __init__(self):
        self.constant_directory = {}
        self.next_int_address = 800  # Initialize memory address for integers starting from 800
        self.next_float_address = 901 # Initialize memory address for floats starting from 901

    """
        Get a new memory address based on the constant type.

        Parameters:
        # constant_type is a string indicating the type of the constant ('int' or 'float')

        Returns a new memory address for the specified constant type.
    """
    def get_new_address(self, constant_type):
        if constant_type == 'int':
            address = self.next_int_address
            self.next_int_address += 1
        elif constant_type == 'float':
            address = self.next_float_address
            self.next_float_address += 1
        
        return address

    """
        Add a constant to the memory directory with its type and memory address.

        Parameters:
        # constant is the constant value to be added.
        # constant_type is a string indicating the type of the constant ('int' or 'float')

        Returns the memory address assigned to the constant.
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