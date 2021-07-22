import random

print("Bem vindo ao JOKENPO !!!!")

print ('''Suas esolhas possíveis são:
    - pedra
    - papel
    - tesoura''')
vez = 0

while vez < 3 :
    escolha_jogador = input('Qual sua escolha? ').upper()

    possibilidades = ["PAPEL", "PEDRA","TESOURA"]

    escolha_computador = random.choice(possibilidades)
    print(f'O computador escolheu {escolha_computador}')

    if escolha_jogador == escolha_computador:
        print('Deu empate')
        print('-'*30)
    elif escolha_jogador == 'PEDRA' and escolha_computador == 'TESOURA':
        print( '\033[1;34mVocê ganhou!\033[m')
        print('-' * 30)
    elif escolha_jogador == 'PEDRA' and escolha_computador == 'PAPEL':
        print( '\033[1;32mComputador ganhou!\033[m')
        print('-' * 30)
    elif escolha_jogador == 'TESOURA' and escolha_computador == 'PAPEL':
        print( '\033[1;34mVocê ganhou!\033[m')
        print('-' * 30)
    elif escolha_jogador == 'TESOURA' and escolha_computador == 'PEDRA':
        print( '\033[1;32mComputador ganhou!\033[m')
        print('-' * 30)
    elif escolha_jogador == 'PAPEL' and escolha_computador == 'PEDRA':
        print( '\033[1;34mVocê ganhou!\033[m')
        print('-' * 30)
    elif escolha_jogador == 'PAPEL' and escolha_computador == 'TESOURA':
        print( '\033[1;32m computador ganhou!\033[m')
        print('-' * 30)
    vez += 1


print('Fim de Jogo !!!')