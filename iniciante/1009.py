"""
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
Entrada

O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.
Saída

Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

# Entrada de dados
# Uso do caster "float" na linha 4 e 5 para forçar a entrada seja float
nome = input() 
salario = float(input()) 
total_vendas = float(input())

# Calculo do total recebido pelo vendedor
total_recebido = salario + (total_vendas*0.15)

# Mostrando ao usuário com duas casas decimais com o ".2f"
print(f"TOTAL = R$ {total_recebido:.2f}")