
def sumapares(n,m):
    i= 0
    while n<=m:
        if n%2==0:
            i= i+n
        else:
            i= i
        n= n+1
    return i
def esPrimo(p):
    p= p*p
    x=0
    y= 2
    while y<= (p-1):
        if p % y == 0:
            x += 1
        else:
            x = x
        y +=1
    if x>=2:
        x= False
    else:
        x= True
    return x

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
def calculadora ():
     print('Ingresa la opcion deseada.\n 1-Suma \n 2-Resta\n 3-Multiplicacion \n 4-Division')
     x = int(input())
     a = int(input('Ingresa el primer numero:\n'))
     b = int(input('Ingresa el segundo numero:\n'))
     if x == 1:
        resultado = a + b
     elif x == 2:
        resultado = a - b
     elif x == 3:
        resultado = a * b
     else:
        resultado = a / b
     return resultado


