import numpy as np


def vectores():
    print("Digite el tamaño de los vectores")
    n = int(input())
    cont = 0
    vector_1 = []
    vector_2 = []
    while cont < n:
        print("digite el ", cont + 1, "° número complejo del primer vector")
        complejo = complex(input())
        vector_1[0] = complejo
        print("digite el ", cont + 1, "° número complejo del primer vector")
        complejo2 = complex(input())
        vector_2[0] = complejo2
        cont = cont + 1

    return vector_1, vector_2


def sumavectores(vector_1, vector_2):
    n = len(vector_1)
    vector_suma = []
    for cont in range(n-1):
        vector_suma[cont] = vector_1[cont] + vector_2[cont]
    print("El vector resultante de sumar A y B es", vector_suma)


def restavectores(vector_1, vector_2):
    n = len(vector_1)
    vector_resta = []
    for cont in range(n-1):
        vector_resta[cont] = vector_1[cont] - vector_2[cont]
    print("El vector resultante de sumar A y B es", vector_resta)


def inverso_aditivo(vector_1, vector_2):
    n = len(vector_1)
    inverso_ad_1 = []
    inverso_ad_2 = []
    for cont in range(n-1):
        inverso_ad_1[cont] = -1 * vector_1[cont]
        inverso_ad_2[cont] = -1 * vector_2[cont]
    print("Los inversos aditivos de los vectores A y B son", inverso_ad_1, "y", inverso_ad_2, "respectivamente")


def escalar_vector(vector_1, vector_2):
    print("digite un complejo escalar")
    escalar = complex(input())
    n = len(vector_1)
    resultante_1 = []
    resultante_2 = []
    for cont in range(n-1):
        resultante_1[cont] = escalar * vector_1[cont]
        resultante_2[cont] = escalar * vector_2[cont]
    print("Los vectores resultantes de multiplicar el escalar", escalar, "por los vectores A y B son", resultante_2, "y", resultante_2)


def matrices():
    matriz_1 = [[3 + 5j, 8 - 2j, 4 - 8j], [8 - 2j, 6 + 5j, 1 - 8j], [2 + 5j, 3 - 8j, 4 + 7j]]
    matriz_2 = [[4 + 5j, 6 - 3j, 5 - 1j], [9 - 3j, 5 + 5j, 1 - 2j], [5 + 8j, 7 - 4j, 3 + 5j]]
    return matriz_1, matriz_2


def suma_matriz(matriz_1, matriz_2):
    suma = []
    for i in range(3):
        for j in range(3):
            suma[i, j] = matriz_1[i, j] + matriz_2[i, j]
    print("la matriz resultante es:")
    print(suma)


def inverso_aditivo_matriz(matriz_1, matriz_2):
    inv_aditivo_matriz_1 = []
    inv_aditivo_matriz_2 = []
    for i in range(3):
        for j in range(3):
            inv_aditivo_matriz_1[i, j] = (-1) * matriz_1[i, j]
            inv_aditivo_matriz_2[i, j] = (-1) * matriz_2[i, j]
    print("los inversos ")


def mult_matriz_escalar(matriz_1, matriz_2):
    print("Digite un número complejo")
    escalar = complex(input())
    escalar_matriz_1 = []
    escalar_matriz_2 = []
    for i in range(3):
        for j in range(3):
            escalar_matriz_1[i, j] = escalar * matriz_1[i, j]
            escalar_matriz_2[i, j] = escalar * matriz_2[i, j]
    print("Las matrices resultantes de multiplicar el escalar", escalar, "por las matrices A y B son", escalar_matriz_1, "y", escalar_matriz_2)


def transpuesta_matriz(matriz_1, matriz_2):
    transpuesta_1 = []
    transpuesta_2 = []
    for i in range(3):
        for j in range(3):
            transpuesta_1[i, j] = matriz_1[j, i]
            transpuesta_2[i, j] = matriz_2[j, i]
    print("Las transpuestas de las matrices son")
    print(transpuesta_1)
    print(transpuesta_2)


