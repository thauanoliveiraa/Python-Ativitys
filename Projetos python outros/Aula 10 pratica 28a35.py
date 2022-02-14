# AULA 10 (FORA DAS ATIVIDADES)
'''nome = str(input('Qual é o seu nome ?')).strip().title()
if nome =='Thauan':
    print(f'Seja bem vindo GameBoss {nome}')
else:
    print(f'Seja bem vindo {nome}')
print(';D')

nota = float(input('Qual foi a sua primeira nota ?'))
nota2 = float(input('E a segunda nota ?'))
media = (nota+nota2)/2
if media >= 6.0:
    print(f'Você passou com a media igual a {media} :D')
else:
    print(f'Infelizmente com a media {media} você não passou, estude mais!')
print('---BOLETIM---')'''

# PRATICA 25 EX028 (FEITO E CORRIGIDO)
# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario
# tentar descobrir qual foi o numero escolhido pelo computador
# O programa deverá escrever na tela se o usuario venceu ou perdeu

'''import random
from time import sleep
print('Pensando em um número entre 0 e 5...')
sleep(2)
pensei = str(input('Ja pensei, você acha que consegue acertar ?')).strip().lower()
n = random.randint(0,5)
print('Hmmm...')
sleep(2)
r = int(input('Então, qual é o número ?'))
print('Processando...')
sleep(2)
if r == n:
    print('Afff, você acertou =)')
else:
    print(f'Ha-Ha-Ha você errou, o número era {n}!!!')'''

# PRATICA 26 EX029 (FEITO E CORRIGIDO)
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar o limite de 80 km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite

'''from termcolor import colored
from time import sleep
print(colored('===== RADAR ELETRÔNICO =====', 'red'))
velocidade = int(input(colored('Qual era a velocidade do carro ?', 'green')))
print(colored('PROCESSANDO...', 'red'))
sleep(2)
if velocidade > 80:
    print(colored('Infelizmente você foi multado', 'red'))
    v = (velocidade-80)
    m = float(v * 7)
    print(colored(f'E com a velocidade igual a {velocidade}km/h você vai ter que pagar\nR$ {m:.2f} de multa', 'red'))
else:
    print(colored('Obrigado por respeitar as normas de trânsito e seguança!\nTenha um bom dia :D', 'green'))
print(colored('===== RADAR ELETRÔNICO =====', 'red'))

# PRATICA 27 EX030 (FEITO E CORRIGIDO)
# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR

'''from time import sleep
from termcolor import colored
print(colored('===== PAR OU IMPAR :D =====', 'red'))
numero = int(input(colored('Digite um numero e irei mostrar se ele é par ou impar', 'green')))
par_e_impar = numero % 2
print(colored('PROCESSANDO...', 'red'))
sleep(2)
if  par_e_impar == 0:
    print(colored(f'De acordo com a análise,\no número {numero} é PAR', 'green'))
else:
    print(colored(f'De acordo com a análise,\no número {numero} é IMPAR', 'red'))
print(colored('===== PAR OU IMPAR :D =====', 'red'))'''

# Parte 2
#
from time import sleep
from termcolor import colored
nome = str(input(colored('Qual o seu nome ?', 'green'))).strip().lower()
n1 = str('thxx')
e = str('Exibir senha').strip().lower()
g = str('Guardar senha').strip().lower()
if nome == n1:
    print(colored(f'Seja bem vindo de volta {nome}', 'red'))
    sleep(1)
    print(colored(f'Oque gostaria de fazer {nome}?', 'red'))
    sleep(1)
    print('Logar')
    print('Deslogar')
    print('Criar nova senha')
    fz = int(input(' '))
else:
    print(colored(f'Seja bem vindo {nome}', 'blue'))
#senha = int(input('Digite uma senha'))
#while senha == '123456':
    #print('Senha muito simples por favor insira outra')'''
    #repeat()

# PRATICA 28 EX031 (FEITO E CORRIGIDO)
# Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem
# Cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas

