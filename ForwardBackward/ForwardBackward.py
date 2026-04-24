# Forward
import numpy as np

print("FORWARD\n")

w = 0.7
x = 2
y = 1
n = 0.5

print("Peso de la entrada: ", w)
print("Input: ", x)
print("Output: ", y)
print("Tasa aprendizaje: ", n)

sop = w * x

print("Error: ", sop)

predicted = round(1/(1+(np.exp(-(sop)))),4)

if predicted >= 0.5:
    pred = 1
else:
    pred = 0

print("Predicho: ", predicted)
print("Funcion de activacion: ", pred, "\n")


#Backward
print("BACKWARD\n")

dError = round(2*(predicted-y),4)
dPredicted = round((1/(1+(np.exp(-(sop)))))*(1-(1/(1+(np.exp(-(sop)))))),4)
dSop = x
gra = round(dError*dPredicted*dSop,4)

print("Derivada de Error: ", dError)
print("Derivada de Predicted: ", dPredicted)
print("Derivada de SOP: ", dSop)
print("Gradiente: ", gra, "\n")

print("W nuevo: ", round(w-(n*gra),4), "\n")