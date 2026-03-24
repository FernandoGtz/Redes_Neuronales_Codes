print("\nOperaciones")
print("\n1. Multiplicacion de matrices\n2. Producto punto\n3. Transpuesta de una matriz\n4. Multiplicacion elemento a elemento")
op = int(input("Ingresa la operacion a calcular: "))

if op == 1:
    mA = []
    mB = []

    filasA = int(input("Filas de A: "))
    columnasA = int(input("Columnas de A: "))

    filasB = int(input("Filas de B: "))
    columnasB = int(input("Columnas de B: "))

    if columnasA == filasB:
        print("--- MATRIZ A ---")
        for i in range(filasA):
            fila = []
            for j in range(columnasA):
                valor = int(input(f"A[{i+1}][{j+1}]: "))
            fila.append(valor)
            mA.append(fila)

        print("--- MATRIZ B ---")
        for i in range(filasB):
            fila = []
            for j in range(columnasB):
                valor = int(input(f"B[{i+1}][{j+1}]: "))
                fila.append(valor)
            mB.append(fila)

        resultado = []
        for i in range(filasA):
            fila_resultado = []
            for j in range(columnasB):
                suma = 0
                for k in range(columnasA):
                    suma += mA[i][k] * mB[k][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)

        print("Resultado A * B:")
        for fila in resultado:
            print(fila)
    else:
        print("No se pueden multiplicar las matrices.")

elif op == 2:
    n = int(input("Ingresa la longitud de los vectores: "))

    A = []
    B = []

    print("--- VECTOR A ---")
    for i in range(n):
        A.append(int(input(f"A[{i+1}]: ")))

    print("--- VECTOR B ---")
    for i in range(n):
        B.append(int(input(f"B[{i+1}]: ")))

    suma = 0
    for i in range(n):
        suma += A[i] * B[i]

    print("Producto punto =", suma)

elif op == 3:
    matriz = []

    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    print("--- MATRIZ ---")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"[{i+1}][{j+1}]: ")))
        matriz.append(fila)

    transpuesta = []
    for i in range(columnas):
        fila = []
        for j in range(filas):
            fila.append(matriz[j][i])
        transpuesta.append(fila)

    print("Transpuesta:")
    for fila in transpuesta:
        print(fila)

elif op == 4:
    mA = []
    mB = []

    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    print("--- MATRIZ A ---")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"A[{i+1}][{j+1}]: ")))
        mA.append(fila)

    print("--- MATRIZ B ---")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"B[{i+1}][{j+1}]: ")))
        mB.append(fila)

    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(mA[i][j] * mB[i][j])
        resultado.append(fila)

    print("Multiplicación elemento a elemento:")
    for fila in resultado:
        print(fila)

else:
    print("ta mal")