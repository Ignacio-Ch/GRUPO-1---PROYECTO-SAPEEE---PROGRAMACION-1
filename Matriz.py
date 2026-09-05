def matrizestacionamiento(n, m):
    matriz = []
    for i in range(n):
        fila_nueva = []
        for j in range(m):
            fila_nueva.append('libre')
        matriz.append(fila_nueva)
    return matriz

def ingresotamañomatriz():
    print("Ingrese el tamaño de la matriz (mxn)")
    x = int(input("Ingrese el parametro m:"))
    x = numeropositivo(x)
    y = int(input("Ingrese el parametro n:"))
    y = numeropositivo(y)
    return x, y

def numeropositivo(x):
    while x <=0:
        x = int(input("Ingrese un valor positivo"))
    return x




def main():
    n, m = ingresotamañomatriz()
    mat = matrizestacionamiento(n, m)
    for i in range(len(mat)):
        print(mat[i])




main()
