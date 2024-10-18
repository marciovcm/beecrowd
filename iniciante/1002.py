"""
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
Entrada

A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
Saída

Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
"""
# Lê o valor do raio pela entrada padrão
r = float(input())

# Calcula o valor conforme a fórmula fornecida
area = 3.14159*(r**2)

# Imprime o valor na saída padrão com arredondamento de 4 casas decimais
print(f'A={area:.4f}')