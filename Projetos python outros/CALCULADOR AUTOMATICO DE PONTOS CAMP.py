#PROJETO CALCULADOR AUTOMATICO DE PONTOS PARA CAMPEONATOS / XTREINOS E ENTRE OUTRAS COISAS

#Iniciamos criando as variavies que iremos utilizar

#Primeiras variaveis = nome da equipe , posição da equipe, quantidade de kills e numero de salas

#Segundas variaveis = tipo de pontuação exemplo : nfa, lbff, lde, lbr ou outro tipo

#Terceiras variaveis = pontuação por kill, pontuação por posição
#somatório de pts de kill + pontos de posição da sala

#Quartas variaveis = Total de salas (número escolhido maximo 10)

#

# CRIAR MODULO PARA SEGUNDAS VARIAVEIS,REFERENTE AO TIPO DE PONTUAÇÃO, SALVADO AS TABELAS

from time import sleep

#PRIMEIRA PARTE
tipo = str(input('É um campeonato ou xtreino ?')).title().strip()
sleep(2)
'''nome_equipe = str(input('Nome da primeira equipe: ')).upper().strip()
nome_equipe2 = str(input('Nome da segunda equipe: ')).upper().strip()
nome_equipe3 = str(input('Nome da terceira equipe: ')).upper().strip()
nome_equipe4 = str(input('Nome da quarta equipe: ')).upper().strip()
nome_equipe5 = str(input('Nome da quinta equipe: ')).upper().strip()
nome_equipe6 = str(input('Nome da sexta equipe: ')).upper().strip()
nome_equipe7 = str(input('Nome da sétima equipe: ')).upper().strip()
nome_equipe8 = str(input('Nome da oitava equipe: ')).upper().strip()
nome_equipe9 = str(input('Nome da nona equipe')).upper().strip()
nome_equipe10 = str(input('Nome da décima equipe ')).upper().strip()
nome_equipe11 = str(input('Nome da décima primeira equipe ')).upper().strip()
nome_equipe12 = str(input('Nome da décima segunda equipe ')).upper().strip()
sleep(1)
print('Por favor, aguarde...')
sleep(3)
#print(nome_equipe)
#SEGUNDA PARTE
posicao_equipe1 = int(input('Posição da primeira equipe: '))
posicao_equipe2 = int(input('Posição da segunda equipe: '))
posicao_equipe3 = int(input('Posição da terceira equipe: '))
posicao_equipe4 = int(input('Posição da quarta equipe: '))
posicao_equipe5 = int(input('Posição da quinta equipe: '))
posicao_equipe6 = int(input('Posição da sexta equipe: '))
posicao_equipe7 = int(input('Posição da sétima equipe: '))
posicao_equipe8 = int(input('Posição da oitava equipe: '))
posicao_equipe9 = int(input('Posição da nona equipe: '))
posicao_equipe10 = int(input('Posição décima equipe: '))
posicao_equipe11 = int(input('Posição da décima primeira equipe: '))
posicao_equipe12 = int(input('Posição da décima segunda equipe: '))
sleep(1)
print('Por favor, aguarde...')
sleep(3)
#
#TERCEIRA PARTE
kills_equipe1 = int(input('Abates primeira equipe: '))
kills_equipe2 = int(input('Abates segunda equipe: '))
kills_equipe3 = int(input('Abates terceira equipe: '))
kills_equipe4 = int(input('Abates quarta equipe: '))
kills_equipe5 = int(input('Abates quinta equipe: '))
kills_equipe6 = int(input('Abates sexta equipe: '))
kills_equipe7 = int(input('Abates sétima equipe: '))
kills_equipe8 = int(input('Abates oitava equipe: '))
kills_equipe9 = int(input('Abates nona equipe: '))
kills_equipe10 = int(input('Abates décima equipe: '))
kills_equipe11 = int(input('Abates décima primeira equipe: '))
kills_equipe12 = int(input('Abates décima segunda equipe: '))
sleep(1)
print('Por favor, aguarde...')
sleep(3)'''
#
#QUARTA PARTE
quantidade_salas = int(input(f'Qual é o numero de salas do {tipo} ?'))
if quantidade_salas > 1:
    print('Por favor, aguarde...')
    sleep(2)
    while quantidade_salas