def ValoresAbCd(A,B,C,D):
    
    if B > C and D > A:
        if 0 <= (C+D) > (A+B):
            parA = A % 2
            if parA == 0:
                print("Valores aceitos")

            else:
                print("Valores nao aceitos")

        else:
            print("Valores nao aceitos")
            
    else:
        print("Valores nao aceitos")

def main():
    entradaValores = input().split()
    A,B,C,D = (int(entradaValores[0]), int(entradaValores[1]), int(entradaValores[2]), int(entradaValores[3]))
    ValoresAbCd(A,B,C,D)

if __name__=='__main__':
    main()