'''from time import sleep
from termcolor import colored
print(colored('====== CALCULO AEREO =====', 'red'))
sleep(1)
nome = str(input(colored('Qual é o seu nome ?', 'red'))).strip().title()
sleep(1)
print(colored(f'Seja muito bem vindo a THAIRLINES {nome}', 'red'))
sleep(1)
distancia = int(input(colored('Qual é a distância da viagem ?', 'red')))
sleep(1)
print(colored('Calculando...', 'red'))
sleep(2)
print(colored('Esse processo pode levar algum tempo...', 'red'))
sleep(2)
curta = float(0.50 * distancia)
longa = float(0.45 * distancia)
if distancia <= 200:
    print(colored(f'Como a distância é {distancia}km', 'red'))
    print(colored(f'A passagem vai custar R$ {curta:.2f}', 'red'))
if distancia > 200:
    print(colored(f'A passagem vai custar R$ {longa:.2f}', 'red'))
sleep(1)
print(colored('===== CALCULO AEREO =====', 'red'))'''

# PRATICA 29 EX032 (FEITO E CORRIGIDO)
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

'''from datetime import date
from time import sleep
from termcolor import colored
ano = int(input(colored('Digite o ano ou digite 0 para o ano atual:', 'red')))
#calculo_par = ano % 4
print(colored('Analisando...', 'red'))
sleep(1)
print(colored('Esse processo pode demorar um pouco, por favor aguarde...', 'red'))
sleep(2)
#print(colored(f'{calculo:.0f}', 'green'))
if ano ==0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print(colored(f'Após analisar o ano {ano}, pode-se concluir que é um ano bissexto', 'red'))
else:
    print(colored(f'Após analisar o ano {ano}, pode-se concluir que não é um ano bissexto', 'red'))

# PRATICA 30 EX033 (FEITO E CORRIGIDO)
# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor'''

'''from time import sleep
from termcolor import colored
n1 = int(input(colored('Digite um número :' ,'red')))
print(colored('Processando...', 'blue'))
sleep(1)
n2 = int(input(colored('Digite um segundo número :', 'red')))
print(colored('Processando...', 'blue'))
sleep(1)
n3 = int(input(colored('Digite um terceiro número :' ,'red')))
print(colored('Analisando...', 'blue'))
sleep(2)
if n1 < n2 and n1 < n3:
    print(colored(f'De acordo com a analise o número {n1} é menor', 'red'))
if n2 < n3 and n2 < n1:
    print(colored(f'De acordo com a analise o número {n2} é menor', 'red'))
if n3 < n1 and n3 < n2:
    print(colored(f'De acordo com a analise o número {n3} é menor', 'red'))
if n1 > n2 and n1 > n3:
    print(colored(f'De acordo com  a analise o número {n1}  é maior', 'red'))
if n2 > n3 and n2 > n1:
    print(colored(f'De acordo com  a analise o número {n2} é maior', 'red'))
if n3 > n2 and n3 > n1:
    print(colored(f'De acordo com a analise o número {n3} é maior', 'red'))'''

# NAO ESTA ERRADO MAS DESONSIDERE
'''if n1 > n2:
    print(colored(f'De acordo com a analise o número {n1} é maior que o número {n2}', 'blue'))
else:
    print(colored(f'De acordo com a analise o número {n1} é menor o número {n2}', 'blue'))
if n2 > n3:
    print(colored(f'De acordo com a analise o número {n2} é maior que o número {n3}', 'blue'))
else:
    print(colored(f'De acordo com a analise o número {n2} é menor que o número {n3}', 'blue'))
if n3 > n1:
    print(colored(f'De acordo com a analise o número {n3} é maior que o número {n1}', 'blue'))
else:
    print(colored(f'De acordo com a analise o número {n3} é menor que o número {n1}', 'blue'))'''

# PRATICA 31 EX034 (FEITO E CORRIGIDO)
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salarios superiores a R$ 1250, calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%

