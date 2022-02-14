# AULA 9 (FORA DAS ATIVIDADES)
'''frase = 'Curso em video'
print(frase)
frase = '   Curso em video python   '
print(frase[9])
print(frase[0:10])
print(frase[0:10:2])
print(frase[0:9:3])
print(frase[0::3])
print(len(frase))
print(frase.count('e'))
print(frase.find('deo'))
print(frase.find('android'))
print('python' in frase)
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(' '.join(frase))'''

# PRATICA 19 EX022 (FEITO E CORRIGIDO)
# Crie um programa que leia o nome o completo de uma pessoa e mostre :
# 1º O nome com todas as letras maiusculas
# 2º O nome com todas as letras minusculas
# 3º Quantas letras ao todo (sem considerar espaços)
# 4º Quantas letras tem o primeiro nome

# nome = str(input('Qual é o seu nome completo ?')).strip()
# print(f'O seu nome maiusculo fica',nome.upper())
# print(f'O seu nome minusculo fica',nome.lower())
# print(f'O total de caracteres do seu nome são',len(nome.replace(" ","")),'letras')
# nome2 = nome.split()[0]
# print(f'O seu primeiro nome tem',len(nome2),'letras')

# PRATICA 20 EX023 (FEITO E CORRIGIDO)
# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos seus digitos separados
# Exemplo :
# Digite um numero : 1834
# Unidade : 4 / Dezena : 3 / Centena : 8 / Milhar : 1

# Parte 1 com strings

'''algo = str(input('Digite algo'))
print(algo.split())
print('A primeira palavra é',algo.split()[0])
print('A segunda palavra é',algo.split()[1])
print('A terceira palavra é',algo.split()[2])
print('A quarta palavra é',algo.split()[3])'''

# Parte 2 com numeros

# print('=====TUTS TUTS TUTS=====')
# numero = int(input('Digite um numero de 0 a 9999 :'))
# u = numero // 1 % 10
# d = numero // 10 % 10
# c = numero  // 100 % 10
# m = numero // 1000 % 10
# print(f'A sua unidade é {u}')
# print(f'A sua dezena é {d}')
# print(f'A sua centena é {c}')
# print(f'O seu milhar é {m}')
# print('===== TUTS TUTS TUTS=====')

# PRATICA 21 EX024 (FEITO E CORRIGIDO)
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'SANTO'

# Parte 1

'''cidade = str(input('Qual é o nome da cidade ?'))
print(cidade.strip(), 'foi a cidade digitada')
print('De acordo com a análise, a cidade', cidade.find('Santo', 0, 6), 'começa com a palavra Santo')
#find = 'Santo' in cidade
#find = cidade.find('Santo')
#print(f'Logo ele {find} tem a palavra Santo')'''

# Parte 2

# cidade = str(input('Qual é o nome da cidade ?')).strip().upper()
# respost = cidade.find('SANTO', 0,6)
# print(f'{cidade} foi a cidade digitada,')
# if respost == 0:
   # print(f'logo,{cidade} começa com SANTO.')
# elif respost == -1:
   # print(f'mas,{cidade} não começa com SANTO.')

# PRATICA 22 EX025 (FEITO)
# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome

# nome = str(input('Qual é o seu nome todo ?'))
# nome2 = nome.upper()
# print('Seu nome todo é', nome2.strip(),',')
# find = nome2.find('SILVA')
# if find == -1:
    # print('más, ele não possui SILVA em nenhum momento')
# elif find != -1:
    # print('disso, percebemos que ele possui SILVA')

# PRATICA 23 EX026 (FEITO E CORRIGIDO)
# Faça um programa que leia uma frase pelo teclado e mostre :
# 1º Quantas vezes aparece a letra 'A'
# 2º Em que posição ela aparece pela primeira vez
# 3º Em que posição ela aparece a ultima vez

# frase = str(input('Digite uma frase :D')).strip()
# frase2 = frase.upper()
# um = frase2.count('A')
# print(f'Na frase {frase2},a letra A aparece {um} vez(es)')
# frase3 = frase2.find('A')
# print(f'A letra A aparece pela primeira vez na posição {frase3}')
# frase4 = frase2.rfind('A')
# print(f'A letra A aparece pela ultima vez na posição {frase4}')

# PRATICA 24 EX027 (FEITO E CORRIGIDO)
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o ultimo nome separadamente
# EXEMPLO : Ana maria de souza
# Primeiro nome = Ana
# Ultimo nome = Souza

# nome = str(input('Qual é o seu nome completo ?')).strip().lower().title() # <<< AGORA VOCE APRENDEU QUE PODE SE FAZER ISSO
# lista = nome.split()[0]
# lista2 = nome.split()[-1]
# print(f'O seu nome é {nome},\nlogo, o seu primeiro nome é {lista}\ne o seu ultimo nome é {lista2}')











