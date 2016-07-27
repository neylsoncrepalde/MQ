# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:06:56 2016

@author: Usuario
"""

class Dog:                          # Cuidado init com 2 underlines
    def __init__(self, name, breed): #Função que cria um novo cachorro
        self.name = name
        self.breed = breed
        self.has_bone = False
        self.memory = ""
        
    def hear(self, something):
        self.memory = something
        
    def take_bone(self):
        self.has_bone = True
        
    def drop_bone(self):
        if self.has_bone == True:
            self.has_bone = False
        
    def bark(self):
        if not(self.has_bone):
            print("WOWuff")