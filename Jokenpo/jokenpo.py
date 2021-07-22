import random

print("Bem vindo ao JOKENPO !!!!")

print ('''Suas esolhas possíveis são:
    - pedra
    - papel
    - tesoura''')

escolha_jogador = input('Qual sua escolha? ').upper()

possibilidades = ["PAPEL", "PEDRA","TESOURA"]

escolha_computador = random.choice(possibilidades)
print(f'O computador escolheu {escolha_computador}')
if escolha_jogador == escolha_computador:
    print('Deu empate')
elif escolha_jogador == 'PEDRA' and escolha_computador == 'TESOURA':
    print( '\033[1;34mVocê ganhou!\033[m')
elif escolha_jogador == 'PEDRA' and escolha_computador == 'PAPEL':
    print( 'Computador ganhou!')

elif escolha_jogador == 'TESOURA' and escolha_computador == 'PAPEL':
    print( 'Você ganhou!')
elif escolha_jogador == 'TESOURA' and escolha_computador == 'PEDRA':
    print( 'Computador ganhou!')

elif escolha_jogador == 'PAPEL' and escolha_computador == 'PEDRA':
    print( '\033[1;34mVocê ganhou!\033[m')
elif escolha_jogador == 'PAPEL' and escolha_computador == 'TESOURA':
    print( 'Computador ganhou!')