import random
import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=float)
outAND = np.array([0, 0, 0, 1], dtype = float).T
outOR = np.array([0, 1, 1, 1], dtype = float).T
output = np.array([0, 0, 0, 0], dtype = float).T
w = np.array([0.0, 0.0, 0.0]).T
l = 0.05

epMax = int(input("-> Ingresa el máximo de épocas: "))

opC = int(input("-> Elige la función lógica a entrenar:\n1.- AND\n2.- OR\nOpción: "))
if opC == 1:
    output = outAND
elif opC == 2:
    output = outOR
elif opC != 1 or opC != 2:
    print("\nOpcion no válida")
    exit()

# Inicialización de pesos y sesgo
opW = int(input("-> Elige la inicialización de pesos:\n1.- Ceros\n2.- Manual\n3.- Aleatorio\nOpción: "))

if opW == 1:
    for i in range(len(w)-1):
        w[i] = 0
    w[2] = 0
    print("\nLos pesos y el sesgo se han ajustado a 0")

if opW == 2:
    for i in range(len(w)-1):
        w[i] = float(input(f"Ingrese peso de X{i + 1} (w{i+1}): "))
    w[2] = float(input(f"Ingrese el sesgo (b): "))
    print(f"\nLos pesos se han ajustado a: {w[0]} y {w[1]}, y el sesgo a: {w[2]} ")

if opW == 3:
    for i in range(len(w)-1):
        w[i] = random.random()
    w[2] = random.random()
    print(f"\nLos pesos se han ajustado a: {w[0]} y {w[1]}, y el sesgo a: {w[2]} ")

epoca = 1
error = True

# Cálculo de error y ajuste de pesos y sesgo
while error == True and epoca < epMax:
    error = False
    print(f"--- Época {epoca} ---")

    for i in range(len(inputs)):
        x = inputs[i]
        d = output[i]

        y_in = np.dot(x, w)

        y = 1 if y_in >= 0 else 0

        e = d - y

        if e != 0:
            w = w + l * (e) * np.array(x)
            error = True
        print(f"Entrada: {x}, Esperado: {d}, Obtenido: {y}, Error: {e}, Pesos: {w}")

    epoca += 1

# Graficación
x_vals = np.linspace(-1, 2, 100)

if w[1] != 0:
    y_vals = (-w[0] * x_vals - w[2]) / w[1]
    y_vals_b = (-w[0] * x_vals) / w[1]
    plt.plot(x_vals, y_vals, label="Frontera de decisión")
    plt.plot(x_vals, y_vals_b, label="Frontera de decisión")
else:
    print("No se puede graficar (w[1] = 0)")

for i in range(len(inputs)):
    x1 = inputs[i][0]
    x2 = inputs[i][1]

    if output[i] == 1:
        plt.scatter(x1, x2, marker='o', label="Clase 1" if i == 0 else "")
    else:
        plt.scatter(x1, x2, marker='x', label="Clase 0" if i == 0 else "")

plt.title("Separación de clases con Perceptrón")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()
plt.legend()
plt.show()

# Conclusión
print(f"\n-->Entrenamiento terminado en {epoca} epocas...")
print(f"Pesos finales: w1 = {w[0]}, w2 = {w[1]}")
print(f"Bias final: b = {w[2]}")








