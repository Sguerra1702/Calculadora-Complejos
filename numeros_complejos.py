import math


def suma_complejos(num1, num2):
    return (num1[0] + num2[0]), (num1[1] + num2[1])


def resta_complejos(num1, num2):
    return (num1[0] - num2[0]), (num1[1] - num2[1])


def multiplicacion_complejos(num1, num2):
    return (num1[0] * num2[0]) - (num1[1] * num2[1]), (num1[0] * num2[1]) + (num2[0] * num1[1])


def division_complejos(num1, num2):
    res = []
    a = num1[0]
    b = num1[1]
    c = num2[0]
    d = num2[1]
    return ((a * c) + (b * d)) / ((c ** 2) + (d ** 2)), ((b * c) - (a * d)) / ((c ** 2) + (d ** 2))


def modulo_complejos(num):
    a = num[0]
    b = num[1]
    return math.sqrt((a ** 2) + (b ** 2))


def conjugado_complejos(num):
    return multiplicacion_complejos(num, (-1, 0))


def conversion_polar_cart(num):
    x = num[0] * math.cos(num[1])
    y = num[0] * math.sin(num[1])
    return round(x, 5), round(y, 5)


def c_fase(num):
    fase = math.atan(num[1] / num[0])
    if (num[0] < 0 and num[1] < 0) or num[0] < 0:
        return 180 + math.degrees(fase)
    elif num[1] < 0:
        return 360 + math.degrees(fase)
    else:
        return math.degrees(fase)


def cart_polar(num):
    h = modulo_complejos(num)
    alpha = c_fase(num)
    return h, alpha
