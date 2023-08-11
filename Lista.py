def lista(n):
    w = 1
    n = int(n)
    arreglo = []
    while w <= n:
        arreglo.append(w)
        w += 1
    print(arreglo)
    if n % 2 == 0:
        x = n / 2
    else:
        x = (n / 2) - 0.5
    x = int(x)
    n = n - 1
    while x >= 0:
        y = arreglo[x]
        z = arreglo[n-(x)]
        arreglo[n-x] = y
        arreglo[x] = z
        x -= 1
    print(arreglo)
    return

