"""
Enunciado:
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Exemplo de entrada:
576.73

Exemplo de saída:
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01 
"""

# Leitura do valor monetário
valor = float(input())

# Definição das notas e moedas
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Conversão para evitar problemas de precisão com ponto flutuante
valor_int = int(valor * 100 + 0.5)  # Multiplicando por 100 para trabalhar com inteiros

# Cálculo da quantidade de notas
print("NOTAS:")
for nota in notas:
    quantidade_notas = valor_int // int(nota * 100)
    print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")
    valor_int %= int(nota * 100)

# Cálculo da quantidade de moedas
print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = valor_int // int(moeda * 100)
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")
    valor_int %= int(moeda * 100)