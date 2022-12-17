def cedulas(valor):
    if 0<valor<1000000:
        qnt = valor // 100
        qnt50 = (valor%100)//50
        qnt20 = ((valor%100)%50)//20
        qnt10 = (((valor%100)%50)%20)//10
        qnt5 = ((((valor%100)%50)%20)%10)//5
        qnt2 = (((((valor%100)%50)%20)%10)%5)//2
        qnt1 = ((((((valor%100)%50)%20)%10)%5)%2)//1

        print(valor)
        print(f'{qnt:.0f} nota(s) de R$ 100,00')
        print(f'{qnt50:.0f} nota(s) de R$ 50,00')
        print(f'{qnt20:.0f} nota(s) de R$ 20,00')
        print(f'{qnt10:.0f} nota(s) de R$ 10,00')
        print(f'{qnt5:.0f} nota(s) de R$ 5,00')
        print(f'{qnt2:.0f} nota(s) de R$ 2,00')
        print(f'{qnt1:.0f} nota(s) de R$ 1,00')

def main():

    valor = int(input("Informe o valor: "))
    cedulas(valor)

if __name__=='__main__':
    main()
