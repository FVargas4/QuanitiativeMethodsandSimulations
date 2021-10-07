import csv
import math 

def listRange(li, min, max):
    count = 0
    for x in li:
	    if min <= x <= max:
		    count += 1
    return count


fileData= []

#Get data from text file
with open('pregunta3.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        number = float(row[0])
        fileData.append(number)

fil3 = [round(num, 4) for num in fileData]



def getX2(a,e):
    X2 = []
    for i in a:
        X2.append(round((i-e)**2/e,4)) 
    return X2

def getH(c):

    c=c-1

    if c == 1:
        return 3.8415
    elif c == 2:
        return 5.9915
    elif c == 3:
        return 7.8147
    elif c == 4:
        return 9.4877
    elif c == 5:
        return 11.1433
    elif c == 6:
        return 12.5916
    elif c == 7:
        return 14.0671
    elif c == 8:
        return 15.5073
    elif c == 9:
        return 16.9190
    elif c == 10:
        return 18.3070
    elif c == 11:
        return 19.6751

def getTable(intervals,obs,exp,ecu):

    intlen = len(intervals)
    print("\nIntervals    Observed    Expected   (O - E)^2 / E\n")
    for i in  range(1,intlen):
        print(intervals[i]+"         " +str(obs[i])+"         "+str(exp) +"        " + str(ecu[i]))

    print("\n")
# # of classes
Classes = 10

W = 0.1

W=round(W,4)

expected = len(fil3)/Classes

aux = 0

lista =[]

classes=[]

for i in range(Classes) :

    top = round(aux+W-0.0001,4)
    
    arreglo = [aux , top]

    top = round(top+0.0001,4)

    lista.append(arreglo)

    result = "["

    result += str(aux)

    result += "-"

    result += str(top)

    result += ")"

    aux=top

    classes.append(result)

#imprimir las clases con su rango
print(classes)
print("\n")
print(lista)
print("\n")

#contar el numero dentro de ese rango
n = []

for x in lista:
  value = listRange(fil3, x[0], x[1])
  n.append(value)

print(n)
print("\n")
ecuation = getX2(n,expected)

print(ecuation)
print("\n")
x2 = sum(getX2(n,expected))

print("X^2: "+  str(x2 ) )
print("\n")
getTable(classes,n,expected,ecuation)

if x2 < getH(Classes):
    print('Since '+str(x2)+" < " + str(getH(Classes))+"\n.H0: Not rejected\n")
else:
    print('Since '+str(x2)+ " > " + str(getH(Classes))+".\nH0: Rejected\n")