def ValoresIntervalos(A):
    if A >= 0:
        if 0 <= A <= 25:
            print("Intervalo [0,25]")
        elif 25 <= A <= 50:
            print("Intervalo (25,50]")
        elif 50 <= A <= 75:
            print("Intervalo (50,75]")
        elif 75 <= A <= 100:
            print("Intervalo (75,100]")
        elif A >= 10:
            print("Fora de intervalo")
    else:
        print("Fora de intervalo")
def main():
    entrada_numero = float(input())
    ValoresIntervalos(entrada_numero)

if __name__=='__main__':
    main()
