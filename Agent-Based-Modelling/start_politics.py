#ABM
#START
from politicians import Politician
from voters import Voter
from random import randrange
from random import normalvariate

print(1)
 
#Alocando os voters
electorate = []
for i in range(50):
    voter_i = Voter(randrange(-200,200),randrange(-200,200))
    electorate.append(voter_i)

print(2)
#Criando o zoo
zoo = []
for i in range(5):
    politician_i = Politician(randrange(-200,200),randrange(-200,200))
    zoo.append(politician_i)
print(3)

#Fazendo o eleitor votar
result = [0] * 5
for voter in electorate:
    v = voter.vote()
    result[v] = result[v]+1 
    #Cuidado que a posição do resultado deve ser o voto, não a iteração

print(result)
    




#Movendo os políticos
for i in range(20):
    for pol in zoo:
        pol.turtle.goto(randrange(-200,200),randrange(-200,200))
    

while True:
    pass