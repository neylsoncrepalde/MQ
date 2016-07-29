#ABM
#START

from politicians import Politician
from voters import Voter
from random import randrange
from numpy import random
from numpy import argmax
import turtle

turtle.tracer(100,0)
#turtle.setworldcoordinates(0,0,5*101, 5*101)


print(1)
#Alocando os voters
electorate = []
for i in range(500):
    voter_i = Voter(random.normal(0,100),random.normal(0,100))
    electorate.append(voter_i)

print(2)
#Criando o zoo
politicians = []
for i in range(5):
    politician_i = Politician(randrange(-200,200),randrange(-200,200))
    politicians.append(politician_i)

print(3)
turtle.tracer(1,0)

#Colocando x rodadas de eleição
wins = [0] * len(politicians)

for rodada in range(5):
    print('round', rodada)
    #os eleitores votam
    votes = [0] * len(politicians)
    for voter in electorate:        
        v = voter.vote(politicians)
        votes[v] = votes[v] + 1
                
    print(votes)
    winner = argmax(votes)
    for i in range(5):
        if i == winner:
            politicians[i].readjust_after_election(True, politicians[i])
        else:
            politicians[i].readjust_after_election(False, politicians[winner])
            
    wins[winner] = wins[winner] + 1
    print('Politician', winner, 'is the round winner')
    

print(wins)
election_winner = argmax(wins)
print('Politician', election_winner, 'won the election')

    
while True:
    pass
