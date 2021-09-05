
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
    matriz_1 = []


def main():
    vector_1, vector_2 = vectores()
    sumavectores(vector_1, vector_2)


main()
