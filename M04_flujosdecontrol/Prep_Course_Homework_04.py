#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

x = 8
if x > 0:
    print("It's greater than zero")
elif x < 0:
    print("It's less than zero")
else:
    print("It´s equal to zero")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = "Data Scientist"
b = "Data Engineer"
if type(a) == type(b):
    print('They are of the same data type')
else:
    print('They aren´t of the same data type')


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for num in range(1, 21):
    if(num % 2 == 0):
        print(num, 'It´s an even number')
    else:
        print(num, 'It´s an odd number')


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for num in range(1, 5):
    res = num**3
    print(num,'Elevado a',3,'es igual a',res)


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

x = 6
for i in range(x):
    print('Loop: ', i+1)


# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

x = 4
fact = 1
if type(x) == int:
    if x > 0:
        num = x
        while x > 0:
            fact = fact * x
            x -= 1
        print('The factorial of',num,'is',fact)
    else:
        print('The number isn´t greater than zero')
else:
    print('The number isn´t a integer')

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

x = 5
while x > 0:
    num = x
    fact = 1
    for i in range(1, x+1):
        fact *= i
    print('The factorial of', num, 'is', fact)
    x -= 1


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

list = [1, 7, 3, 9]
for i in list:
    num = i
    fact = 1
    while i > 0:
        fact *= i
        i -= 1
    print('The factorial of', num, 'is:', fact)


# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for i in range(31):
    isPrime = True
    num = i
    if i <= 1:
        isPrime = False
    else:
        while i > 1:
            if num == i:
                i -= 1
            elif num % i == 0:
                isPrime = False
                i -= 1
            else:
                i -= 1

    if isPrime == True:
        print('Prime Number:',num)    



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

for i in range(31):
    isPrime = True
    num = i
    if i <= 1:
        continue
    else:
        while i > 1:
            if num == i:
                i -= 1
                continue
            elif num % i == 0:
                isPrime = False
                break
            i -= 1

    if isPrime == True:
        print('Prime Number:',num)



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

without_break = 0
for i in range(31):
    isPrime = True
    num = i
    if i <= 1:
        isPrime = False
    else:
        while i > 1:
            without_break += 1
            if num == i:
                i -= 1
            elif num % i == 0:
                isPrime = False
                i -= 1
            else:
                i -= 1

    if isPrime == True:
        print('Prime Number:',num)
print('Loops without break:', without_break)


# In[57]:

with_break = 0
for i in range(31):
    isPrime = True
    num = i
    if i <= 1:
        continue
    else:
        while i > 1:
            with_break += 1
            if num == i:
                i -= 1
                continue
            elif num % i == 0:
                isPrime = False
                break
            i -= 1

    if isPrime == True:
        print('Prime Number:',num)
print('Loops with break:', with_break)

print('It was optimized by:', 100 - (with_break / without_break * 100), '%')

# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

i = 100
max = 300

while i <= max:
    if i % 12 != 0:
        i += 1
        continue
    print(i, 'is divisible by 12')
    i += 1
    




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

def EsPrimo(valor):
    if valor <= 1:
        return False
    else:
        for i in range(2, valor):
            if valor % i == 0:
                return False
        return True

print('Enter a number')
num = int(input())
isPrime = EsPrimo(num)
print('Prime is it?:', isPrime)
while True:
    print('Do you want know the next prime number?')
    print('1. Yes')
    print('2. No')
    x = int(input())
    if x == 1:
        while True:
            num += 1
            if EsPrimo(num):
                print(num, 'is the next prime number')
                break
    else:
        print('Programa terminado')
        break

# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

num = 100
max = 300

while num <= max:
    if num % 3 == 0 and num % 6 == 0:
        print('The first number divisible by 3 and multiple of 6 is:', num)
        break
    num += 1  


# %%
