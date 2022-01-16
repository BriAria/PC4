#!/usr/bin/env python
# coding: utf-8

# Problema 1:
# Escribe un programa en Python para encontrar los números que son divisibles por 7 y
# múltiplos de 5, entre 1500 y 2700 (ambos incluidos).

# In[3]:


numero = 1500
while numero >=1500 and numero <= 2700:
    if numero % 7 == 0 and numero % 5 ==0:
        print(numero)
    numero += 1
    continue
        


# Problema 2:
# Escriba un programa en Python para construir el siguiente patrón, usando un bucle for
# anidado
# #*
# #* *
# #* * *
# #* * * *
# #* * * * *
# #* * * *
# #* * *
# #* *
# #*

# In[17]:


for i in range(1,6):
    print('* '*i)
for j in range(4,0,-1):
    print('* '*j)


# Problema 3:
# Escriba un programa en Python para contar la cantidad de números pares e impares de una
# serie de números.
# Lista de números = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Resultado esperado:
# Cantidad de números pares: 5
# Cantidad de números impares: 4

# In[24]:


def cantidad_pares_impares (lista_de_numeros):
    pares, impares = 0, 0
    
    for n in lista_de_numeros:
        if n % 2 == 0:
            pares += 1
        
        else:
            impares += 1
            
    return pares, impares

lista_de_numeros = [1,2,3,4,5,6,7,8,9]
resultado = cantidad_pares_impares (lista_de_numeros)

print(f'La cantidad de pares es:{resultado[0]}')
print(f'La cantidad de impares es:{resultado[1]}')
        


# Problema 4:
# Escriba un programa Python que imprima cada elemento y su tipo correspondiente de la
# siguiente lista.
# Lista de muestra:
# [1452, 11.23, 1 + 2j, True, 'Python', (0, -1), [5, 12], {"Clase": 'V', "Seccion": 'A'} ]

# In[34]:


Lista_de_muestra = [1452, 11.23, 1 + 2j, True, 'Python', (0, -1), [5, 12], {"Clase": 'V', "Seccion": 'A'} ]

for i in range(len(Lista_de_muestra)):
    print(f'Elemento: {Lista_de_muestra[i]} - Tipo: {type(Lista_de_muestra[i])}')


# Problema 5:
# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
# Nota: La secuencia de Fibonacci es la serie de números:
# 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
# Cada número siguiente se obtiene sumando los dos números anteriores

# In[60]:


#METODO 1
def Serie_Fibonacci(n):
    if n == 0:
        Fibonacci = []
    elif n == 1:
        Fibonacci = [0]
    elif n == 2:
        Fibonacci = [0,1]
    elif n > 2:
        Fibonacci = [0,1]
        i = 1
        while i < n-1:
            Fibonacci.append(Fibonacci[i] + Fibonacci[i-1])
            i += 1
    return Fibonacci
        
resultado = Serie_Fibonacci (50)
print(resultado)
    


# In[ ]:


#METODO 2
def Fibonacci(n):
    if n < 2:
        return n
    else:
       
        return fib(n-1) + fib(n-2)
for i in range(50):
    print(Fibonacci(i))


# Problema 6:
# Escriba un programa Python que acepte una cadena y calcule el número de dígitos y letras.
# Ejemplo: Python 3.2
# Resultado esperado:
# Letras 6
# dígitos 2

# In[2]:


def Conteo_letras_num(cadena):
    digitos = 0
    letras = 0
    
    for cad in cadena:
        if cad.isdigit():
            digitos += 1
        elif cad.isalpha():
            letras += 1
        else:
            pass
    return digitos, letras

texto = input('Escriba un texto:')
resultado = Conteo_letras_num(texto)

print(f'Cantidad de digitos: {resultado[0]}')
print(f'Cantidad de letras: {resultado[1]}')


# Problema 7:
# Escribe una función de Python para multiplicar todos los números en una lista.
# Lista de muestra: [8, 2, 3, -1, 7]
# Resultado esperado: -336

# In[5]:


def multiplicacion (num):
    producto = 1
    
    for n in num:
        producto *= n
    
    return producto

lista_numeros = [2,3,5,7,11]

print(multiplicacion(lista_numeros))


# Problema 8:
# Escriba un programa en Python para invertir una cadena.
# Cadena de muestra: "1234abcd"
# Salida esperada: "dcba4321"
# 

# In[20]:


#datux => xutad

cadena = 'datux'
#Opcion 1
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i], end = ' ')

#Opcion 2
print()

print(cadena[::-1])


# Problema 9:
# Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos
# únicos de la primera lista.
# 

# In[23]:


def lista_val_unicos(lista):
    return set(lista)

numeros = [5,5,6,7,7,7,8,8,9,9,11,10]

resultado = lista_val_unicos(numeros)

print(f'Lista_original:{numeros}')
print(f'Lista de valores unicos:{resultado}')


# Problema 10:
# Escriba una función de Python que tome un número como parámetro y verifique que el
# número sea primo o no.

# In[24]:


def si_es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range (2, numero):
            if numero % i == 0:
                return False
        return True
    
for i in range(1,100):
    print(i, si_es_primo(i))


# Problema 11:
# Escriba una función de Python que devuelva los números pares de una lista dada.
# Lista de muestras: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Resultado esperado: [2, 4, 6, 8]

# In[27]:


def pares(numeros):
    num_pares = []
    
    for n in numeros:
        if n % 2 == 0:
            num_pares.append(n)
    return num_pares

numeros = [1,3,4,6,7,8,10]

resultado = pares(numeros)

print(f'numeros ingresados:{numeros}')
print(f'numeros pares ingresados: {resultado}')


# Problema 12:
# Escribe una función de Python para calcular el factorial de un número (un entero no negativo).
# La función acepta el número como argumento.

# In[31]:


def factorial (n):
    producto = 1
    for i in range (1, n+1):
        producto *= i
    return producto


print(factorial(11))

