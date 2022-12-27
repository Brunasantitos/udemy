def TempoIdade(i):
    idade = i // 365
    mes = (i % 365)//30
    dia = (i % 365)%30
    print(f'{idade} ano(s)')
    print(f'{mes} mes(es)')
    print(f'{dia} dia(s)')

def main():
    entrada = int(input())
    TempoIdade(entrada)


if __name__=='__main__':
    main()
