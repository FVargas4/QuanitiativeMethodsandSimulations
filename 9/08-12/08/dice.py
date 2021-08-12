import matplotlib.pyplot as plt
import random
trials = int(input('Enter the number of trials: ', ))
result = 0
cont = 0
freqs = {}

for i in range(trials):
    aux = random.randint(1,6)

    if aux in freqs:
        freqs[aux] += 1
    else:
        freqs[aux] = 1

    if aux == 5:
        result = result + aux
    else:
        result = result - 1

    faces = list(freqs.keys())
    freq = list(freqs.values())

    
print(f'Total Trails: {trials}')
print(f'Last Number: {aux}')
print(f'Total Money: ${result}')
print('')
plt.bar(faces, freq)
plt.xlabel('Numeros disponibles')
plt.ylabel('Frecuencia')
plt.show()
