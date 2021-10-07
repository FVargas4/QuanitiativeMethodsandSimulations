import csv
import math 

def lessSigns(a):
    menos=0
    length=len(a)
    if a[0]=='-':
        menos=menos+1
    for i in  range(1,length):
        if a[i]=='-' and a[i-1]!='-':
            menos=menos+1
    return menos

def plusSigns(a):
    mas=0
    length=len(a)
    if a[0]=='+':
        mas=mas+1
    for i in  range(1,length):
        if a[i]=='+' and a[i-1]!='+':
            mas=mas+1
    return mas

def countPlus(a):
    mas=0
    for i in  a:
        if i=='+':
            mas=mas+1
    return mas

def countLess(a):
    menos=0
    for i in  a:
        if i=='-':
            menos=menos+1
    return menos

def getSigns(a):
    signs=[]
    length=len(a)
    for i in range(1,length):
        #print(a[i])
        if a[i-1] < a[i]:
            signs.append("+")
        else:
            signs.append("-")
    return signs

dataaux= []

with open('pregunta3.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        number=float(row[0])
        dataaux.append(number)

data = [round(num, 4) for num in dataaux]


def getH(valor):
    if valor == .1:
        return 1.645
    elif valor == .05:
        return 1.96
    elif valor == .1:
        return 2.575   

C=10

MAX=round(max(data),4)

MIN=0

W=0.1
W=round(W,4)

N=len(data)

print("N:"+str(N)+"\n")

signs = getSigns(data)

print(getSigns(data))

print('(+): '+str(countPlus(signs))+'\n(-): '+str(countLess(signs))+"\n")

total = countLess(signs) +countPlus(signs)

print('Total: '+str(total)+'\n+ runs: '+str(plusSigns(signs))+"\n- runs: "+str(lessSigns(signs))+"\n")

runs = plusSigns(signs) + lessSigns(signs)

print('Stadistics\n')

miu = ((total*2)-1)/3 

aux = ((16*total) -29) /90

sigma = math.sqrt(aux)

print('Miu: '+str(miu)+", "+'Sigma: '+str(sigma)+"\n")

Zscore = (runs-miu)/sigma  

print('Zscore: '+str(Zscore)+", "+'Z Alfa/2: '+str( getH(0.05))+"\n")

if abs(Zscore) < getH(0.05):
    print('Since '+str(Zscore)+" < " + str(getH(0.05))+".\nH0: Not rejected\n")
else:
    print('Since '+str(Zscore)+ " > " + str(getH(0.05))+".\nH0: Rejected\n")