'''from time import sleep
from termcolor import colored
print(colored('===== MICROSOFT BRASIL =====', 'red'))
nome = str(input(colored('Olá, qual é o seu nome ?', 'red'))).strip().title()
print((colored(f'Seja Bem-vindo {nome}', 'red')))
sleep(1)
salario = float(input(colored(f'Qual é o seu salário {nome} ?', 'red')))
calculo = salario + (salario*10/100)
calculo2 = salario + (salario*15/100)
sleep(1)
print(colored('Processando...', 'red'))
sleep(2)
print(colored('Esse processo pode demorar um pouco...', 'red'))
sleep(2)
if salario > 1250:
    print(colored(f'De acordo com o seu salário no valor de R$ {salario:.2f} {nome},\ncom o aumento de 10% ele passará a ser no valor de R$ {calculo:.2f}', 'red'))
else:
    print(colored(f'De acordo com o seu salário no valor de R$ {salario:.2f} {nome},\ncom o aumento de 10% ele passará a ser no valor de R$ {calculo2:.2f}', 'red'))'''

# PRATICA 32 EX035 (FEITO E CORRIGIDO)
# Desenvolva um programa que leia o comprimento de 3 retas que diga se ele pode ou não formar um triangulo

'''from time import sleep
from termcolor import colored

print(colored('===== DESIGUALDADE TRIANGULAR =====', 'red'))
reta1 = float(input(colored('Digite o comprimento da primeira reta em cm', 'red')))
sleep(1)
reta2 = float(input(colored('Digite o comprimento da segudna reta em cm', 'red')))
sleep(1)
reta3 = float(input(colored('Digite o comprimento da terceira reta em cm', 'red')))
sleep(1)
print(colored('Processando...', 'red'))
sleep(2)
#calculo1 = (reta1 + reta2)
#calculo2 = (reta2 + reta3)
#if reta1 > reta2:
    #print(f'{calculo1}')
#else:
    #print(f'')
if reta1 + reta2 > reta3 and reta2 < reta3 + reta1:
    print(colored(f'Após processar, pude concluir que as medidas da reta 1 igual a {reta1}, da reta 2 igual a {reta2} e da reta 3 igual a {reta3} podem sim formar um triângulo', 'red'))
else:
    print(colored(f'Após processar, pude concluir que as medidas da reta 1 igual a {reta1}, da reta 2 igual a {reta2} e da reta 3 igual a {reta3} não podem formar um triângulo', 'red'))'''
#if calculo2 > reta1:
    #print(colored())




###############################################################################################################
# REMAKE APAGAR DEPOIS
# PRATICA 25 EX028 (FEITO)
# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario
# tentar descobrir qual foi o numero escolhido pelo computador
# O programa deverá escrever na tela se o usuario venceu ou perdeu

'''from time import sleep
from termcolor import colored
import random

nome = str(input(colored('Olá, qual é o seu nome ?', 'red'))).strip().lower()
print(colored(f'Seja bem vindo {nome}', 'red'))
sleep(1)
print(colored('Pensando em um número entre 0 e 5', 'red'))
sleep(2)
print(colored('Pensando...', 'red'))
sleep(1)
sorteio = random.randint(0,5)
pensei = str(input(colored(f'Ja pensei, acha que consegue acertar {nome}?', 'red'))).strip().title()
print(colored('Entao...', 'red'))
sleep(2)
resposta = int(input(colored('Qual é o numero ?', 'red')))
if resposta == sorteio:
    print(colored('Aff, você acertou', 'red'))
else:
    print(colored('Voce errou hehehe, eu ganhei', 'red'))
if pensei == Sim:
    print(colored('Beleza, então qual é o número ?', 'red'))
else:
    print(colored('Aaah que pena, então acabamos por aqui :(', 'red'))'''

# PRATICA 26 EX029 (FEITO)
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar o limite de 80 km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite

'''from termcolor import colored
from time import sleep

print(colored('===== DETRAN BAHIA =====', 'red'))
nome = str(input(colored('Olá, qual é o seu nome completo?', 'red'))).strip().title()
print(colored(f'Seja muito bem vindo ao Detran Bahia {nome}','red'))
sleep(1)
print(colored('Processando...', 'red'))
sleep(2)
velocidade = int(input(colored('Qual era a velocidade do veiculo ?', 'red')))
calculo1 = (velocidade - 80)
calculo2 = float(calculo1 * 7.00)
print(colored('Processando...', 'red'))
sleep(2)
if velocidade > 80:
    print(colored(f'Infelizmente você foi multado {nome} e a multa custará R$ {calculo2:.2f}', 'red'))
if velocidade <=80:
    print(colored(f'Parabéns {nome}, obrigado por respeitar as leis de transito', 'red'))'''

