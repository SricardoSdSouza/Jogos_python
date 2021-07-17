import random

print("Bem vindo ao JOKENPO !!!!")

print ('''Suas esolhas possíveis são:
    - pedra
    - papel
    - tesoura''')

escolha_jogador = input('Qual sua escolha? ')

possibilidades = ["papel", "pedra","tesoura"]

escolha_computador = random.choice(possibilidades)
print(f'O computador escolheu {escolha_computador}')
if escolha_jogador == escolha_computador:
    print('Deu empate')
elif escolha_jogador == 'pedra' and escolha_computador == 'tesoura':
    print( 'Você ganhou!')
elif escolha_jogador == 'pedra' and escolha_computador == 'papel':
    print( 'Computador ganhou!')

elif escolha_jogador == 'tesoura' and escolha_computador == 'papel':
    print( 'Você ganhou!')
elif escolha_jogador == 'tesoura' and escolha_computador == 'pedra':
    print( 'Computador ganhou!')

elif escolha_jogador == 'papel' and escolha_computador == 'pedra':
    print( 'Você ganhou!')
elif escolha_jogador == 'papel' and escolha_computador == 'tesoura':
    print( 'Computador ganhou!')