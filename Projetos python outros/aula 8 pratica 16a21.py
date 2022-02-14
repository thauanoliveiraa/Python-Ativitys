# AULA 8  (FORA DAS ATIVIDADES)
# Faça um programa que leia um número e mostre a sua raiz quadrada

import math
num = int(input('Digite um número e descubra a sua raiz quadrada :D'))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.2f}'
import math
num = int(input('Digite um numero e descubra a sua raiz quadrada :D'))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.ceil(raiz):.2f}')
from math import ceil,sqrt,floor
num = int(input('Digite um numero e descubra a sua raiz quadrada :D'))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {math.floor(raiz:.2f)}')
import random
num = random.randint(1, 10)
print(num)
import emoji

# PRATICA 13 EX016 (FEITO E CORRIGIDO)
# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira
# EX : Digite um numero : 6.127 / O numero 6.127 tem a parte inteira 6

 import math
 num = float(input('Digite um número : '))
 calculo = math.trunc(num)
 print(f'O número {num:.3f} tem a parte inteira {calculo}')

# PRATICA 14 EX017 (FEITO E CORRIGIDO)
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa

 import math
 catop = float(input('Digite o comprimento do cateto oposto'))
 catadj = float(input('Digite o comprimento do cateto adjacente'))
 calculo = (math.pow(catop, 2)+math.pow(catadj, 2))
 hipotenusa = math.sqrt(calculo)
 print(f'De acordo com os valores do cateto oposto {catop} e do cateto adjacente {catadj}\no valor da hipotenusa é {hipotenusa}')

# PRATICA 15 EX018 (FEITO E CORRIGIDO)
# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

 import math
 angulo = int(input('Qual é o valor do angulo ?'))
 sen = math.sin(math.radians(angulo))
 cos = math.cos(math.radians(angulo))
 tan = math.tan(math.radians(angulo))
 print(f'De acordo com o valor do angulo {angulo}\nO valor do seu seno é {sen:.2f}\nDo seu cosseno é {cos:.2f}\nDa sua tangente é {tan:.2f}')

# PRATICA 16 EX019 (FEITO E CORRIGIDO)
# Um professor quer sortear quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

 import random
 aluno1 = str(input('Qual é o nome do primeiro aluno ?'))
 aluno2 = str(input('Qual é o nome do segundo aluno ?'))
 aluno3 = str(input('Qual é o nome do terceiro aluno ?'))
 aluno4 = str(input('Qual é o nome do quarto aluno ?'))# alunos = [aluno1, aluno2, aluno3, aluno4]
 sorteio = random.choice(alunos
 print(f'Dos alunos {aluno1,aluno2,aluno3,aluno4} o escolhido para apagar o quadro foi {sorteio}')

# PRATICA 17 EX020 (FEITO E CORRIGIDO)
# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

 import random
 aluno1 = str(input('Qual é o nome do primeiro aluno ?'))
 aluno2 = str(input('Qual é o nome do segundo aluno ?'))
 aluno3 = str(input('Qual é o nome do terceiro aluno ?'))
 aluno4 = str(input('Qual é o nome do quarto aluno ?'))
 alunos = [aluno1, aluno2, aluno3, aluno4]
 oap = random.sample(alunos, 4)
 print(f'A ordem de apresentação será {oap}!')

# PRATICA 18 EX021 (NÃO FEITO >> BUGADO)
# Faça um programa em python que abra e reproduza o audio de um arquivo mp3

import playsound
import ctypes
playsound.playsound('homenagem.mp3')

import pyglet#
source = pyglet.media.load('homenagem.mp3')

music = pyglet.resource.media('\Users\Th\AppData\Local\Programs\Python\Python36\Lib\site-packages\pyglet\homenagem.mp3')
music.play()
pyglet.app.run()

from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_mp3('homenagem.wav')
play(song)

import pygame
from pygame import mixer
mixer.init()
mixer.music.load('homenagem.wav')#
mixer.music.play()
input('Agora você escuta?')

import Play_mp3
filename = ('homenagem.mp3')
Play_mp3.play('homenagem.mp3')

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('homenagem.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy:pass