# PRATICA 27 EX030
# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR

'''from termcolor import colored
from time import sleep

print(colored('===== PAR OU IMPAR =====', 'red'))
sleep(1)
numero = int(input(colored('Digite um número e irei mostrar se ele é par ou impar', 'red')))
calculo = numero % 2
sleep(1)
print(colored('Processando...', 'red'))
sleep(2)
if calculo == 0:
    print(colored(f'Após o processamento, tive a conclusão que o número {numero} é PAR', 'red'))
else:
    print(colored(f'Após o processamento, tive a conclusão que o número {numero} é IMPAR', 'red'))'''


# PRATICA 28 EX031 (FEITO)
# Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem
# Cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas

'''from termcolor import colored
from time import sleep

print(colored('Welcome to...', 'red'))
sleep(1)
print(colored('T Airlines, live your dream', 'red'))
sleep(2)
distancia = int(input(colored('Qual é a distância da viagem em km ?', 'red')))
sleep(1)
print(colored('Processando...', 'red'))
sleep(2)
print(colored('Esse processo pode demorar um pouco', 'red'))
sleep(1)
calculo1 = float(distancia * 0.50)
calculo2 = float(distancia * 0.45)
if distancia <= 200:
    print(colored(f'De acordo com a análise com a distância de {distancia}km a passagem custará R$ {calculo1:.2f}', 'red'))
if distancia > 200:
    print(colored(f'De acordo com a análise com a distância de {distancia}km a passagem custará R$ {calculo2:.2f}', 'red'))'''

# PRATICA 29 EX032 (FEITO)
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

'''from termcolor import colored
from time import sleep

print(colored('Bem vindo a calculadora de ano bissexto', 'blue'))
sleep(1)
print(colored('Por favor aguarde...', 'blue'))
sleep(2)
ano = int(input(colored('Qual é o ano ?', 'blue')))
calculo = int(ano % 4)
sleep(1)
print(colored('Analisando...', 'blue'))
sleep(2)
if calculo == 0:
    print(colored(f'Após a análise pude concluir que o ano {ano} é bissexto', 'blue'))
else:
    print(colored(f'Após a análise pude concluir que o ano {ano} nao é bissexto', 'blue'))'''

# PRATICA 30 EX033 (FEITO)
# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

'''from termcolor import colored
from time import sleep

n1 = int(input(colored('Digite um número', 'blue')))
sleep(1)
n2 = int(input(colored('Digite outro número', 'blue')))
sleep(1)
n3 = int(input(colored('Digite mais um número', 'blue')))
sleep(2)
print(colored('Analisando...'))
sleep(1)
if n1 > n2:
    print(f'De acordo com a analise o número {n1} é maior que o número {n2}')
else:
    print(f'De acordo com a analise o número {n1} é menor que o número {n2}')
if n1 > n3:
    print(f'De acordo com a analise o número {n1} é maior que o número {m3}')
else:
    print(f'De acordo com a analise o número {n1} é menor que o número {n3}')
if n2 > n1:
    print(f'De acordo com a analise o número {n2} é maior que o número {n1}')
else:
    print(f'De acordo com a analise o número {n2} é menor que o número {n1}')
if n3 > n2:
    print(f'De acordo com a analise o número {n3} é maior que o número {n2}')
else:
    print(f'De acordo com a analise o número {n3} é menor que o número {n2}')'''

# PRATICA 31 EX034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salarios superiores a R$ 1250, calcule um aumento de 10%
# Para os inferiores ou iguais o aumento é de 15%

'''salario = float(input('Qual é o seu salario ?'))
calculo1 = salario + (salario*10/100)
calculo2 = salario + (salario*15/100)
if salario >= 1250:
    print(f'O seu salario atual que era de R$ {salario:.2f}  passa a ser de R$ {calculo1:.2f}')
if salario < 1250:
    print(f'O seu salario atual que era de R$ {salario:.2f} passa a ser de R$ {calculo2:.2f}')'''

# REMAKE COMPLETO


