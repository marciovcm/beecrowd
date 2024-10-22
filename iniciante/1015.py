"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia = sqrt((x2 - x1)^2 + (y2 - y1)^2)

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.
"""
import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def quadrado_perfeito(a, b):
    return b**2 - 2*b*a + a**2

resultado = math.sqrt(quadrado_perfeito(x1, x2) + quadrado_perfeito(y1, y2))

print(f'{resultado:.4f}')
