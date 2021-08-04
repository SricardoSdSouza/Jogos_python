import random
print('--- BEM VINDO A BATALHA POKEMON ---')

vida_inimigo = 50
vida = 50
while vida > 0 and vida_inimigo > 0:
    print('\033[1;31m*\033[m' * 50)
    print('Lista de ataques possíveis do Pikachu')
    print('''
        a - choque do trovão
        b - cabeçada
        c - trovão megamasterblaster
    ''')
    print('\033[1;34m*\033[m' * 50)
    ataque = input('Escolha qual ataque você que usar: ').lower().strip()
    print('\033[1;31m*\033[m'*50)
    while ataque not in ('a','b','c'): # testando para que seja digitado somente (a,b,ou c)
        print('Escolha um ataque válido')
        ataque = input('Escolha qual ataque você que usar: ').lower().strip()

    if ataque == 'a':
        print('Você usou o choque do trovão')
        vida_inimigo -= 12
    elif ataque == 'b':
        print('Você usou cabeçada')
        vida_inimigo -= 7
    elif ataque == 'c':
        print('Você usou megamasterblaster')
        vida_inimigo -= 18


    print(f'Avida do Inimigo agora é : {vida_inimigo}')

    if vida_inimigo <= 0:
        break

    print('O Charmander te ataca')
    ataque_inimigo_chance = random.randint(0,1)
    print('\033[1;31m*\033[m'*50)

    if ataque_inimigo_chance == 1:
        print('Chamander usa a bola de fogo')
        vida -= 15
    else:
        print('Chamander usa arranhão')
        vida -= 8
    print(f'Avida do PIKACHU agora é : {vida}')

if vida > 0 :
    print(f'\033[0;30;42mParabéns, o PIKACHU WIN !!!!\033[m')
else:
    print(f'\033[0;30;41mO CHARMANDER WIN, PIKACHU lost !!!!\033[m')


