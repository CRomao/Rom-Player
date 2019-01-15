__author__ = 'Cicero Romão'
__version__ = '4.0'
__description__ = 'Player de músicas!'
import pygame, time, os, pyautogui, sys
import tkinter as Tk
from time import sleep
from random import randint
from tkinter.filedialog import askopenfile
from tkinter import *
pygame.init() # iniciar o pygame
cor_fundo_padrao = 	(95,158,160)
cor_fundo_escolhida = cor_fundo_padrao
texto_preto = (0,0,0)
os.environ['SDL_VIDEO_CENTERED']='1'
largura = 750
altura = 300
# tenta carregar as musicas do arquivo se existir, se não ele cria o arquivo
try:
    open('musicas\lista_music.txt', 'r')
    open('musicas\lista.txt', 'r')
except:
    open('musicas\lista_music.txt', 'w')
    open('musicas\lista.txt', 'w')

#BOTOES
botao_esquerda = pygame.image.load("icones\icon_esquerda.png")
img1 = botao_esquerda.get_rect()
img1[0] = 100
img1[1] = 150

botao_direita = pygame.image.load("icones\icon_direita.png")
img2 = botao_direita.get_rect()
img2[0] = 330
img2[1] = 150

botao_play = pygame.image.load("icones\icon_play_pause.png")
img3 = botao_play.get_rect()
img3[0] = 215
img3[1] = 150

botao_lista = pygame.image.load("icones\icon_lista.png")
img4 = botao_lista.get_rect()
img4[0] = 430
img4[1] = 8

botao_repet_all = pygame.image.load("icones\icon_repet_all.png")
img5 = botao_repet_all.get_rect()
img5[0] = 465
img5[1] = 250

botao_aleat = pygame.image.load("icones\icon_aleat_desat.png")
img6 = botao_aleat.get_rect()
img6[0] = 430
img6[1] = 250

divisor_x = 5
pygame.mixer.init() # inicia o mixer do pygame
lista = []
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Rom Player")
pygame.display.set_icon(pygame.image.load('icones\icon_player.ico'))
listaNomes = []
pygame.font.init() # inicia as fontes das letras
fonte_padrao = pygame.font.get_default_font()
fonte_addMusica = pygame.font.SysFont("comicsansms", 20)
fonte_nome_music = pygame.font.SysFont("arial", 22)
fonte_sair = pygame.font.SysFont("comicsansms", 20)
fonte_removerMusica = pygame.font.SysFont("comicsansms", 20)
texto_addMusica = 0
texto_nome_music = 0
texto_sair = 0
texto_removerMusica = 0
fundo.fill(cor_fundo_padrao)
a = True
nome_musica = 0
valor_play_pause = 0
valor_repet_all = 0
valor_aleat = 0
z = 0
v = 0
prox = ''
minimizar = 0

def chamarTelaListaMusicas():
    janela = Tk()
    janela.title("Lista de Músicas")
    telaL = 500
    telaA = 400
    telaLargura = janela.winfo_screenwidth()
    telaAltura = janela.winfo_screenheight()
    x = (telaLargura / 2) - (telaL / 2)
    y = (telaAltura / 2) - (telaA / 2)
    janela.geometry("%dx%d+%d+%d" % (telaL, telaA, x, y))
    janela.iconbitmap("icones/icon_player.ico")
    for i in range(len(lista)):
        Label(text='- '+lista[i]).pack()
    janela.mainloop()

