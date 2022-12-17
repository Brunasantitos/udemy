entrada = input().split()
a, b, c = int(entrada[0]), int(entrada[1]), int(entrada[2])
maiorAB = (a + b + abs(a - b)) / 2
maiorXC =(maiorAB + c + abs(maiorAB - c)) / 2
print(f'{maiorXC:.0f} eh o maior')
