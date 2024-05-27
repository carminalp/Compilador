class Quadruple:
    # Constructor 
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    # Returns the object quad as a string "(+, a, b, t1)"
    def __repr__(self):
        return f"({self.operator}, {self.left_operand}, {self.right_operand}, {self.result})"