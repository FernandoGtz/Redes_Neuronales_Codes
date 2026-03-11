import random
import numpy as np
import matplotlib.pyplot as plt

n_inputs = int(input("Ingrese número de entradas: "))
n_examples = int(input("Ingrese número de ejemplos de entrenamiento: "))
n = float(input("Ingrese tasa de aprendizaje: "))
max_epocas = int(input("Ingrese máximo de épocas: "))

w = [0.0] * n_inputs
b = 0
cAND = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
cOR = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

print("\nSeleccione inicialización:")
print("1.-Ceros\n2.-Manual\n3.-Aleatorio")
opcion = int(input("Opción: "))

if opcion == 1:
    for i in range(n_inputs):
        w[i] = 0
    b = 0
    print("\nLos pesos se han ajustado a 0")
if opcion == 2:
    for i in range(n_inputs):
        w[i] = float(input(f"Ingrese peso {i + 1}: "))
    b = float(input("Ingrese sesgo: "))
if opcion == 3:
    for i in range(n_inputs):
        w[i] = random.random()
    b = random.random()
    print(f"\nLos pesos se han ajustado a: {w}, {b} ")


datos = []
salidas_esperadas = []

for i in range(n_examples):
    print(f"\nEjemplo {i + 1}: ")
    ejemplo = []
    for j in range(n_inputs):
        valor = float(input(f"Ingrese valor de X{j + 1}: "))
        ejemplo.append(valor)
    datos.append(ejemplo)

    salida = int(input("Ingrese salida esperada (0 o 1): "))
    salidas_esperadas.append(salida)

epoca = 0
hubo_error = True

while hubo_error and epoca < max_epocas:
    hubo_error = False
    print(f"\n--- Época {epoca+1} ---")

    for i in range(n_examples):
        suma = 0
        for j in range(n_inputs):
            suma += datos[i][j] * w[j]
        suma += b
        print(f"La suma del ejemplo {j+1} es: {suma}")
        if suma >= 0:
            prediccion = 1
        else:
            prediccion = 0
        print(f"La salida lineal es {prediccion} y la salida esperada es {salidas_esperadas[i]}")

        error = salidas_esperadas[i] - prediccion

        if prediccion != salidas_esperadas[i]:
            print("Se necesitan ajustar pesos...")
            for j in range(n_inputs):
                w[j] = w[j] + (n * error * datos[i][j])
                print(f"Peso {j+1} ajustado a: {w[j]}")
            b = b + (n * error)
            print(f"Sesgo ajustado a: {b}")
            hubo_error = True
        else:
            print("No se necesitan ajustar pesos")

    epoca += 1

# Graficar la línea de decisión
# Obviamos que serán 2 entradas y no más para graficar en 2D
if n_inputs == 2:
    x = np.linspace(0, 1)  # 100 puntos entre 0 y 10
    y = (-w[0] * x - b) / w[1]  # Ecuación de la línea de decisión
    plt.plot(x, y)
    for i in range(n_examples):
        x1 = datos[i][0]
        x2 = datos[i][1]
        plt.scatter(x1, x2)
    plt.title("Separación de clases con Perceptrón")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

print("\n------------------------------")
print(f"Entrenamiento finalizado en {epoca} épocas")
print(f"Pesos finales: {w}")
print(f"Sesgo final: {b}")

