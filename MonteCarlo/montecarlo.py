
# importing the necessary libraries
import random
import numpy as np
import matplotlib.pyplot as plt
 
# limits of integration
a = 0
b = np.pi
N = 400
 

def f(x):
    return np.sin(x)

values = []
 
for i in range(N):
   

    ar = np.zeros(N)
 
    for i in range (len(ar)):
        ar[i] = random.uniform(a,b)
 
    integral = 0.0
 
    for i in ar:
        integral += f(i)
 
    result = (b-a)/float(N)*integral
 
    values.append(result)
 
plt.title("Distribution from the calculated areas")
 
plt.hist (values, bins=30, ec="black")

plt.xlabel("Areas")
plt.show()