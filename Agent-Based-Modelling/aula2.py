# -*- coding: utf-8 -*-
"""
ABM - Aula 2
@author: Neylson
"""
#Generating random numbers
import gc
from random import randrange

gc.enable()

print(randrange(0, 10))

#Writing a guessing program
def computer_guess():
    randnumber = randrange(0, 100)
    print("Can you guess what number did I think of (0-99)?")
    
    while True:
        ans = int(input())
        if ans == randnumber:
            print("Yeah! You did it!")
            break
        else:
            if ans > randnumber:
                print("It's too high")
            else:
                print("It's too low")

#Printing uneven numbers
def uneven():
    a = 10
    while a < 100:
        a = a + 1
        if a % 2 == 0:
            continue
        print(a)
        
#Creating a list
l = [0,1,2,4,7]
print(l)

l = list(range(5))
print(l)

#Building a for loop
for i in range(90, 101):
    if i > 99:
        print("finally")
    print(i)
    
l = [7,4,8,5,2,9]
for i in l:
    print(i)
    
l = [0, 'car', 8]
for i in l:
    print(i)

#Usando vários prints
for i in range(4):
    print(i, end= ' ')
    print(i+1, end = ' ')
    print(i+2, end = ' ')
    print(i+3)

#Usando loops aninhados
for line in range(4):
    for col in range(4):
        print(col+line, end = ' ')
    print(' ')
        
#Trabalhando com uma lista

l = [0,1,2,3,4,5]
l.append(10)
l.append('car')
len(l)
l.pop() #Retorna o último elemento da lista e retira-o
l
l[3]
l[-1] #Conta para trás
l[-3]

l = [] #Criando uma lista vazia
l
l.append(5)
l.append(3)

#Create a list [0,1,4,9,16] from an empty list usign for loop
l = []
for i in range(5):
    l.append(i**2)






