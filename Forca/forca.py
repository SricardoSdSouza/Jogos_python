import random
palavras = ['COMPUTADOR', 'CACHORRO','MULHER','BRASIL','PAREDE','GALINHA','PERIQUITO','CANARINHO','FOGO','MADEIRA','PIPOCA',
            'RADIO','VIDEO','SOFA','IMPRESSORA','COPO']
palavra = random.choice(palavras)
#print(palavra)
tentativas = 0
chances = 5 #len(palavra)
letras_escolhidas = []
estado_atual = ['_'] * len(palavra)
print('BEM VINDO AO JOGO DA FORCA')
print('Seu objetivo é tentar acertar a palavra escolhida pelo computador!!')
print(f'Você terá {chances} chances!!!!')
while tentativas < chances and ''.join(estado_atual) != palavra:
    letra = input('\nQual letra você quer tentar? : ').upper()
    while letra in letras_escolhidas:
        print('\033[7;30mVocê ja escolheu esta letra, tente outra!!!\033[m')
        letra = input('\nQual letra você quer tentar? : ').upper()
    letras_escolhidas.append(letra)
    if letra in palavra.upper():
        print('Parabéns você acertou a letra !!')
        for i in range(len(palavra)):
            if letra == palavra[i]:
                estado_atual[i] = letra
    else:
        print('Que pena vc \033[1;31mERROU!!!\033[m')
        tentativas += 1

    print(f'Você fez {tentativas} tentativas, ainda tem {chances - tentativas},tentativas !!')

    print(f'Este é o estado atual {estado_atual}')

    print(f'\033[1;34mAs letras que você escolheu foram :\033[m {letras_escolhidas}')

if tentativas == chances:
    print('!' * 50)
    print('\033[0;30;41mGame over, esgotaram suas tentativas !!!! :( \033[m')
    print('!' * 50)
else:
    print('*' * 30)
    print('\033[0;36mYou WIN !!!! Congratulations\033[m')
    print('*' * 30)
print(f'A palvra era {palavra}')