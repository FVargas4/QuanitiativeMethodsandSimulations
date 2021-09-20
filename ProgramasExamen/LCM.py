import csv
import math

def genRandom(x,a,c,m,n):
    
    resultados=[]
    for i in range(n):
        aux=((a*x) +c)%m
        x=aux
        resultados.append(x/m)
    
    return resultados

#linear congruential method: 

#Get the Seed
x=int(input("Enter X0: "))

#Get the multiplier
a=int(input("Enter a:  "))

#Get the incrememnt constant
c=int(input("Enter c:  "))

#Get the modulus
m=int(input("Enter m:  "))

#Get the random numbers
n=int(input("How many random numbers?   "))

#Apply the function
print(genRandom(x,a,c,m,n))