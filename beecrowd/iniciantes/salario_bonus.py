vendedor = input()
salarioFixo = float(input())
total_de_vendas = float(input())
porcentagem = (total_de_vendas * 15)/100 
print(f'TOTAL = R$ {(salarioFixo + porcentagem):.2f}')
