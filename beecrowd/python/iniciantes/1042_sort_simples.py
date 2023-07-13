def Do_Menor(min,max,A,B,C):
    if min < A < max:
        return A
    elif min < B < max:
        return B
    else:
        return C

def imprime_normal(A,B,C):
    print(A)
    print(B)
    print(C)

def main():
    entrada = input().split()
    A,B,C = int(entrada[0]), int(entrada[1]), int(entrada[2])
    minimo = (min(A,B,C))
    maximo = (max(A,B,C))
    resultado = Do_Menor(minimo, maximo, A, B, C)
    print(minimo)
    print(resultado)
    print(maximo)
    print()
    imprime_normal(A,B,C)


if __name__=='__main__':
    main()
    