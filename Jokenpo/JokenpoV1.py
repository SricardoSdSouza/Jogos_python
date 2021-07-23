import random

print("Bem vindo ao JOKENPO !!!!")

print ('''Suas esolhas possíveis são:
    - pedra
    - papel
    - tesoura''')
vez = 0
computador = 0
jogador = 0

while vez < 3 :
    escolha_jogador = input('Qual sua escolha? ').upper()
    while escolha_jogador not in ["PAPEL", "PEDRA","TESOURA"]:
        escolha_jogador = input('Qual sua escolha? ').upper()

    possibilidades = ["PAPEL", "PEDRA","TESOURA"]

    escolha_computador = random.choice(possibilidades)
    print(f'O computador escolheu {escolha_computador}')

    if escolha_jogador == escolha_computador:
        print('Deu empate')
        print('-'*30)
    elif escolha_jogador == 'PEDRA' and escolha_computador == 'TESOURA':
        print( '\033[1;34mVocê ganhou!\033[m')
        jogador += 1
        print('-' * 30)
    elif escolha_jogador == 'PEDRA' and escolha_computador == 'PAPEL':
        print( '\033[0;30;41mComputador ganhou!\033[m')
        computador += 1
        print('-' * 30)
    elif escolha_jogador == 'TESOURA' and escolha_computador == 'PAPEL':
        print( '\033[1;34mVocê ganhou!\033[m')
        jogador += 1
        print('-' * 30)
    elif escolha_jogador == 'TESOURA' and escolha_computador == 'PEDRA':
        print( '\033[0;30;41mComputador ganhou!\033[m')
        computador += 1
        print('-' * 30)
    elif escolha_jogador == 'PAPEL' and escolha_computador == 'PEDRA':
        print( '\033[1;34mVocê ganhou!\033[m')
        jogador += 1
        print('-' * 30)
    elif escolha_jogador == 'PAPEL' and escolha_computador == 'TESOURA':
        print( '\033[0;30;41m computador ganhou!\033[m')
        computador += 1
        print('-' * 30)
    vez += 1

print(f'O computador acertou {computador} veze(s) e Você acertou {jogador} veze(s)')

if computador == jogador:
    print('\033[1;31;44mHouve empate sem vencedores\033[m')
elif computador > jogador:
    print('\033[7;30;41mO computador venceu!!\033[m')
else:
    print('\033[1;34mVocê venceu!!\033[m')
print('Fim de Jogo !!!')