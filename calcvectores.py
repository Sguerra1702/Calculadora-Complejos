import numeros_complejos as lc


def sumamatrix(a, b):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):
        # Ojo con referencias:
        # Hay que crear un objeto fila nuevo para cada fila. si no se hace
        # Todos quedan apuntando al mismo objeto, es decir una sola fila.
        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.suma_complejos(a[j][k], b[j][k])
    return r


def multivectores():
    print("hola")


def producto_tensor_vectores(a, b):
    na = len(a)
    nb = len(b)
    nr = nb * na
    r = [(0,0)] * nr
    index = 0
    for j in range(na):
        for k in range(nb):
            r[index] = lc.multiplicacion_complejos(a[j], b[k])
            index = index + 1

    return r


def main():
    a = [(0, 2), (1, 6)]
    b = [(0, -5), (3, 4), (-2.1,)]
    print(producto_tensor_vectores(a, b))


main()