def removerMusica():
    global listaNomes, lista, musica_e, z, fundo, cor_fundo_escolhida
    if musica_e == 'Adicione uma música para tocar':
        pyautogui.alert(text='Não existe músicas na lista!', title='Aviso', button='OK')
    else:
        botao = pyautogui.confirm(text='Deseja remover \"'+musica_e+'\" da lista de músicas?', title='Remover', buttons=['SIM', 'NÃO'])
        if botao == 'SIM':
            s = 0
            removida = 0
            for i in range(len(lista)):
                if musica_e == lista[i]:
                    s = i
                    removida = musica_e
                    lista.remove(musica_e)
                    break
            listaNomes.remove(listaNomes[s])
            fundo.fill(cor_fundo_escolhida)
            if len(lista) == 0:
                pygame.mixer.music.stop()
                salvarLista()
                pyautogui.alert(text='A música \"' + removida + '\" foi removida da lista!', title='', button='OK')
                musica_e = 'Adicione uma música para tocar'
            else:
                pygame.mixer.music.stop()
                pyautogui.alert(text='A música \"'+removida+'\" foi removida da lista!', title='', button='OK')
                musica_e = 'Música removida!'
                salvarLista()
                pyautogui.alert(text='Sua lista de músicas foi atualizada!', title='', button='OK')
        else:
            lista = lista
            listaNomes = listaNomes
    salvarLista()

def salvarLista():
    global listaNomes, lista
    arquivo = open('musicas\lista_music.txt', 'w')
    arquivo_lista = open('musicas\lista.txt', 'w')
    for i  in range(len(listaNomes)):
        arquivo.writelines(listaNomes[i])
        arquivo.writelines("\n")
    for i  in range(len(lista)):
	    arquivo_lista.writelines(lista[i])
	    arquivo_lista.writelines("\n")

opcoes = {}
def adicionarMusica():
	global listaNomes, opcoes, lista, musica_e, z, fundo, cor_fundo_escolhida, minimizar, botao_play, valor_play_pause
	jatem = False
	root = Tk()
	root.geometry('0x0')
	root.overrideredirect(False)
	root.iconbitmap('icones\icon_player.ico')
	opcoes['defaultextension'] = '.mp3'
	opcoes['filetypes'] = [('arquivos .mp3', '.mp3')]
	opcoes['initialdir'] = ''    # será o diretório atual
	opcoes['initialfile'] = '' #apresenta todos os arquivos no diretorio
	opcoes['title'] = 'Selecione a música'
	nome_musica = askopenfile(mode='r', **opcoes)
	root.destroy()
	root.mainloop()
	try:
		fundo.fill(cor_fundo_escolhida)
		d = nome_musica.name
		f = d.split('/')
		w = f[len(f) - 1]
		w = w.split('.')
		if d in listaNomes:
			pyautogui.alert(text='A música \"' + w[0] + '\" já encontra-se na lista!', title='', button='OK')
			listaNomes = listaNomes
			lista = lista
			jatem = True
		else:
			try:
				pygame.mixer.music.load(d)
				pygame.mixer.music.play()
				listaNomes.append(nome_musica.name)
				lista.append(w[0])
				musica_e = w[0]
				z = len(lista) - 1
			except:
				pyautogui.alert(text='Não foi possível reproduzir a música!', title='Erro', button='OK')
				listaNomes = listaNomes
				lista = lista
		if valor_play_pause == 1 and jatem == False:
			botao_play = pygame.image.load("icones\icon_play_pause.png")
			valor_play_pause = 0
	except AttributeError as error:
		listaNomes = listaNomes
		lista = lista
	minimizar = 1
	salvarLista()
def lerListaMusics():
	global listaNomes, lista
	arquivo_lista = open('musicas\lista.txt', 'r')
	arquivo = open('musicas\lista_music.txt', 'r')
	listaNomes = arquivo.readlines()
	lista = arquivo_lista.readlines()
	for i in range(len(listaNomes)):
		t = len(listaNomes[i])
		listaNomes[i] = listaNomes[i][:t - 1]
		listaNomes[i] = listaNomes[i]
	for i in range(len(lista)):
		t = len(lista[i])
		lista[i] = lista[i][:t - 1]
		lista[i] = lista[i]

def validarPassagemMusica():
	global listaNomes, z, musica_e, lista, v
	try:
		pygame.mixer.music.stop()
		pygame.mixer.music.load(listaNomes[z])
		pygame.mixer.music.play()
	except:
		musica_e = 'Música não encontrada!'
		lista.remove(lista[z])
		listaNomes.remove(listaNomes[z])
		salvarLista()
	v = z	
	
