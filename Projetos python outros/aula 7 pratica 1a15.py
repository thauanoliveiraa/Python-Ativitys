# nome = input ('Qual é o seu nome ?')
# print (f'Olá muito prazer {nome:^20}!')

# !!!!!!!QUANDO ACABAR UMA PRÁTICA NÃO ESQUEÇA DE NÃO MENCIONA-LAS MAIS PARA NÃO DAR ERRO!!!!!!!!
# PRATICA 1 EX004 (FEITO)

# n1 = int(input('Digite um valor : '))
# n2 = int(input('Digite outro valor : '))
# s = n1+n2
# su = n1-n2
# m = n1*n2
# d = n1/n2
# di = n1//n2
# r = n1%n2
# print (f'A soma de {n1} e {n2} vale {s}')
# print (f'O resultado da sua subtração vale {su}')
# print (f'O resultado da sua multiplicação é {m}')
# print (f'O resultado da sua divisão {d}')
# print (f'Sua divisão inteira é {di}')
# print (f'E o resto da divisão é {r}')

# PRATICA 2 EX005 (FEITO E CORRIGIDO)
# Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e o seu sucessor
# n = int(input('Digite um número :'))
# a = n-1
# su = n+1
# print (f'Analisando o número {n}, pude concluir que o seu antecessor é {a} e o seu sucessor é {su}!')

# PRATICA 3 EX006 (FEITO E CORRIGIDO)
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
# n = int(input('Digite um número : '))
# d = n*2
# t = n*3
# rq = int(n)**0.5
# print = input (f'O seu dobro é {d}, o seu triplo é {t} e a sua raiz quadrada é {rq}')

# PRATICA 4 EX007 (FEITO E CORRIGIDO)
# Desenvolva um programa que leia as duas notas de um aluno, calcule e  mostre a sua media
# print('=====Boletim 2021=====')
# nome = str(input('Nome do aluno :'))
# nota1 = float(input('Avaliação 1 :'))
# nota2 = float(input('Avaliação 2 :'))
# media = float(nota1+nota2)/2
# print (f'A media referente as notas {nota1} e {nota2} do aluno {nome} é {media:.1f}')

# PRATICA 5 EX008 (FEITO E CORRIGIDO)
# Escreva um programa que leia um valor em metros e exiba ele convertido em centímetros e milimetros

# print('=====CONVERSOR METRO PARA KM, HM, DAM, DM, CM, MM=====')
# metro = float(input('Em metros, digite um valor: '))
# cv = int(1000)
# c = str(metro/cv)
# print(f'O valor de {metro}m em quilometros é {c}km')
# cv2 = float(0.01)
# c2 = str(metro*cv2)
# print(f'O valor de {metro}m em hectômetro é {c2}hm')
# cv3 = float(0.1)
# c3 = (metro*cv3)
# print(f'O valor de {metro}m em decâmetro é {c3}dam')
# cv4 = int(10)
# c4 = (metro*10)
# print(f'O valor de {metro} em decímetro é {c4:.0f}dm')
# cv5 = int(100)
# c5 = str(metro*cv5)
# print(f'O valor de {metro}m em centímetros é {c5}cm')
# cv6 = int(1000)
# c6 = str(metro*cv6)
# print(f'O valor de {metro}m em milimetros é {c6}mm')

# PRATICA 6 EX009 (FEITO E CORRIGIDO)
# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

# print('=====TABUADA======')
# nmr = int(input('Digite um número e veja a sua tabuada'))
# print('________________')
# print(f'{nmr} x {1:2} = {nmr*1}')
# print(f'{nmr} x {2:2} = {nmr*2}')
# print(f'{nmr} x {3:2} = {nmr*3}')
# print(f'{nmr} x {4:2} = {nmr*4}')
# print(f'{nmr} x {5:2} = {nmr*5}')
# print(f'{nmr} x {6:2} = {nmr*6}')
# print(f'{nmr} x {7:2} = {nmr*7}')
# print(f'{nmr} x {8:2} = {nmr*8}')
# print(f'{nmr} x {9:2} = {nmr*9}')
# print(f'{nmr} x 10 = {nmr*10}')
# print('________________')

# ABAIXO NAO DEVE SER CONSIDERADO

