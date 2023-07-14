def multiplos(A,B):

    if A % B == 0 or B % A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

def main():
    valores = input().split()
    A,B = int(valores[0]), int(valores[1])
    multiplos(A,B)

if __name__=='__main__':
    main()