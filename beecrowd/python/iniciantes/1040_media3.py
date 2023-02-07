def media_3(A,B,C,D):
    media_total = ((2*A)+(3*B)+(4*C)+(1*D))/(2+3+4+1)
    print(f'Media: {media_total:.1f}')

    if media_total >= 7.0:
        print("Aluno aprovado.")
    elif media_total < 5:
        print("Aluno reprovado.")
        
    elif 5.0 <= media_total <= 6.9:
        print("Aluno em exame.")
        
        nota_exame = float(input())
        print(f'Nota do exame: {nota_exame:.1f}')

        nova_media = (media_total + nota_exame)/2
        
        if nova_media >= 5.0:
            print("Aluno aprovado.")
            print(f'Media final: {nova_media:.1f}')
            
        elif nova_media <= 4.9:
            print("Aluno reprovado.")
            print(f'Media final: {nova_media:.1f}')
    
def main():
    entrada = input().split()
    A,B,C,D = float(entrada[0]), float(entrada[1]), float(entrada[2]), float(entrada[3])
    media_3(A,B,C,D)
if __name__=='__main__':
    main()
