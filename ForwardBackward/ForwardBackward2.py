import numpy as np
import matplotlib.pyplot as plt

prediction = []
iteration = []
errors = []

def sigmoid(sop):
    return 1.0/(1+(np.exp(-(sop))))

def error(predicted, target):
    return np.power((predicted - target),2)

def deriv_error_predicted(predicted, target):
    return 2*(predicted - target)

def deriv_activation_sop(sop):
    return sigmoid(sop)*(1.0-sigmoid(sop))

def deriv_sop_w(x):
    return x

def update_w(w, grad, learning_rate):
    return w - learning_rate * grad

# Definir entradas, salida y tasa de aprendizaje
n_inputs = 10
x = np.random.random(n_inputs)  # Vector de 10 entradas aleatorias
w = np.random.random(n_inputs)  # Vector de 10 pesos aleatorios
target = 0.3
learning_rate = 0.1
print("Entradas aleatorias: ", x, "\n")
print("Pesos iniciales: ", w, "\n")

for k in range(10000):
    iteration.append(k)

    # Forward Pass
    y = np.dot(w, x)  # Suma ponderada de todas las entradas
    predicted = sigmoid(y)
    err = error(predicted, target)
    print(f"Iteración {k} - Error: {err}")

    prediction.append(predicted)
    errors.append(err)

    # Backward Pass
    g1 = deriv_error_predicted(predicted, target)
    g2 = deriv_activation_sop(predicted)
    
    # Calcular gradientes para cada peso
    grad = g1 * g2 * x

    # Actualizar todos los pesos
    w = w - learning_rate * grad

# Crear gráfico de Predicción vs Iteración
plt.figure(figsize=(10, 6))
plt.plot(iteration, prediction, 'b-', linewidth=2)
plt.xlabel('Iteración')
plt.ylabel('Predicción')
plt.title('Predicción vs Iteración')
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"\nPesos finales: {w}")
print(f"Predicción final: {predicted}")
print(f"Target: {target}")

