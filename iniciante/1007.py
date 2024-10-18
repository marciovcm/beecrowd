"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada

O arquivo de entrada contém 4 valores inteiros.
Saída

Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
"""
# Recebe os quatro valores e salva cada um em uma variável
A = int(input())
B = int(input())
C = int(input())
D = int(input())

# Imprime na tela o texto "DIFERENCA =" seguido do resultado pedido no exercício
print(f'DIFERENCA = {A * B - C * D}')