# print = str(input(f'Você escolheu {nmr} certo?'))
# print = input('Beelezaaa, la vaai a sua tabuada')
# num = str(nmr*1)
# num2 = str(nmr*2)
# num3 = str(nmr*3)
# num4 = str(nmr*4)
# num5 = str(nmr*5)
# num6 = str(nmr*6)
# num7 = str(nmr*7)
# num8 = str(nmr*8)
# num9 = str(nmr*9)
# num10 = str(nmr*10)
# print(f'{nmr} x 1 = {num}')
# tabuada2 = input(str(f'{nmr} x 2 = {num2}'))
# tabuada3 = input(str(f'{nmr} x 3 = {num3}'))
# tabuada4 = input(str(f'{nmr} x 4 = {num4}'))
# tabuada5 = input(str(f'{nmr} x 5 = {num5}'))
# tabuada6 = input(str(f'{nmr} x 6 = {num6}'))
# tabuada7 = input(str(f'{nmr} x 7 = {num7}'))
# tabuada8 = input(str(f'{nmr} x 8 = {num8}'))
# tabuada9 = input(str(f'{nmr} x 9 = {num9}'))
# tabuada10 = input(str(f'{nmr} x 10 = {num10}'))


# PRATICA 7 EX010 (FEITO E CORRIGIDO)
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

# print('=====Conversor de moedas=====')
# real = float(input('Olá, quantos reais você tem na carteira ? R$ '))
# dolar = float(real/5.29)
# euro = float(real/6.50)
# iene = float(real/0.051)
# conversao = float(input(f'De acordo com o valor presente na sua carteira agora no valor de R$ {real:.2f} você pode comprar USD {dolar:.2f} Dólares, Є {euro:.2f} Euros, ¥ {iene:.2f} Ienes'))

# PRATICA 8 EX011 (FEITO E CORRIGIDO)
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²

# largura = float(input('Qual é a altura da parede ?'))
# altura = float(input('Qual é a altura da parede ?'))
# area = float(largura*altura)
# print(f'As dimensões dessa parede são iguais a {largura}x{altura} e a sua area é igual a {area}m²')
# pintar = (area/2)
# print(f'E para pintar essa parede será necessário {pintar}litros de tinta')

# PRATICA 9 EX012 + BONUS (FEITO E CORRIGIDO)
# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

# print('=====DESCONTOS=====')
# print('=====5% DE DESCONTO APENAS HOJE!!!!!=====')
# preço = float(input('Digite o preço do produto : R$'))
# desconto = preço -(preço*5/100)
# print(f'O  valor de {preço} com o desconto de 5% será {desconto}')

# Crie um programa que leia o preço de um produto e calcule o preço dele com desconto para pagamento
# a vista e com aumento para pagamento com cartão(ESCOLHA LIVRE DOS DESCONTOS E AUMENTO)

# print('=====MERCADINHO DO TH=====')
# nome = input('Bem vindo ao Mercadinho do TH, qual é o seu nome ? ')
# print(f'Seja muito bem vindo(a) {nome}')
# valor = float(input('Digite o valor do produto que voce vai comprar : '))
# vista = valor - (valor*20/100)
# cartao = valor + (valor*10/100)
# print(f'Se você pagar a vista receberá 20% de desconto, e o produto que custava {valor:.2f} irá custar {vista:.2f}')
# print(f'Se você pagar no cartao receberá 10% de acrescimo, e o produto que custava {valor:.2f} irá custar {cartao:.2f}')

# PRATICA 10 EX013 (FEITO E CORRIGIDO)
# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento

# print('=====REAJUSTE SALARIAL MICROSOFT=====')
# nome = str(input('Olá, bem vindo a Microsoft, por favor digite seu nome :'))
# print(f'Seja muito bem vindo denovo {nome}')
# salario = float(input('Digite o seu salario atual : R$'))
# reajuste = salario + (salario * 15 / 100)
# print(f'O seu salário no valor de R$ {salario} com um acrescimo de 15% passará a ser R$ {reajuste}, parabens {nome}')
# print('=====REAJUSTE SALARIAL MICROSOFT=====')

# PRATICA 11 EX014 (FEITO E CORRIGIDO)
# Escreva um programa que converta a temperatura digitada em ºC para ºF

# print('=====CONVERSOR DE TEMPERATURAS=====')
# tc = float(input('Digite a temperatura em ºC : '))
# fh = float(tc*1.8+32)
# print(f'A temperatura {tc:.1f}ºC em Fahrenheint é {fh:.1f}ºF')
# k = (tc+273)
# print(f'A temperatura {tc:.1f}ºC em Kelvin é {k:.1f}K')
# print('=====CONVERSOR DE TEMPERATURAS=====')

# PRATICA 12 EX015 (FEITO E CORRIGIDO)
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# print('=====ALUGUEL DE CARROS=====')
# nome = input('Para continuar, digite o seu nome :')
# dias = int(input(f'Olá,{nome},quantos dias foram alugados ?'))
# km = float(input('Quantos quilometros(km) foram rodados ?'))
# total = (dias * 60) + (km * 0.15)
# print(f'Então,{nome},o total que você tem a pagar é R${total:.2f}')
