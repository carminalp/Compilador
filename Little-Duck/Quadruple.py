class Quadruple:
    # Constructor 
    def __init__(self, operator, left_operand, right_operand, result):
        # initializes Quadruple atributes
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    # Returns the object quad as a string
    def __repr__(self):
        # "(+, a, b, t1)"
        return f"({self.operator}, {self.left_operand}, {self.right_operand}, {self.result})"
