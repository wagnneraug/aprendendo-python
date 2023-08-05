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

'''
#laços de repetição

repete o mesmo comando várias vezes sem precisar criar códigos enormes

for - para quando sabemos a quantidade exata

while - quando não se sabe o numero de repetições

item - é o comando para destacar o que está sendo repetido.
em casos de listas, a palvra item pode ser trocada por uma versão singular do que está sendo destacado na variavel da lista
a sintatese nesse caso é "for item em coleção"
listas se criam com colchetes
'''

for item in range(1,5): #print apenas de 1-4 pois o ultimo numero não é impresso
    print('chovendo')

for item in range (1,10,2): #o terceiro numero é quantas casas serão puladas nesse caso
    print(item)

nomes = ['wagnner','fernando','dylan','billy']
for nome in nomes:
    print(nome)

valor_max = int(input('Digite um valor max: '))
valor_ini = 1
for numero in range(valor_ini, valor_max + 1):
    print(numero)

'''
Listas

as listas se fazem com colchetes
precos = [01, 02, 03]
           0   1   2
cada numero é um indice, e para colocar no código, coloca com o indice

exemplo de código print(precos[1]) e será impresso o numero 02

print(precos.index(03))
Essa função me traria qual é o numero do indice do valor 03 da lista precos

com um laço de repetição, você pode imprimir tudo o que precisar de uma lista com um codigo menor
exemplo: for preco in precos:
            print(preco)
'''

idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total)