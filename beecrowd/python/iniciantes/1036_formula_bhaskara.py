def bhaskara(A,B,C):
    delta = ((B**2)-4*A*C)
    return delta
    
def raiz_valores(A,B,C):
    if A != 0 and C >= 0:
        raiz =(C**(1/2))
        
        raiz1 = ((-B+raiz)/(2*A))
        raiz2 = ((-B-raiz)/(2*A))

        print(f'R1 = {raiz1:.5f}')
        print(f'R2 = {raiz2:.5f}')

    else:
        print("Impossivel calcular")
    
def main():
    entrada_valores = input().split()

    A,B,C = (float(entrada_valores[0]), float(entrada_valores[1]), float(entrada_valores[2]))
    
    valor = bhaskara(A,B,C)
    raiz_valores(A,B,valor)
    
if __name__=='__main__':
    main()
