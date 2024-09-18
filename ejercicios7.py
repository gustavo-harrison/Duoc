matriz = [
    [2, 3, 4],
    [3, 4, 2],
    [1, 1, 1]
]

suma = 0

for i in matriz:
    for elemento in i:
        suma += elemento

print("Matriz de 3x3:")
for i in matriz:
    print(i)

print(f"\nLa sumatoria de los elementos de la matriz es: {suma}")