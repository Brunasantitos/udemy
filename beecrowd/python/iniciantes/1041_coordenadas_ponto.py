def pontos(x,y):
    if x == y == 0:
        print("Origem")
    elif x>0 and y<0:
        print("Q4")
    elif x>0 and y>0:
        print("Q1") 
    elif x<0 and y>0:
        print("Q2")
    elif x<0 and y<0:
        print("Q3")
    elif x==0 and y<0:
        print("Eixo Y")
    elif x==0 and y>0:
        print("Eixo Y")
    elif x<0 and y==0:
        print("Eixo X")
    elif x>0 and y==0:
        print("Eixo X")
    

def main():
    entrada = input().split()
    X,Y = float(entrada[0]), float(entrada[1])

    pontos(X,Y)

if __name__=='__main__':
    main()
