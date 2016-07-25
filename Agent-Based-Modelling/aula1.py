# -*- coding: utf-8 -*-
"""
Agent-Based Modelling - aula 1
Created on Mon Jul 25 13:53:17 2016

@author: Neylson
"""

#Exemplos

#print("Tell me your age")
#age = input()
#ge = int(age)
#rint("Your age in 5 years", age+5)

#Criando uma função de somar

def add(a, b):
    print("My sum function")
    c = a + b
    return c
    
#Criando uma função que pede a idade e calcula o ano de nascimento
def birth(age):
    print("My birth year ")
    ano = 2016
    nasc = ano - age
    return nasc
    
#Creating int_input() function

def int_input():
    print("Type a number:")
    number = input()
    print("Let's see if your a grown up.")
    return int(number)
    
age = int_input()
if age < 18:
    print("Minor -> go to Disney")
elif age > 65:
    print("Older person")
else:
    print("Adult")

print("other")


