class Calculator:
    """Калькулятор с базовыми функциями"""
    def add(x, y): 
        """ Функция сложения
        x и y - параметры для сложения"""
        return x + y 

    def subtract(x, y):
        """ Функция вычитания
        x и y - параметры для вычитания"""

        return x - y


    def multiply(x, y):
        """Функция умножения
        x и y - параметры для умножения"""
        return x * y


    def divide(x, y):
        """ Функция деления
        x и y - параметры для деления"""
        if y == 0:
            raise ValueError('На ноль не делим')
        return x / y