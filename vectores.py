import numpy as np


def vectores():
    np_vector_1 = [3 + 4j, 2 - 3j, 5 + 8j]
    np_vector_2 = [5 + 4j, 1 - 9j, 4 + 6j]
    vector_1 = np.array(np_vector_1)
    vector_2 = np.array(np_vector_2)
    print(vector_1)
    print(vector_2)
    print("")
    print("")
    return vector_1, vector_2


def sumavectores(vector_1, vector_2):
    vector_suma = vector_1 + vector_2
    print("El vector resultante de sumar A y B es", vector_suma)
    print("")
    print("")


def restavectores(vector_1, vector_2):
    vector_resta = vector_1 - vector_2
    print("El vector resultante de sumar A y B es", vector_resta)
    print("")
    print("")


def inverso_aditivo(vector_1, vector_2):
    inverso_ad_1 = -1 * vector_1
    inverso_ad_2 = -1 * vector_2
    print("Los inversos aditivos de los vectores A y B son", inverso_ad_1, "y", inverso_ad_2, "respectivamente")
    print("")
    print("")


def escalar_vector(vector_1, vector_2):
    print("digite un complejo escalar")
    escalar = complex(input())
    resultante_1 = escalar * vector_1
    resultante_2 = escalar * vector_2
    print("Los vectores resultantes de multiplicar el escalar", escalar, "por los vectores A y B son", resultante_1, "y", resultante_2)
    print("")
    print("")


def matrices():
    np_matriz_1 = [[3 + 5j, 8 - 2j, 4 - 8j], [8 - 2j, 6 + 5j, 1 - 8j], [2 + 5j, 3 - 8j, 4 + 7j]]
    np_matriz_2 = [[4 + 5j, 6 - 3j, 5 - 1j], [9 - 3j, 5 + 5j, 1 - 2j], [5 + 8j, 7 - 4j, 3 + 5j]]
    matriz_1 = np.array(np_matriz_1)
    matriz_2 = np.array(np_matriz_2)
    print(matriz_1)
    print("")
    print(matriz_2)
    print("")
    print("")
    return matriz_1, matriz_2


def suma_matriz(matriz_1, matriz_2):
    suma = matriz_1 + matriz_2
    print("la matriz resultante es:")
    print(suma)
    print("")
    print("")


def inverso_aditivo_matriz(matriz_1, matriz_2):
    inv_aditivo_matriz_1 = (-1) * matriz_1
    inv_aditivo_matriz_2 = (-1) * matriz_2
    print("los inversos aditivos de las matrices son")
    print(inv_aditivo_matriz_1)
    print(inv_aditivo_matriz_2)
    print("")
    print("")


def mult_matriz_escalar(matriz_1, matriz_2):
    print("Digite un número complejo")
    escalar = complex(input())
    escalar_matriz_1 = escalar * matriz_1
    escalar_matriz_2 = escalar * matriz_2
    print("Las matrices resultantes de multiplicar el escalar", escalar, "por las matrices A y B son", escalar_matriz_1, "y", escalar_matriz_2)
    print("")
    print("")


def transpuesta_matriz(matriz_1, matriz_2):
    transpuesta_1 = np.transpose(matriz_1)
    transpuesta_2 = np.transpose(matriz_2)
    print("Las transpuestas de las matrices son")
    print(transpuesta_1)
    print(transpuesta_2)


def conjugado_matriz(matriz_1, matriz_2):
    conjugado_1 = np.conjugate(matriz_1)
    conjugado_2 = np.conjugate(matriz_2)
    print("Los conjugados de las matrices son")
    print(conjugado_1)
    print(conjugado_2)
    print("")
    print("")


def conjugado_vector(vector_1, vector_2):
    conjugado_vector_1 = np.conjugate(vector_1)
    conjugado_vector_2 = np.conjugate(vector_2)
    print("Los conjugados de los vectores son")
    print(conjugado_vector_1)
    print(conjugado_vector_2)
    print("")
    print("")


def adjunta_matriz(matriz_1, matriz_2):
    adjunta_1 = np.matrix(matriz_1)
    adjunta_2 = np.matrix(matriz_2)
    print("Las adjuntas de las matrices son")
    print(adjunta_1)
    print(adjunta_2)
    print("")
    print("")


def mult_matrices(matriz_1, matriz_2):
    multi_matriz = np.matmul(matriz_1, matriz_2)
    print("La matriz producto es")
    print(multi_matriz)
    print("")
    print("")


def producto_interno(vector_1, vector_2):
    interno = np.dot(vector_1, vector_2)
    print("El producto interno de los vectores es:", interno)
    print("")
    print("")


def norma_vector(vector_1, vector_2):
    suma_cuadrados_1 = 0
    suma_cuadrados_2 = 0
    n = len(vector_1)
    for cont in range(n - 1):
        suma_cuadrados_1 = suma_cuadrados_1 + (vector_1[cont] ** 2)
        suma_cuadrados_2 = suma_cuadrados_2 + (vector_2[cont] ** 2)
    norma1 = np.sqrt(suma_cuadrados_1)
    norma2 = np.sqrt(suma_cuadrados_2)
    print("La norma del vector A es:")
    print(norma1)
    print("La norma del vector B es:")
    print(norma2)
    print("")
    print("")


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
    print("")
    print("")


def producto_tensor(vector_1, vector_2):
    tensor = np.tensordot(vector_1, vector_2, axes=0)
    print("El producto tensor de los dos vectores es ")
    print(tensor)
    print("")
    print("")


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
