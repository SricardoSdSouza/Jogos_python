import random

print("Bem  vindo ao Jogo da Velha")
print("Tente vencer o computador se for capaz!!!")
print("Você ganha se conseguir uma linha ou uma coluna ou uma diagonal no grid com o mesmo símbolo")
print("Você precisa escolher uma posição no grid para marcar sua jogada, de acordo com a numeração\n")
print("_ _ _")
print("_ _ _")
print("_ _ _")
print("Escolha os números de acordo com o Grid abaixo")
print("1 2 3")
print("4 5 6")
print("7 8 9")
qtda_escolhas = 0
def verifica_grid(grid,jogada):
    '''Testando as linhas'''
    if grid[0] == jogada and grid[1] == jogada and grid[2] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    if grid[3] == jogada and grid[4] == jogada and grid[5] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    if grid[6] == jogada and grid[7] == jogada and grid[8] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    '''Testando as colunas'''
    if grid[0] == jogada and grid[3] == jogada and grid[6] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    if grid[1] == jogada and grid[4] == jogada and grid[7] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    if grid[2] == jogada and grid[5] == jogada and grid[8] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    '''Testando as diagonais'''
    if grid[0] == jogada and grid[4] == jogada and grid[8] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    if grid[2] == jogada and grid[4] == jogada and grid[6] == jogada:
        if jogada == "x":
            return 1
        else:
            return 2
    return 0

def imprime_grid(grid):
    print('O status do grid é\n')
    for indice in range(len(grid)):
        print(grid[indice], end=" ")
        if indice == 2 or indice == 5 or indice == 8:
            print("")

grid = ["-"] * 9

while True:
    escolha = int(input("Qual é a sua escolha: "))
    '''Testando se a escolha do usuário ja existe'''
    while grid[escolha - 1] != "-":
        print('Sua escolha já existe, tente outra!!, veja suas opções')
        imprime_grid(grid)
        escolha = int(input("Qual é a sua escolha: "))

    grid[escolha-1] = 'x'
    qtda_escolhas += 1

    vencedor = verifica_grid(grid,"x")
    if vencedor != 0:
        break
    if qtda_escolhas == 9:
        break
    imprime_grid(grid)

    escolha_computador = random.randint(1,9)
    '''Testando se a escolha do computador ja existe'''
    while grid[escolha_computador-1] != "-":
        escolha_computador = random.randint(1, 9)

    grid[escolha_computador-1] = '0'
    qtda_escolhas += 1

    vencedor = verifica_grid(grid,"0")
    if vencedor != 0:
        break

    imprime_grid(grid)
if vencedor == 1:
    print("\033[1;34mParabéns!!!, Você Ganhou you win!!! :)\033[m")
elif vencedor == 2:
    print("\033[1;32mVocê Perdeu, O Computador WIN!!!!!\033[m")
else:
    print("Deu Jogo da Velha, Ninguém ganhou!!! :(")

imprime_grid(grid)