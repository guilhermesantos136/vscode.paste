import random
import tkinter as tk
import json

filename = "WebstersEnglishDictionary-master/WebstersEnglishDictionary-master/dicionario.json"

# abrir o arquivo JSON e ler o conteúdo
with open(filename, 'r') as arquivo:
    conteudo = arquivo.read()

# converter o conteúdo JSON em um dicionário Python
dicionario = json.loads(conteudo)

palavra_antiga = ""

dica_mostrada = False

# inicializar variáveis de pontuação e número de tentativas
pontuacao = 0
tentativas = 0


def escolher_palavra():
    global palavra, definicao, baralhada, dica_mostrada, palavra_antiga
    palavra, definicao = random.choice(list(dicionario.items()))
    while palavra == palavra_antiga:
        palavra, definicao = random.choice(list(dicionario.items()))
    palavra_antiga = palavra
    dica_mostrada = False
    lista = list(palavra.strip(""))
    random.shuffle(lista)
    baralhada = "".join(lista)
    baralhada_label.config(text=baralhada)
    resultado_label.config(text="")
    dica_label.config(text="")


def verificar_palavra():
    global pontuacao, tentativas
    palavra_correta = palavra_entry.get().strip().lower()
    if palavra_correta == palavra:
        pontuacao += 1
        resultado_label.config(text="Correto! Definição: " + definicao)
        pontuacao_label.config(text="Pontuação: " + str(pontuacao))
        escolher_palavra()
        palavra_entry.delete(0, tk.END)
    else:
        tentativas += 1
        resultado_label.config(text="Incorreto. Tente novamente.")
        tentativas_label.config(text="Tentativas: " + str(tentativas))


def reiniciar_jogo():
    global pontuacao, tentativas
    pontuacao = 0
    tentativas = 0
    escolher_palavra()
    palavra_entry.delete(0, tk.END)
    pontuacao_label.config(text="Pontuação: " + str(pontuacao))
    tentativas_label.config(text="Tentativas: " + str(tentativas))


def mostrar_dica():
    global definicao, dica_mostrada
    if not dica_mostrada:
        dica_mostrada = True
        dica = definicao[:len(definicao)]  # exibe a primeira metade da definição
        dica_label.config(text="Dica: " + dica)
    else:
        dica_label.config(text="Você já usou a dica!")


# criar janela
janela = tk.Tk()
janela.minsize(800, 600)

# criar widgets
pergunta_label = tk.Label(janela, text="Qual é a palavra?", font=("Arial", 24))
baralhada_label = tk.Label(janela, text="", font=("Arial", 14))
palavra_entry = tk.Entry(janela, width=40, font=("Arial", 14))
verificar_button = tk.Button(janela, text="Verificar", command=verificar_palavra, width=20, height=2)
verificar_button.configure(background="green", foreground="white", font=("Arial", 14), relief="groove")
reiniciar_button = tk.Button(janela, text="Reiniciar", command=reiniciar_jogo, width=20, height=2)
reiniciar_button.configure(background="blue", foreground="white", font=("Arial", 14), relief="groove")
resultado_label = tk.Label(janela, text="")
pontuacao_label = tk.Label(janela, text="Pontuação: 0")
tentativas_label = tk.Label(janela, text="Tentativas: 0")
dica_button = tk.Button(janela, text="Dica", command=mostrar_dica, width=20, height=2)
dica_button.configure(background="orange", foreground="white", font=("Arial", 14), relief="groove")
dica_label = tk.Label(janela, text="", font=("Arial", 14))

# organizar widgets na janela
escolher_palavra()
pergunta_label.pack()
baralhada_label.pack()
palavra_entry.pack()
verificar_button.pack()
reiniciar_button.pack()
resultado_label.pack()
pontuacao_label.pack()
tentativas_label.pack()
dica_button.pack()
dica_label.pack()

# iniciar aplicação
janela.mainloop()