def validarPassagemMusica2():
	global lista, musica_e, z, valor_play_pause, listaNomes
	if len(lista) == 0:
		musica_e = 'Adicione uma música para tocar'
	else:
		musica_e = lista[z]
	if valor_play_pause == 0:
		try:
			pygame.mixer.music.stop()
			pygame.mixer.music.load(listaNomes[z])
			pygame.mixer.music.play()
		except:
			musica_e = 'Música não encontrada!'
			if len(lista) == 0:
				musica_e = 'Adicione uma música para tocar'
			else:
				lista.remove(lista[z])
				listaNomes.remove(listaNomes[z])
				salvarLista()
def musicaAlearoriaAtivada():
    global z, lista, listaNomes, musica_e
    z = randint(0,(len(listaNomes)-1))
    musica_e = lista[z]
    fundo.fill(cor_fundo_escolhida)
    pygame.mixer.music.load(listaNomes[z])
    pygame.mixer.music.play()

lerListaMusics()
if len(lista) == 0:
    musica_e = 'Adicione uma música para tocar'
else:
	while not pygame.mixer.music.get_busy():
		try:
			pygame.mixer.music.load(listaNomes[z])
			pygame.mixer.music.play()
			musica_e = lista[0]
		except:
			if len(lista) == 0:
				musica_e = 'Adicione uma música para tocar'
				break
			else:
				del(lista[0])
				del(listaNomes[0])
		
				