def conjugado_matriz(matriz_1, matriz_2):
    conjugado_1 = []
    conjugado_2 = []
    for i in range(3):
        for j in range(3):
            conjugado_1[i, j] = np.conjugate(matriz_1[i, j])
            conjugado_2[i, j] = np.conjugate(matriz_2[i, j])
    print("Los conjugados de las matrices son")
    print(conjugado_1)
    print(conjugado_2)


def conjugado_vector(vector_1, vector_2):
    n = len(vector_1)
    conjugado_vector_1 = []
    conjugado_vector_2 = []
    for cont in range(n):
        conjugado_vector_1[cont] = np.conjugate(vector_1[cont])
        conjugado_vector_2[cont] = np.conjugate(vector_2[cont])
    print("Los conjugados de los vectores son")
    print(conjugado_vector_1)
    print(conjugado_vector_2)


def adjunta_matriz(matriz_1, matriz_2):
    adjunta_1 = np.matrix(matriz_1)
    adjunta_2 = np.matrix(matriz_2)
    print("Las adjuntas de las matrices son")
    print(adjunta_1)
    print(adjunta_2)


def mult_matrices(matriz_1, matriz_2):
    multi_matriz = np.matmul(matriz_1, matriz_2)
    print("La matriz producto es")
    print(multi_matriz)


def producto_interno(vector_1, vector_2):
    n = len(vector_1)
    interno = 0
    for cont in range(n-1):
        interno = interno + (vector_1[cont] * vector_2[cont])
    print("El producto interno de los vectores es:", interno)


def norma_vector(vector_1, vector_2):
    suma_cuadrados_1 = 0
    suma_cuadrados_2 = 0
    n = len(vector_1)
    for cont in range(n - 1):
        suma_cuadrados_1 = suma_cuadrados_1 + (vector_1[cont] ^ 2)
        suma_cuadrados_2 = suma_cuadrados_2 + (vector_2[cont] ^ 2)
    norma1 = np.sqrt(suma_cuadrados_1)
    norma2 = np.sqrt(suma_cuadrados_2)
    print("La norma del vector A es:")
    print(norma1)
    print("La norma del vector B es:")
    print(norma2)


def si_matriz_hermitiana(matriz_1, matriz_2):
    adjunta_1 = np.matrix(matriz_1)
    adjunta_2 = np.matrix(matriz_2)
    if matriz_1 == adjunta_1:
        print("La matriz A es hermitiana")
    else:
        print("La matriz A NO es hermitiana")
    if matriz_2 == adjunta_2:
        print("La matriz A es hermitiana")
    else:
        print("La matriz A NO es hermitiana")


def producto_tensor(vector_1, vector_2):
    tensor = np.tensordot(vector_1, vector_2, axes=0)
    print("El producto tensor de los dos vectores es ")
    print(tensor)


def main():
    vector_1, vector_2 = vectores()
    sumavectores(vector_1, vector_2)
    restavectores(vector_1, vector_2)
    inverso_aditivo(vector_1, vector_2)
    escalar_vector(vector_1, vector_2)
    matriz_1, matriz_2 = matrices()
    suma_matriz(matriz_1, matriz_2)
    inverso_aditivo_matriz(matriz_1, matriz_2)
    mult_matriz_escalar(matriz_1, matriz_2)
    transpuesta_matriz(matriz_1, matriz_2)
    conjugado_matriz(matriz_1, matriz_2)
    conjugado_vector(vector_1, vector_2)
    adjunta_matriz(matriz_1, matriz_2)
    mult_matrices(matriz_1, matriz_2)
    producto_interno(vector_1, vector_2)
    norma_vector(vector_1, vector_2)
    si_matriz_hermitiana(matriz_1, matriz_2)
    producto_tensor(vector_1, vector_2)


main()
