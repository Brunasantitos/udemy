def gastos_viagem(tempo_gasto_viagem,velocidade_media ):
   
    distancia_percorrida = (tempo_gasto_viagem * velocidade_media)/12
    print(f'{distancia_percorrida:.3f}')
    

def main():
    tempo_gasto_viagem = int(input())
    velocidade_media = int(input())
    gastos_viagem(tempo_gasto_viagem, velocidade_media)

if __name__ =='__main__':
    main()
