'''
#variaveis

> numeros - números inteiros ou decimais.
int #numero inteiro
float #decimal

> valores boleanos - representa um valor verdade ou falso (true or false)
True
False

> strings - são textos que formam frases ou conjuntos de palavras, sempre entre aspas
nome = 'Wagnner Augusto'
'''

salario_mensal = input('Qual seu salário mensal? ')
horas_trabalhadas = input('Quais foram as horas trabalhadas? ')
valor_hora = int(salario_mensal) / int(horas_trabalhadas)
print(valor_hora)