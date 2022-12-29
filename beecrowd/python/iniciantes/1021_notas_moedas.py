def NotasMoedas(entrada):
    if 0<= entrada<=1000000.00:
        print('NOTAS:')
        V100 = entrada // 100
        print(f'{V100:.0f} nota(s) de R$ 100.00')

        V50 = (entrada%100)//50
        print(f'{V50:.0f} nota(s) de R$ 50.00')

        V20 = ((entrada%100)%50)//20
        print(f'{V20:.0f} nota(s) de R$ 20.00')

        V10 = (((entrada%100)%50)%20)//10
        print(f'{V10:.0f} nota(s) de R$ 10.00')

        V5 = ((((entrada%100)%50)%20)%10)//5
        print(f'{V5:.0f} nota(s) de R$ 5.00')

        V2 = (((((entrada%100)%50)%20)%10)%5)//2
        print(f'{V2:.0f} nota(s) de R$ 2.00')

        print('MOEDAS:')
        V1 = ((((((entrada%100)%50)%20)%10)%5)%2)//1
        print(f'{V1:.0f} moeda(s) de R$ 1.00')

        V050 = (((((((entrada%100)%50)%20)%10)%5)%2)%1)//0.50
        print(f'{V050:.0f} moeda(s) de R$ 0.50')

        V025 = ((((((((entrada%100)%50)%20)%10)%5)%2)%1)%0.50)//0.25
        print(f'{V025:.0f} moeda(s) de R$ 0.25')

        V010 = (((((((((entrada%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)//0.10
        print(f'{V010:.0f} moeda(s) de R$ 0.10')

        V005 = ((((((((((entrada%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)//0.05
        print(f'{V005:.0f} moeda(s) de R$ 0.05')

        V001 = (((((((((((entrada%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)%0.05)/0.01
        print(f'{V001:.0f} moeda(s) de R$ 0.01')

def main():
    entrada = float(input())
    NotasMoedas(entrada)

if __name__=='__main__':
    main()
