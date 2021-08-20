# importar a biblioteca tkinter
import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random
 # atribuindo funções aos botões

def escolheu_pedra():
    jokenpo(escolha_usuario='pedra')

def escolheu_papel():
    jokenpo(escolha_usuario='papel')

def escolheu_tesoura():
    jokenpo(escolha_usuario='tesoura')
# Função que verifica a jogada do usuário e retorna quem foi o vencedor da partida

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['pedra','papel', 'tesoura'])
    if escolha_usuario == escolha_computador:
        mensagem = f'''
            Você: {escolha_usuario.upper()}
            Computador: {escolha_computador.upper()}
            Resultado: Empate!!
        '''
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') \
            or (escolha_usuario == 'papel' and escolha_computador == 'pedra') \
            or (escolha_usuario == 'tesouta' and escolha_computador == 'papel'):
        mensagem = f'''
            Você: {escolha_usuario.upper()}
            Computador: {escolha_computador.upper()}
            Resultado: Você ganhou!!
        '''
    else:
        mensagem = f'''
                   Você: {escolha_usuario.upper()}
                   Eu: {escolha_computador.upper()}
                   Resultado: Computador venceu!!
               '''
    resultado.config(text=mensagem)
# Criar uma isntância de Tk
janela = tk.Tk()
# Criar um LabelFrame para armazenar os elementos
frame = LabelFrame(janela, text='Qual você escolhe?', padx=10, pady=10)
frame.pack()

# Definir os ícones que ser]ao usados nos botões
icone_pedra = PhotoImage(file='imagens/pedra.png')
icone_papel = PhotoImage(file='imagens/papel.png')
icone_tesoura = PhotoImage(file='imagens/tesoura.png')

#Cria os botões com o ícone e a escolha do usuário em cada jogada

Button(frame, text='pedra', command=escolheu_pedra, image=icone_pedra, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='papel', command=escolheu_papel, image=icone_papel, compound=tk.LEFT).grid(column=2, row=1)
Button(frame, text='tesoura', command=escolheu_tesoura, image=icone_tesoura, compound=tk.LEFT).grid(column=3, row=1)

# cria um label que irá exibir o resultado da partida
resultado = Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=0, row=2, columnspan=3)

# define o título do APP
janela.title('JOKENPO = Pedra, Papel e Tesoura')

# Define as medidas da janela do APP
janela.geometry("500x200+300+200")

# executa o programa gerando o APP
janela.mainloop()