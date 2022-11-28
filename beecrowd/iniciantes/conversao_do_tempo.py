def tempo(tempo_para_horas):
    horas = (tempo_para_horas//3600)
    minutos = (tempo_para_horas%60)//60
    segundos = (tempo_para_horas%60)

    print(horas)
    print(minutos)
    print(segundos)

def main():
    tempo_para_horas = int(input("Informe um valor: "))
    tempo(tempo_para_horas)

if __name__=='__main__':
    main()