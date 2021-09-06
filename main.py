import numpy as np


def calccomplejos():
    print("Digite su primer numero complejo")
    comp1 = complex(input())
    print("Digite el segundo numero complejo")
    comp2 = complex(input())
    return comp1, comp2


def sumacompl(comp1, comp2):
    suma = comp1 + comp2
    print(comp1, "+", comp2, "= ", suma)


def restacompl(comp1, comp2):
    resta = comp1 - comp2
    print(comp1, "-", comp2, "= ", resta)


def multcompl(comp1, comp2):
    multi = comp1 * comp2
    print(comp1, "*", comp2, "= ", multi)


def divisioncomplejos(comp1, comp2):
    division = comp1 / comp2
    print(comp1, "/", comp2, "= ", division)


def conjugado_complejos(comp1, comp2):
    conjugado_1 = np.conjugate(comp1)
    conjugado_2 = np.conjugate(comp2)
    print("Los conjugados de ", comp1, "y de ", comp2, "Son ")
    print(conjugado_1)
    print(conjugado_2)
    print("respectivamente")


def main():
    comp1, comp2 = calccomplejos()
    sumacompl(comp1, comp2)
    restacompl(comp1, comp2)
    multcompl(comp1, comp2)
    divisioncomplejos(comp1, comp2)


main()
