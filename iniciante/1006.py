"""
Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
Entrada

O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).
Saída

Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".
"""
# Recebemos os 3 valores de entrada, já utilizando a função float para convertê-los, já que em python todo input retorna uma string
A = float(input())
B = float(input())
C = float(input())

# Em seguida, calculamos a média utilizando os pesos descritos no exercício e por fim a imprimimos com apenas uma casa decimal
media = (A*2 + B*3 + C*5)/10

print(f"MEDIA = {media:.1f}")