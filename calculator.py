'''
Калькулятор который будет выполнять стандартные вычисления
'''

class Calculator: 

    def __init__(self, one_digit, two_digit, action):
        self.one_digit = one_digit
        self.two_digit = two_digit
        self.action = action

    def sum(self):
        if self.action == '+':
            return self.one_digit + self.two_digit


    def __str__(self) :
        return int(self.one_digit) + int(self.two_digit)


one_action = Calculator(1,2,'+')
print(one_action)