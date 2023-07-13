def como_saber(A,B,C):
    valor = A + B + C
    if A+B>C and B+C>A and A+C>B:
        print(f'Perimetro = {valor:.1f}')
    else:
        valor = ((A+B)*C)/2
        print(f'Area = {valor:.1f}')


def main():
    entrada = input().split()
    A,B,C = float(entrada[0]), float(entrada[1]), float(entrada[2])
    como_saber(A,B,C)

if __name__=='__main__':
    main()
    