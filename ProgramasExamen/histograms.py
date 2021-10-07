import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

archivo = ""
#Obtain which file to obtain the data from
while exit != 1:
    choice = int(input("Enter which file you want to get the data from: "))
    if choice == 1:
        archivo = "data01.txt"
        break
    elif choice == 2:
        archivo = "data02.txt"
        break
    elif choice == 3:
        archivo = "data03.txt"
        break
    elif choice == 4:
        archivo = "pregunta3.txt"
        break
    else:
        print('Please enter a valid option.')
        exit = 1

# Obtain data from files
text = pd.read_csv(archivo)
dFile = text.to_numpy()
decimals = 4

dFile = list(map(lambda x: '%.3f' % (x), dFile))

# Get length 
N = len(dFile) 
print("N:", N + 1)

# Get number of classes
C = (int(1 + 3.33 * math.log10(N)))+1
print("C:", C)

# Get a Min and a max
dFile = np.array(dFile)
dFile = dFile.astype(float)
dFile.sort()
print("Max: ", dFile[-1] ,"Min:", dFile[0])

# Get width
W = ((dFile[(-1)]-dFile[0])/C)
W += 10**-(decimals)
W = round(W,decimals)
print("W:", W)

# Get intervals
print("\nIntervals")
ranges = np.empty([C,2],dtype=np.float64)
ranges[0,0] = dFile[0]
ranges[0][1] = dFile[0]+W
for i in range(1,C):
    for j in range(2):
        if j==0:
            ranges[i][j]=ranges[i-1][j+1]
        else:
            ranges[i][j]=ranges[i][j-1]+W
print(ranges)

# Get frequency
print("\nFrequency")
freq = np.zeros([C])
for i in range(N):
    for j in range(C):
        if(ranges[j,0]<=dFile[i]<ranges[j,1]):
            freq[j]+=1
            break
print(freq)

# Get the sum of frequencies
print("\nSum of the frequencies:", N + 1)
ranges=np.unique(ranges.flatten())

# Show Graph
plt.hist(dFile,ranges)
plt.show()