while a:
    if valor_aleat == 1 and not pygame.mixer.music.get_busy():
        musicaAlearoriaAtivada()
    elif not pygame.mixer.music.get_busy() and musica_e != 'Adicione uma música para tocar' and valor_repet_all == 0:
        z = z + 1
        if z > (len(listaNomes) - 1):
            z = 0
        validarPassagemMusica2()
        fundo.fill(cor_fundo_escolhida)
    elif valor_repet_all == 1 and not pygame.mixer.music.get_busy() and musica_e != 'Adicione uma música para tocar':
        pygame.mixer.music.load(listaNomes[z])
        pygame.mixer.music.play()
    time.sleep(0.5)
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_posX = event.pos
            if (mouse_pos[0] >= 437 and mouse_pos[0] <= 489) and (mouse_pos[1] >= 15 and mouse_pos[1] <= 67): # se clicar na lista das musicas
                chamarTelaListaMusicas()
            if musica_e != 'Adicione uma música para tocar':
                if (mouse_pos[0] >= 433 and mouse_pos[0] <= 453) and (mouse_pos[1] >= 252 and mouse_pos[1] <= 272): # clicou no aleatorio
                    if valor_aleat == 0:
                        botao_aleat = pygame.image.load("icones\icon_aleat_ativ.png")
                        valor_aleat = 1
                    elif valor_aleat == 1:
                        botao_aleat = pygame.image.load("icones\icon_aleat_desat.png")
                        valor_aleat = 0
                if (mouse_pos[0] >= 467 and mouse_pos[0] <= 487) and (mouse_pos[1] >= 252 and mouse_pos[1] <= 272): # clicou no de repetir
                    if valor_repet_all == 0:
                        botao_repet_all = pygame.image.load("icones\icon_repet_atual.png")
                        valor_repet_all = 1
                    elif valor_repet_all == 1:
                        botao_repet_all = pygame.image.load("icones\icon_repet_all.png")
                        valor_repet_all = 0
                if (mouse_pos[0] >= 222 and mouse_pos[0] <= 274) and (mouse_pos[1] >= 159 and mouse_pos[1] <= 208): # quando clica no de pausar
                    if valor_play_pause == 0:
                        botao_play = pygame.image.load("icones\icon_play.png")
                        valor_play_pause = 1
                        pygame.mixer.music.pause()
                        if v != z:
                            v = z
                    else:
                        botao_play = pygame.image.load("icones\icon_play_pause.png")
                        valor_play_pause = 0
                        if v == z:
	                        pygame.mixer.music.unpause()
                        elif v != z and z == prox:
                            pygame.mixer.music.load(listaNomes[z])
                            pygame.mixer.music.play()
                            v = z
                        else:
                            pygame.mixer.music.load(listaNomes[z])
                            pygame.mixer.music.play()
                            v = z
                if (mouse_pos[0] >= 335 and mouse_pos[0] <= 389) and (mouse_pos[1] >= 159 and mouse_pos[1] <= 208): # direita
                    if valor_aleat == 0:
                        cor_fundo_escolhida = cor_fundo_padrao
                        fundo.fill(cor_fundo_escolhida)
                        v = z
                        z += 1
                        prox = z
                        if z > (len(listaNomes)-1):
                            z = 0
                        validarPassagemMusica2()
                    else:
                        musicaAlearoriaAtivada()
                if (mouse_pos[0] >= 107 and mouse_pos[0] <= 159) and (mouse_pos[1] >= 159 and mouse_pos[1] <= 208): # esquerda
                    if valor_aleat == 0:
                        cor_fundo_escolhida = cor_fundo_padrao
                        fundo.fill(cor_fundo_escolhida)
                        v = z
                        z -= 1
                        prox = z
                        if z < 0:
                            z = (len(listaNomes) - 1)
                        validarPassagemMusica2()
                    else:
                        musicaAlearoriaAtivada()
        if event.type == pygame.KEYDOWN:
            if musica_e != 'Adicione uma música para tocar':
                if event.key == pygame.K_RIGHT:
                    if valor_aleat == 0:
                        cor_fundo_escolhida = cor_fundo_padrao
                        fundo.fill(cor_fundo_escolhida)
                        v = z
                        z += 1
                        if z > (len(listaNomes) - 1):
                            z = 0
                        validarPassagemMusica2()
                    else:
                        musicaAlearoriaAtivada()
                if event.key == pygame.K_LEFT:
                    if valor_aleat == 0:
                        cor_fundo_escolhida = cor_fundo_padrao
                        fundo.fill(cor_fundo_escolhida)
                        v = z
                        z -= 1
                        if z < 0:
                            z = (len(listaNomes) - 1)
                        validarPassagemMusica2()
                    else:
                        musicaAlearoriaAtivada()
                if event.key == pygame.K_SPACE:
                    if valor_play_pause == 0:
                        botao_play = pygame.image.load("icones\icon_play.png")
                        valor_play_pause = 1
                        pygame.mixer.music.pause()
                        if v != z:
                            v = z
                    else:
                        botao_play = pygame.image.load("icones\icon_play_pause.png")
                        valor_play_pause = 0
                        if v == z:
                            pygame.mixer.music.unpause()
                        elif v != z and z == prox:
                            validarPassagemMusica()
                        else:
                            validarPassagemMusica()
            if event.key == pygame.K_a:
                adicionarMusica()
            if event.key == pygame.K_c:
                a = False
            if event.key == pygame.K_r:
                removerMusica()
    texto_addMusica = fonte_addMusica.render('[A] - Adicionar Música', True, (texto_preto))
    fundo.blit(texto_addMusica, (510,0))
    texto_removerMusica = fonte_removerMusica.render('[R] - Remover Música', True, (texto_preto))
    fundo.blit(texto_removerMusica, (510,25))
    texto_sair = fonte_sair.render('[C] - Sair', True, (texto_preto))
    fundo.blit(texto_sair, (510, 50))
    texto_nome_music = fonte_nome_music.render(musica_e, True, (texto_preto))
    pygame.draw.rect(fundo, texto_preto, [500, 0, divisor_x, altura])
    fundo.blit(texto_nome_music, (90, 70))
    fundo.blit(botao_esquerda, (img1[0], img1[1]))
    fundo.blit(botao_direita, (img2[0], img2[1]))
    fundo.blit(botao_play, (img3[0], img3[1]))
    fundo.blit(botao_lista, (img4[0], img4[1]))
    fundo.blit(botao_repet_all, (img5[0], img5[1]))
    fundo.blit(botao_aleat, (img6[0], img6[1]))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()