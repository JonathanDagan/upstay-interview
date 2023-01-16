from functools import cache


class Calculator(object):
    operator = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    def __init__(self):
        pass

    @cache
    def perform_operation(self, operation, x, y):
        return self.operator[operation](x, y)

    def calculate(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        operands = []
        operators = []
        number = ""
        negative = False
        for char in expression:
            if char == '-':
                negative = True
            elif char.isalnum():
                number += char
            else:
                if number:
                    operands.append(int(number) * (-1 if negative else 1))
                    number = ""
                    negative = False
                while (operators and operators[-1] != '(' and precedence[char] <= precedence[operators[-1]]):
                    op2, op1 = operands.pop(), operands.pop()
                    operator = operators.pop()
                    result = self.perform_operation(operator, op1, op2)
                    operands.append(result)
                operators.append(char)
        if number:
            operands.append(int(number) * (-1 if negative else 1))
        while operators:
            op2, op1 = operands.pop(), operands.pop()
            operator = operators.pop()
            result = self.perform_operation(operator, op1, op2)
            operands.append(result)
        return operands[0]
