class Memory:
    def __init__(self):
        self.global_int = []
        self.global_float = []
        self.local_int = []
        self.local_float = []
        self.temp_int = []
        self.temp_float = []
        self.temp_bool = []
        self.constant_string = []
        self.constant_int = []
        self.constant_float = []

    """
        Determine the memory segment and base address for a given address.

        Parameters:
        - address is a int with the memory address to locate.

        Returns a tuple containing the memory segment (dictionary) and the base address (min).
    """
    def get_memory_segment(self, address):
        if 1002 <= address <= 2000:
            return self.global_int, 1002
        elif 2001 <= address <= 3000:
            return self.global_float, 2001
        elif 4001 <= address <= 5000:
            return self.temp_int, 4001
        elif 5001 <= address <= 6000:
            return self.temp_float, 5001
        elif 6001 <= address <= 7000:
            return self.temp_bool, 6001
        elif 7001 <= address <= 8000:
            return self.local_int, 7001
        elif 8001 <= address <= 9000:
            return self.local_float, 8001
        elif 10001 <= address <= 11000:
            return self.constant_string, 10001
        elif 11001 <= address <= 12000:
            return self.constant_int, 11001
        elif 12001 <= address <= 13000:
            return self.constant_float, 12001

    """
        Set a value in the memory at a specific address.

        Parameters:
        - address is a int with the memory address of the value
        - value is the value to store at the specified address.
    """
    def set_value(self, address, value):
        segment, base_address = self.get_memory_segment(address)
        index = address - base_address
        while len(segment) <= index:
            segment.append(None)
        segment[index] = value

    """
        Get a value from the memory at a specific address.

        Parameters:
        - address is an int with the memory address to retrieve the value from.

        Returns the value stored at the specified address, or Error if not found.
    """
    def get_value(self, address):
        segment, base_address = self.get_memory_segment(address)
        index = address - base_address
        return segment[index]

    """
        Initialize memory with constants from a constant directory.

        Parameters:
        - constant_directory is a dictionary where keys are values and values are the memory addresses
    """
    def initialize_constants(self, constant_directory):
        for value, address in constant_directory.items():
            self.set_value(address, value)