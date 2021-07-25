import random
palavras = ['computador', 'cachorro','mulher','Brasil','parede','galinha','periquito','canarinho','fogo','madeira','pipoca']
palavra = random.choice(palavras)
#print(palavra)
tentativas = 0
chances = len(palavra)
letras_escolhidas = []
estado_atual = ['_'] * len(palavra)
print('BEM VINDO AO JOGO DA FORCA')
print('Seu objetivo é tentar acertar a palavra escolhida pelo computador!!')
print(f'Você terá {chances} chances!!!!')
while tentativas < chances and ''.join(estado_atual) != palavra:
    letra = input('\nQual letra você quer tentar? : ')
    while letra in letras_escolhidas:
        print('Você ja escolheu esta letra, tente outra!!!')
    letras_escolhidas.append(letra)
    if letra in palavra:
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
    print('\033[7;30mGame over, esgotaram suas tentativas !!!! :(\033[m')
else:
    print('\033[0;31;44mYou WIN !!!! Congratulations\033[m')
print(f'A palvra foi {palavra}')