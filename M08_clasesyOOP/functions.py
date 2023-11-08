class FunctionsM07:
    def __init__(self, number_list):
        self.number_list = number_list

    def __verificar_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    def verificar_primo(self):
        for e in self.number_list:
            if self.__verificar_primo(e):
                print(e, 'It is a prime number')
            else:
                print(e, 'It is not a prime number')
    
    def __valor_modal(self, num_list):
        e_r = 0
        c_r = 0
        for e in num_list:
            if num_list.count(e) > c_r:
                e_r = e
                c_r = num_list.count(e)
        return e_r, c_r
    def valor_modal(self):
        m, r = self.__valor_modal(self.number_list)
        print('The modal is', m, 'and it is repited', r, 'times')
    
    def __conversion_grados(self, value, measure_origen, measure_destiny):
        if measure_origen == 'c':
            if measure_destiny == 'f':
                return (value * 9/5) + 32
            elif measure_destiny == 'k':
                return value + 273.15
            else:
                print('Not valid measure destiny parameter') 
        elif measure_origen == 'f':
            if measure_destiny == 'c':
                return (value - 32) * 5/9
            elif measure_destiny == 'k':
                return (value - 32) * 5/9 + 273.15
            else:
                print('Not valid measure destiny parameter')
        elif measure_origen == 'k':
            if measure_destiny == 'c':
                return value - 273.15
            elif measure_destiny == 'f':
                return ((value - 273.15) * 9/5) + 32
            else:
                print('Not valid measure destiny parameter')
        else:
            print('Not valid measure origen parameter')
    def conversion_grados(self, origin, destiny):
        for e in self.number_list:
            print(e, origin, 'is', self.__conversion_grados(e, origin, destiny), destiny)

    def __factorial(self, n):
        if type(n) != int or n < 0:
            return 'Invalid parameter'
        elif n <= 1:
            return 1
        else:
            return n * self.__factorial(n - 1)
    def factorial(self):
        for e in self.number_list:
            print('The factorial of', e, 'is', self.__factorial(e))