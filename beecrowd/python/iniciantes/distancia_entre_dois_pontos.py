primeira_entrada = input().split()
x1, y1 = float(primeira_entrada[0]), float(primeira_entrada[1])
segunda_entrada = input().split()
X2, Y2 = float(segunda_entrada[0]), float(segunda_entrada[1])
import math
formula = (((X2 - x1)**2)+((Y2 - y1)**2))
print(f'{math.sqrt(formula):.4f}')
