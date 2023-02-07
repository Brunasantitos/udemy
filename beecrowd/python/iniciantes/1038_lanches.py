def valor_lanches(A,B):
    if A == 1:
        total = B * 4.00
        print(f'Total: R$ {total:.2f}')
    elif A == 2:
        total = B * 4.50
        print(f'Total: R$ {total:.2f}')
    elif A == 3:
        total = B * 5.00
        print(f'Total: R$ {total:.2f}')
    elif A == 4:
        total = B * 2.00
        print(f'Total: R$ {total:.2f}')
    elif A == 5:
        total = B * 1.50
        print(f'Total: R$ {total:.2f}')

def main():
    entrada_valores = input().split()
    A,B =(float(entrada_valores[0]), float(entrada_valores[1]))
    valor_lanches(A,B)

if __name__=='__main__':
    main()
    
