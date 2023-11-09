class FunctionsM07:
    def __init__(self, number_list):
        if type(number_list) != list:
            self.number_list = []
            raise ValueError('The param must be a list')
        else:
            for e in number_list:
                if type(e) != int:
                    self.number_list = []
                    raise ValueError('The list must contain just integer values')
            self.number_list = number_list

    def __verificar_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    def verificar_primo(self):
        boolean_list = []
        for e in self.number_list:
            boolean_list.append(self.__verificar_primo(e))
        return boolean_list
    
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
        return m, r
    
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
        param_list = ['c', 'f', 'k']
        response_list = []
        try:
            assert origin in param_list and destiny in param_list, f'Invalid param, it can take just this values {param_list}'
            for e in self.number_list:
                response_list.append(self.__conversion_grados(e, origin, destiny))
            return response_list
        except AssertionError as e:
            print(e)
            return None

    def __factorial(self, n):
        if type(n) != int or n < 0:
            return 'Invalid parameter'
        elif n <= 1:
            return 1
        else:
            return n * self.__factorial(n - 1)
    def factorial(self):
        factorial_list = []
        for e in self.number_list:
            factorial_list.append(self.__factorial(e))
        return factorial_list