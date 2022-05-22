'''
link para a documentacao do pygame: https://www.pygame.org/docs/
OBS: Os eixos x e y do diplay tem inicio da ponta superior esqueda da janela
	o valor de x aumenta para direita e o valor de y aumenta para baixo

                        RESUMO DAS FUNCOES DO PYGAME QUE FORAM UTILIZADAS
			pg = pygame
								pg.event
--pg.event.get() => retorna uma lista com todos os out puts do mouse, do teclado e outros

--um_evento.type => retorna um numero inteiro que equivale a um tipo de evento

obs: pg.MOUSEBUTTONDOWN == 1025
obs: pg.QUIT == 256

								pg.mouse
--pg.mouse.get_pos() => retorna uma tupla com dois elementos que equivalem as coordenadas x e y do mouse

								pg.mixer.music
--pg.mixer.music.load(st) => nao tem valor de retorno
st = uma string que equivale ao arquivo de som que vc queira abrir (deve estar em mp3 ou wav)
> carrega a musica relativa ao st na memoria

--pg.mixer.music.play(n) => nao tem valor de retorno
n = um valor inteiro maior ou igual a -1
faz a faixa de musica tocar n vezes, se n for igual a -1 a faixa toca sem parar

--pg.mixer.music.get_volume() => retorna um float entre 0 e 1, que equivale ao volume da faixa de musica

--pg.mixer.music.set_volume(float) => nao tem valor de retorno
float = um float entre 1 e 0
> redefine o volume para n

--pg.mixer.music.stop() => n tem valor de retorno
faz a faixa de musica parar de tocar

								pg.mixer.Sound
--pg.mixer.Sound(st) => retorna um objeto de tipo Sound
st = uma string que equivale ao arquivo de som que vc queira abrir futuramente (deve estar em wav)
> esse som pode ser tocado a partir de uma faixa de som alternativa, definida pelo pygame

--pg.mixer.Sound.set_volume(obj_sound ,float) => nao tem valor de retorno
obj_sound = objeto definido pela funcao: pg.mixer.Sound()
float = um float entre 1 e 0
> muda o som do obj_sound

								pg.font
--pg.font.get_fonts() => retorna uma lista de strings com todas as fontes instaladas no computador

--pg.font.SysFont(string_font, tamanho) => retorna um objeto de tipo pg.font.Font
string_font = uma string com o nome de uma fonte
tamanho = um numero int que equivale ao tamanho da fonte

--obj_font.render(string, n, color) => retorna um objeto de tipo pg.Surface, com a cor definida pela tupla
string = a string que vai virar uma superficie
n = numero equivalente a valor de Anti-Aliasing, ou seja a qualidade da imagem
color = (red, green, blue), define a cor das letras
	red = int de 0 ate 255
	green = int de 0 ate 255
	blue = int de 0 ate 255

								pg.image
--pg.image.load(st) => retorna um objeto de tipo pg.Surface, relativo a st
st = uma string que equivale ao arquivo de imagem que vc queira abrir futuramente

								pg.display
--pg.display.set_mode((width, height)) => retorna um objeto de tipo pg.Surface e trata ele como a superficie principal (a janela do jogo)
width = numero int maior ou igual a 0, equivale a largura da janela
height = numero int maior ou igual a 0, equivale a altura da janela

--pg.display.set_caption(st) => nao tem valor de retorno
st = uma string
> redefine a nome da janela para o valor de st

--pg.display.set_icon(obj_surface) => nao tem valor de retorno
obj_surface = definida pelas funcoes: obj_font.render(string, n, color) ou pg.image.load(st)

--pg.display.update() => nao tem valor de retorno
> atualiza a tela, as imgaens so sao desenhadas na tela quando essa funcao eh chamada

--obj_display.blit(obj_surface, coord) => nao tem valor de retorno
obj_display = eh o objeto pg.Surface principal, gerado pela funcao: pg.display.set_mode((width, height))
obj_surface = objeto pg.Surface normal, gerado pelas funcoes: obj_font.render(string, n, color) ou pg.image.load(st)
coord = (x,y), x e y equivalem as coordenadas da ponta superior esqueda do retangulo
	x = numero int, coordenada do eixo x
	y = numero int, coordenada do eixo y
> deixa a imagem pronta para ser colocada na janela principal

								pg.draw
--pg.draw.rect(obj_display, color, tamanho) => nao tem valor de retorno
obj_display = eh o objeto pg.Surface principal, gerado pela funcao: pg.display.set_mode((width, height))
color = (red, green, blue), define a cor da superficie
	red = int de 0 ate 255
	green = int de 0 ate 255
	blue = int de 0 ate 255
tamanho = (x, y, width, height), x e y equivalem as coordenadas da ponta superior esqueda do retangulo
	x = numero int, coordenada do eixo x
	y = numero int, coordenada do eixo y
	width = numero int maior ou igual a 0, equivale a largura da janela
	height = numero int maior ou igual a 0, equivale a altura da janela
> deixa a imagem pronta para ser colocada na janela principal

--pg.draw.circle(obj_display, color, coord, raio) => nao tem valor de retorno
color = (red, green, blue), define a cor da superficie
	red = int de 0 ate 255
	green = int de 0 ate 255
	blue = int de 0 ate 255
coord = (x,y), equivale as coordenadas do centro do circulo
	x = numero int, coordenada do eixo x
	y = numero int, coordenada do eixo y
raio = numero int maior ou igual a 0, equivale ao raio do circulo
> deixa a imagem pronta para ser colocada na janela principal
'''
import pygame as pg
import copy as cp
from time import sleep
#Inicializa as funcoes e processos do pygame
pg.init()

#-------------------------------------CLASSES CRIADAS-------------------------------------------------
#Classe dos pioes
class pawn:
	def __init__(self,x,y,image):
		self.x = x
		self.y = y
		self.image = image
		self.button_move = 48
		self.button_color = (150, 50, 150)
		self.button_radius = round(((32*(2**0.5))/2) - 5)
		self.button_pressed = False
		self.wall = 10

	def center(self):
		center_x = self.x + round(32/2)
		center_y = self.y + round(32/2)
		center = [center_x, center_y]
		return center

	def draw(self, window):
		window.blit(self.image,(self.x,self.y))

#Classe das barreiras
class wall:
	L1 = [0, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L2 = [1, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L3 = [2, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L4 = [3, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L5 = [4, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L6 = [5, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L7 = [6, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	L8 = [7, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	valid = True
	status_wall = '|'
	button_radius = 5
	color = (0,250,0)
	color_wall = (100,100,200)
#--------------------------------------FUNCOES DO SISTEMA EM GERAL------------------------------------
#Essa funcao é utilizada para criar um botao
def put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, text=''):
	color = (173, 216, 230)
	over_color = (70,130,180)
	if type(text) == pg.Surface:
		t_width = text.get_width()
		t_height = text.get_height()
	else:
		t_width = 0
	if t_width > width:
		width = t_width
	if is_over_rect(x, y, width, height, mouse):
		pg.draw.rect(window, (over_color), (x, y, width, height))
	else:
		pg.draw.rect(window, (color), (x, y, width, height))
	pg.draw.rect(window, (0, 0, 0), (x, y, width, height), 2)
	if type(text) == pg.Surface:
		window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
	if mouse_pressed and is_over_rect(x, y, width, height, mouse):
		click_button.play()
		return True
	return False

#Uma funcao que retorna os movimentos no inicio do jogo
def r_movs():
	#Dicionario referente aos movimentospossiveis de serem feitos
	movs = {'A1':['  ','B1','A2','  '],'B1':['  ','C1','B2','A1'],'C1':['  ','D1','C2','B1'],'D1':['  ','E1','D2','C1'],'E1':['  ','F1','E2','D1'], 'F1':['  ','G1','F2','E1'],'G1':['  ','H1','G2','F1'],'H1':['  ','I1','H2','G1'],'I1':['  ','  ','I2','H1'],\
		\
			'A2':['A1','B2','A3','  '],'B2':['B1','C2','B3','A2'],'C2':['C1','D2','C3','B2'],'D2':['D1','E2','D3','C2'],'E2':['E1','F2','E3','D2'], 'F2':['F1','G2','F3','E2'],'G2':['G1','H2','G3','F2'],'H2':['H1','I2','H3','G2'],'I2':['I1','  ','I3','H2'],\
		\
			'A3':['A2','B3','A4','  '],'B3':['B2','C3','B4','A3'],'C3':['C2','D3','C4','B3'],'D3':['D2','E3','D4','C3'],'E3':['E2','F3','E4','D3'], 'F3':['F2','G3','F4','E3'],'G3':['G2','H3','G4','F3'],'H3':['H2','I3','H4','G3'],'I3':['I2','  ','I4','H3'],\
		\
			'A4':['A3','B4','A5','  '],'B4':['B3','C4','B5','A4'],'C4':['C3','D4','C5','B4'],'D4':['D3','E4','D5','C4'],'E4':['E3','F4','E5','D4'], 'F4':['F3','G4','F5','E4'],'G4':['G3','H4','G5','F4'],'H4':['H3','I4','H5','G4'],'I4':['I3','  ','I5','H4'],\
		\
			'A5':['A4','B5','A6','  '],'B5':['B4','C5','B6','A5'],'C5':['C4','D5','C6','B5'],'D5':['D4','E5','D6','C5'],'E5':['E4','F5','E6','D5'], 'F5':['F4','G5','F6','E5'],'G5':['G4','H5','G6','F5'],'H5':['H4','I5','H6','G5'],'I5':['I4','  ','I6','H5'],\
		\
			'A6':['A5','B6','A7','  '],'B6':['B5','C6','B7','A6'],'C6':['C5','D6','C7','B6'],'D6':['D5','E6','D7','C6'],'E6':['E5','F6','E7','D6'], 'F6':['F5','G6','F7','E6'],'G6':['G5','H6','G7','F6'],'H6':['H5','I6','H7','G6'],'I6':['I5','  ','I7','H6'],\
		\
			'A7':['A6','B7','A8','  '],'B7':['B6','C7','B8','A7'],'C7':['C6','D7','C8','B7'],'D7':['D6','E7','D8','C7'],'E7':['E6','F7','E8','D7'], 'F7':['F6','G7','F8','E7'],'G7':['G6','H7','G8','F7'],'H7':['H6','I7','H8','G7'],'I7':['I6','  ','I8','H7'],\
		\
			'A8':['A7','B8','A9','  '],'B8':['B7','C8','B9','A8'],'C8':['C7','D8','C9','B8'],'D8':['D7','E8','D9','C8'],'E8':['E7','F8','E9','D8'], 'F8':['F7','G8','F9','E8'],'G8':['G7','H8','G9','F8'],'H8':['H7','I8','H9','G8'],'I8':['I7','  ','I9','H8'],\
		\
			'A9':['A8','B9','  ','  '],'B9':['B8','C9','  ','A9'],'C9':['C8','D9','  ','B9'],'D9':['D8','E9','  ','C9'],'E9':['E8','F9','  ','D9'], 'F9':['F8','G9','  ','E9'],'G9':['G8','H9','  ','F9'],'H9':['H8','I9','  ','G9'],'I9':['I8','  ','  ','H9']}
	return movs

#Define a interacao de uma barreira com as casas (onde os pioes pode andar)
def interaction_p_w():
	interac = {\
	'0_0':['A1','B1','A2','B2'],'0_1':['B1','C1','B2','C2'],'0_2':['C1','D1','C2','D2'],'0_3':['D1','E1','D2','E2'],\
	'0_4':['E1','F1','E2','F2'],'0_5':['F1','G1','F2','G2'],'0_6':['G1','H1','G2','H2'],'0_7':['H1','I1','H2','I2'],\
	\
	'1_0':['A2','B2','A3','B3'],'1_1':['B2','C2','B3','C3'],'1_2':['C2','D2','C3','D3'],'1_3':['D2','E2','D3','E3'],\
	'1_4':['E2','F2','E3','F3'],'1_5':['F2','G2','F3','G3'],'1_6':['G2','H2','G3','H3'],'1_7':['H2','I2','H3','I3'],\
	\
	'2_0':['A3','B3','A4','B4'],'2_1':['B3','C3','B4','C4'],'2_2':['C3','D3','C4','D4'],'2_3':['D3','E3','D4','E4'],\
	'2_4':['E3','F3','E4','F4'],'2_5':['F3','G3','F4','G4'],'2_6':['G3','H3','G4','H4'],'2_7':['H3','I3','H4','I4'],\
	\
	'3_0':['A4','B4','A5','B5'],'3_1':['B4','C4','B5','C5'],'3_2':['C4','D4','C5','D5'],'3_3':['D4','E4','D5','E5'],\
	'3_4':['E4','F4','E5','F5'],'3_5':['F4','G4','F5','G5'],'3_6':['G4','H4','G5','H5'],'3_7':['H4','I4','H5','I5'],\
	\
	'4_0':['A5','B5','A6','B6'],'4_1':['B5','C5','B6','C6'],'4_2':['C5','D5','C6','D6'],'4_3':['D5','E5','D6','E6'],\
	'4_4':['E5','F5','E6','F6'],'4_5':['F5','G5','F6','G6'],'4_6':['G5','H5','G6','H6'],'4_7':['H5','I5','H6','I6'],\
	\
	'5_0':['A6','B6','A7','B7'],'5_1':['B6','C6','B7','C7'],'5_2':['C6','D6','C7','D7'],'5_3':['D6','E6','D7','E7'],\
	'5_4':['E6','F6','E7','F7'],'5_5':['F6','G6','F7','G7'],'5_6':['G6','H6','G7','H7'],'5_7':['H6','I6','H7','I7'],\
	\
	'6_0':['A7','B7','A8','B8'],'6_1':['B7','C7','B8','C8'],'6_2':['C7','D7','C8','D8'],'6_3':['D7','E7','D8','E8'],\
	'6_4':['E7','F7','E8','F8'],'6_5':['F7','G7','F8','G8'],'6_6':['G7','H7','G8','H8'],'6_7':['H7','I7','H8','I8'],\
	\
	'7_0':['A8','B8','A9','B9'],'7_1':['B8','C8','B9','C9'],'7_2':['C8','D8','C9','D9'],'7_3':['D8','E8','D9','E9'],\
	'7_4':['E8','F8','E9','F9'],'7_5':['F8','G8','F9','G9'],'7_6':['G8','H8','G9','H9'],'7_7':['H8','I8','H9','I9']\
	}
	return interac

#Funcao que diz se o mouse esta em cima do botao
#Usado apenas na interacao do mouse com um botao redondo
def is_over(x, y, mouse, radius):
	distance = ((mouse[0] - x)**2 + (mouse[1] - y)**2)**0.5
	if distance <= radius:
		return True
	return False

#Funcao que diz se o mouse esta em cima do botao
#Usado apenas na interacao do mouse com um botao retangular
def is_over_rect(x, y, width, height, mouse):
	if mouse[0] > x and mouse[0] < x + width:
		if mouse[1] > y and mouse[1] < y + height:
			return True
	return False

#Retorna uma lita com quase todos os textos que vai aparecer na tela
def sis_texts(n):
	#Fontes principais sao: algerian, castellar, footlight ou arial
	#Define qual fonte sera usada
	f = pg.font.get_fonts()
	if 'algerian' in f:
		name_font = 'algerian'
	elif 'castellar' in f:
		name_font = 'castellar'
	elif 'arial' in f:
		name_font = 'arial'
	elif 'footlight' in f:
		name_font = 'footlight'
	else:
		print('As fontes mais adequadas para o programa nao forao encontradas')
		print('algerian, castellar, arial, footlight')
		name_font = f[0]

	#Formatacao das palavras
	if name_font == 'castellar':
		font_nano = pg.font.SysFont(name_font,15)
		font_mine = pg.font.SysFont(name_font,20)
		font = pg.font.SysFont(name_font,35)
		font_mid = pg.font.SysFont(name_font,55)
		font_big = pg.font.SysFont(name_font,65)
	else:
		font_nano = pg.font.SysFont(name_font,20)
		font_mine = pg.font.SysFont(name_font,25)
		font = pg.font.SysFont(name_font,40)
		font_mid = pg.font.SysFont(name_font,60)
		font_big = pg.font.SysFont(name_font,70)

	if n == 4:
		#Textos que vao aparecer dentro da tela da opcao de configuracao
		text_1 = 'Volume'
		text_2 = 'Plano de fundo'
		text_3 = 'Pioes'
		text_4 = 'Tabuleiro'
		text_5 = 'Voltar'
		text_6 = 'Musica:'
		#Tabuleiro
		text_7 = 'Tab. de madeira'
		text_8 = 'Tab. verde'
		text_9 = 'Tab. azul'
		text_10 = 'Tab. branco'
		text_11 = 'Tab. estilo xadrez'
		text_12 = 'Tab. de granito'
		#Plano de fundo
		text_13 = 'Madeira escura'
		text_14 = 'Gaming'
		text_15 = 'Pedras'
		text_16 = 'Void'
		text_17 = 'Arco-iris'
		text_18 = 'Madeira clara'
		text_19 = 'Tijolo'
		text_20 = 'Horizonte'
		text_21 = 'Estrelas'
		#Pioes
		text_22 = 'Jogador 1:'
		text_23 = 'Jogador 2:'
		text_24 = 'Coroa'
		text_25 = 'Coroa negra'
		text_26 = 'Rainha negra'
		text_27 = 'Rainha dourada'
		text_28 = 'Piao transpa.'
		text_29 = 'Piao negro'
		text_30 = 'Piao dourado'
		text_31 = 'Piao azul'

		c_texts = (
					font_mine,
					font.render(text_1, 1, (255,255,255)),font.render(text_2, 1, (0,0,0)),font.render(text_3, 1, (0,0,0)),
					font.render(text_4, 1, (0,0,0)),font.render(text_5, 1, (0,0,0)),font.render(text_6, 1, (255,255,255)),
					font_mine.render(text_7, 1, (0,0,0)),font_mine.render(text_8, 1, (0,0,0)),font_mine.render(text_9, 1, (0,0,0)),
					font_mine.render(text_10, 1, (0,0,0)),font_mine.render(text_11, 1, (0,0,0)),font_mine.render(text_12, 1, (0,0,0)),
					font_mine.render(text_13, 1, (0,0,0)),font_mine.render(text_14, 1, (0,0,0)),font_mine.render(text_15, 1, (0,0,0)),
					font_mine.render(text_16, 1, (0,0,0)),font_mine.render(text_17, 1, (0,0,0)),font_mine.render(text_18, 1, (0,0,0)),
					font_mine.render(text_19, 1, (0,0,0)),font_mine.render(text_20, 1, (0,0,0)),font_mine.render(text_21, 1, (0,0,0)),
					font.render(text_22, 1, (255,255,255)),font.render(text_23, 1, (255,255,255)),
					font_nano.render(text_24, 2, (0,0,0)),font_nano.render(text_25, 2, (0,0,0)),font_nano.render(text_26, 2, (0,0,0)),
					font_nano.render(text_27, 2, (0,0,0)),font_nano.render(text_28, 2, (0,0,0)),font_nano.render(text_29, 2, (0,0,0)),
					font_nano.render(text_30, 2, (0,0,0)),font_nano.render(text_31, 2, (0,0,0))
					)
		return c_texts

	elif n == 3:
		#Textos que vao aparecer dentro da tela do manual
		text_1 = 'Voltar'
		text_2 = 'Movimentos'
		text_3 = 'Mov. especiais'
		text_4 = 'objetivo do jogo'

		ma_texts = (
					font_mine,
					font.render(text_1, 1, (0,0,0)),font.render(text_2, 1, (0,0,0)),font.render(text_3, 1, (0,0,0)),
					font.render(text_4, 1, (0,0,0))
					)
		return ma_texts

	elif n == 2:
		#Textos que vao aparecer dentro da tela do menu
		text_0 = 'BEM VINDO AO BLOQUEIO!'
		text_1 = 'Jogar'
		text_2 = 'Manual'
		text_3 = 'Configuracoes'
		text_4 = 'Fechar jogo'

		m_texts = (
				font_mid.render(text_0, 1, (255,255,255)), font.render(text_1, 1, (0,0,0)), font.render(text_2, 1, (0,0,0)),
				font.render(text_3, 1, (0,0,0)), font.render(text_4, 1, (0,0,0))
				)
		return m_texts

	elif n == 1:
		#Textos que vao aparecer dentro da tela de jogo
		text_1 = 'Vez do jogador 1'
		text_2 = 'Vez do jogador 2'
		text_3 = 'Rotacionar barreira'
		text_4 = 'BARREIRA'
		text_5 = 'INVALIDA'
		text_6 = 'Desistir'

		g_texts = (
				font_mine,
				font.render(text_1, 1 , (250,250,250)), font.render(text_2, 1 , (250,250,250)), font.render(text_3, 1, (0,0,0)),
				font.render(text_4, 1,(240,128,128)),	font.render(text_5, 1,(240,128,128)),   font.render(text_6, 1,(0,0,0)),
				font_big
				)
		return g_texts

#Retorna as imagens usadas pelo codigo
def load_images():
	try:
		open_file = open('imagens.txt','r')
		lines = open_file.readlines()
		if len(lines) != 4:
			raise FileNotFoundError
		brd = pg.image.load(lines[0][:-1])
		bg = pg.image.load(lines[1][:-1])
		pawn1 = pg.image.load(lines[2][:-1])
		pawn2 = pg.image.load(lines[3])
	#A excessao so ativa se:
	#O arquivo das imagens nao existir
	#Ou alguem tenha trocado o que esta escrito dentro dele (para algo que o sistema nao reconheca)
	except FileNotFoundError:
		try:
			open_file = open('imagens.txt','w')
			write = open_file.write('tabuleiro/tab1.png\nbackground/background_1.png\nplayer/pawn1.png\nplayer/pawn2.png')
			open_file.close()
			open_file = open('imagens.txt','r')
			lines = open_file.readlines()
			n = 'tabuleiro'
			brd = pg.image.load(lines[0][:-1])
			n = 'background'
			bg = pg.image.load(lines[1][:-1])
			n = 'player'
			pawn1 = pg.image.load(lines[2][:-1])
			pawn2 = pg.image.load(lines[3])
		#So eh ativado quando algum arquivo nao eh encontrado
		except:

			print('----------------------------------AVISO------------------------------------------')
			print(f'As imagens originais do jogo nao estao dentro da pasta correta ({n}).')
			print('Ou nao existem.')
			print('----------------------------------AVISO------------------------------------------')
			return True, 1, 2, 3, 4

	open_file.close()
	return False, brd, bg, pawn1, pawn2

#Retorna os efetos sonoros e musicas utilizadas no jogo
def load_sounds():
	try:
		pg.mixer.music.load('sound/music.mp3')
		p_move = pg.mixer.Sound('sound/wood.wav')
		b_press = pg.mixer.Sound('sound/wood2.wav')
		click_button = pg.mixer.Sound('sound/click.wav')
		mov_erro = pg.mixer.Sound('sound/erro.wav')
		win = pg.mixer.Sound('sound/win.wav')
	#except normal foi usado pois caso a funcao do pg.music.load de erro, ele eh reconhecido como pygame.error
	#porem as outras retornam FileNotFoundError
	except:
		print('----------------------------------AVISO------------------------------------------')
		print('Os arquivos de som originais do jogo nao estao dentro da pasta correta (sound).')
		print('Ou nao existem.')
		print('----------------------------------AVISO------------------------------------------')
		return True, 1, 2, 3, 4, 5
	return False, p_move, click_button, mov_erro, b_press, win

#--------------------------------------FUNCOES DA JANELA DO JOGO--------------------------------------
#Funcao que é chamada quando o jogo acaba
def end (window, turn, win, w_width, w_height):
	_text_ = sis_texts(1)[7]
	turn += 1
	if turn > 2:
		turn = 1
	text = _text_.render(f'Vitoria do jogador {turn}', 1, (0,0,0))
	win.play()
	t_height = text.get_height()
	t_width = text.get_width()
	x = w_width/2 - t_width/2
	y = w_height/2 - t_height/2
	window.blit(text,(x, y))
	pg.display.update()
	reset = True
	sleep(3)
	return reset

#Funcao que faz as variaveis voltarem ao seu valor padrao (o jogo e reiniciado)
def reset_game(player1, player2, walls, cdt_p_x, cdt_p_y):
	player1.x = cdt_p_x['E']
	player1.y = cdt_p_y['1']
	player2.x = cdt_p_x['E']
	player2.y = cdt_p_y['9']
	player1.wall = 10
	player2.wall = 10

	walls.valid = True
	walls.L1 = [0, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L2 = [1, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L3 = [2, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L4 = [3, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L5 = [4, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L6 = [5, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L7 = [6, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]
	walls.L8 = [7, [[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,''],[False,'']]]

	moves = r_movs()
	option = ''
	turn = 1 
	return option, turn, moves

#Funcao que define se a barreira pode ser colocada em jogo
def validate(line_indx, wall_indx, moves, walls, player1, player2, cdt_p_x, cdt_p_y, mov_erro):
	#Uma copia do obj walls e criada para testarmos se o movimento e valido
	lines = [walls.L1, walls.L2, walls.L3, walls.L4, walls.L5, walls.L6, walls.L7, walls.L8]

	copy_moves = cp.deepcopy(moves)

	#Alteramos os valores que indicam o posicionamento da barreira
	lines[line_indx][1][wall_indx][0] = True
	lines[line_indx][1][wall_indx][1] = walls.status_wall

	test_moves = wall_interaction(lines, copy_moves)

	#Ciclo que so para quando encontrar um caminho que liga o piao do primeiro jogador 
	#ate vitoria ou quando define que nao existe um caminho para ganhar
	p1 = where_p(player1.x, player1.y, cdt_p_x, cdt_p_y)
	path = [p1]
	move = True
	indx_squere = -1
	try:
		while move:
			if test_moves[path[indx_squere]][2] != '  ' and test_moves[path[indx_squere]][2] not in path:
				path.append(test_moves[path[indx_squere]][2])
				indx_squere = -1
				if path[-1][1] == '9':
					move = False
			elif test_moves[path[indx_squere]][1] != '  ' and test_moves[path[indx_squere]][1] not in path:
				path.append(test_moves[path[indx_squere]][1])
				indx_squere = -1

			elif test_moves[path[indx_squere]][3] != '  ' and test_moves[path[indx_squere]][3] not in path:
				path.append(test_moves[path[indx_squere]][3])
				indx_squere = -1

			elif test_moves[path[indx_squere]][0] != '  ' and test_moves[path[indx_squere]][0] not in path:
				path.append(test_moves[path[indx_squere]][0])
				indx_squere = -1
			else:
				indx_squere -= 1
	#Quando esta excecao e acionada significa que nao existe um caminho entre o piao 1 chegar na linha 9
	except IndexError:
		mov_erro.play()
		lines[line_indx][1][wall_indx][0] = False
		lines[line_indx][1][wall_indx][1] = ''
		walls.valid = False
		return False

	#Ciclo que so para quando encontrar um caminho que liga o piao do segundo jogador 
	#ate vitoria ou quando define que nao existe um caminho para ganhar
	#E importante ter 2 while para optimizar o tempo gastopara descobrir o caminho,
	#afinal o piao 1 deve andar  para baixo e o p2 deve andar para cima
	p2 = where_p(player2.x, player2.y, cdt_p_x, cdt_p_y)
	path = [p2]
	move = True
	indx_squere = -1
	try:
		while move:
			if test_moves[path[indx_squere]][0] != '  ' and test_moves[path[indx_squere]][0] not in path:
				path.append(test_moves[path[indx_squere]][0])
				indx_squere = -1
				if path[-1][1] == '1':
					move = False

			elif test_moves[path[indx_squere]][1] != '  ' and test_moves[path[indx_squere]][1] not in path:
				path.append(test_moves[path[indx_squere]][1])
				indx_squere = -1

			elif test_moves[path[indx_squere]][3] != '  ' and test_moves[path[indx_squere]][3] not in path:
				path.append(test_moves[path[indx_squere]][3])
				indx_squere = -1

			elif test_moves[path[indx_squere]][2] != '  ' and test_moves[path[indx_squere]][2] not in path:
				path.append(test_moves[path[indx_squere]][2])
				indx_squere = -1
			else:
				indx_squere -= 1
	#Quando esta excecao e acionada significa que nao existe um caminho para o piao 2 chegar na linha 1
	except IndexError:
		mov_erro.play()
		lines[line_indx][1][wall_indx][0] = False
		lines[line_indx][1][wall_indx][1] = ''
		walls.valid = False
		return False
	return True

#Funcao que retorna a casa que o piao esta naquele momento
def where_p(x, y, cdt_p_x, cdt_p_y):
	list_x = list(cdt_p_x.keys())
	list_y = list(cdt_p_y.keys())
	for coordinate in cdt_p_x:
		if cdt_p_x[coordinate] == x:
			frist = coordinate
			break
	for coordinate in cdt_p_y:
		if cdt_p_y[coordinate] == y:
			second = coordinate
			break

	return frist + second

#Funcao que retorna os movimentos dos pioes apos uma barreira ser colocada
def wall_interaction(lines, mov):
	ract = interaction_p_w()
	for line in lines:
		#qual linha estamos botando a barreira
		fist = str(line[0])
		second = '_'
		wall_indx = 0
		for wall in line[1]:
			#qual coluna estamos botando a barreira
			third = str(wall_indx)
			key = fist + second + third
			#Se tiver uma barreira nessa coordenada os movimentos dos pioes sao restringidos
			if wall[0]:
				if wall[1] == '|':
					mov[ract[key][0]][1] = '  '
					mov[ract[key][1]][3] = '  '
					mov[ract[key][2]][1] = '  '
					mov[ract[key][3]][3] = '  '
				elif wall[1] == '-':
					mov[ract[key][0]][2] = '  '
					mov[ract[key][1]][2] = '  '
					mov[ract[key][2]][0] = '  '
					mov[ract[key][3]][0] = '  '
			wall_indx += 1
	return mov

#Funcao que permite os jogadores colocarem uma parede
def put_wall (window, turn, mouse, mouse_pressed, walls, player1, player2, cdt_p_x, cdt_p_y, moves, mov_erro, b_press):
	if turn == 1:
		player = player1
	elif turn == 2:
		player = player2

	#Altura e largura das barreiras
	side_1 = 10
	side_2 = 82
	#Lista das coordenadas 
	coord = [109,156,203,251,298,345,392,440]
	lines = [walls.L1,walls.L2,walls.L3,walls.L4,walls.L5,walls.L6,walls.L7,walls.L8]
	#Coloca as barreiras na tela
	for line in lines:
		indx = 0
		for wall in line[1]:
			if wall[0]:
				if wall[1] == '|':
					pg.draw.rect(window,walls.color_wall,(coord[indx]-(side_1/2), coord[line[0]]-(side_2/2), side_1, side_2))
				elif wall[1] == '-':
					pg.draw.rect(window,walls.color_wall,(coord[indx]-(side_2/2), coord[line[0]]-(side_1/2), side_2, side_1))
			indx += 1

	#Coloca os botoes de posicionar barreiras no tabuleiro
	if not player.button_pressed and player.wall > 0:
		for line in lines:
			wall_indx = 0
			for wall in line[1]:
				if not wall[0]:
					pg.draw.circle(window,walls.color,(coord[wall_indx],coord[line[0]]),walls.button_radius)
					if is_over(coord[wall_indx],coord[line[0]],mouse,walls.button_radius):
						
						#Caso a barreira estiver na horizontal
						if walls.status_wall == '|':
							pg.draw.rect(window,(255,0,0),(coord[wall_indx]-(side_1/2), coord[line[0]]-(side_2/2), side_1, side_2))
							if line[0] == 0:
								line_before_indx = 0
								line_after_indx = line[0] + 1
							elif line[0] == 7:
								line_before_indx = line[0] - 1
								line_after_indx = 7
							else:
								line_before_indx = line[0] - 1
								line_after_indx = line[0] + 1
							#Caso a linha de cima ou  de baixo tiver uma barreira na posicao vertical nao podemos colocar uma barreira entre elas
							if lines[line_before_indx][1][wall_indx][1] != '|' and lines[line_after_indx][1][wall_indx][1] != '|':
								if mouse_pressed:
									if validate(line[0], wall_indx, moves, walls, player1, player2, cdt_p_x, cdt_p_y, mov_erro):
										b_press.play()
										walls.valid = True
										wall[0] = True
										wall[1] = walls.status_wall
										player.wall -= 1
										turn += 1
							else:
								if mouse_pressed:
									mov_erro.play()
									walls.valid = False

						#Caso a barreira estiver na vertical
						elif walls.status_wall == '-':
							pg.draw.rect(window,(255,0,0),(coord[wall_indx]-(side_2/2), coord[line[0]]-(side_1/2), side_2, side_1))
							if wall_indx == 0:
								wall_before_indx = 0
								wall_after_indx = wall_indx + 1
							elif wall_indx == 7:
								wall_before_indx = wall_indx - 1
								wall_after_indx = 7
							else:
								wall_before_indx = wall_indx - 1
								wall_after_indx = wall_indx + 1
							#Caso a linha na direita ou na esquerda tiver uma barreira na posicao horizontal nao podemos colocar uma barreira entre elas
							if lines[line[0]][1][wall_before_indx][1] != '-' and lines[line[0]][1][wall_after_indx][1] != '-':
								if mouse_pressed:
									if validate(line[0], wall_indx, moves, walls, player1, player2, cdt_p_x, cdt_p_y, mov_erro):
										b_press.play()
										walls.valid = True
										wall[0] = True
										wall[1] = walls.status_wall
										player.wall -= 1
										turn += 1
							else:
								if mouse_pressed:
									mov_erro.play()
									walls.valid = False
				wall_indx += 1

	#Redefine o dicionario de movimentos, de acordo com as barreiras colocadas no tabuleiro
	moves = wall_interaction(lines, moves)

	if turn >= 3:
		turn = 1
	return turn, moves

#Funcao que permite o paio se mover
def mov_pawn(window, turn, mouse, mouse_pressed, player1, player2, cdt_p_x, cdt_p_y, moves, walls, p_move):
	#Determinar qual jogador deve execuatar uma acao
	if turn == 1:
		player = player1
		other = player2
	else:
		player = player2
		other = player1

	#Pega a posicao de cada player 
	where_player = where_p(player.x, player.y, cdt_p_x, cdt_p_y)
	where_other = where_p(other.x, other.y, cdt_p_x, cdt_p_y)
	 
	if player.button_pressed:
		#MOVER PARA CIMA
		if moves[where_player][0] != '  ':
			button_x = player.center()[0]
			button_y = player.center()[1] - player.button_move 
			#Movimento normal
			if moves[where_player][0] != where_other:
				pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
				if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
					p_move.play()
					player.y = cdt_p_y[moves[where_player][0][1]]
					turn += 1
			#Movimentos especiais
			if moves[where_player][0] == where_other:
				#Pula o piao inimigo e vai reto
				if moves[where_other][0] != '  ':
					button_x = other.center()[0]
					button_y = other.center()[1] - other.button_move
					pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
					if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
						p_move.play()
						player.y = cdt_p_y[moves[where_other][0][1]]
						turn += 1
				#Pula o paio inimigo e vai para um dos lados
				if moves[where_other][0] == '  ':
					#Direita
					if moves[where_other][1] != '  ':
						button_x = other.center()[0] + other.button_move
						button_y = other.center()[1]
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][1][0]]
							player.y = cdt_p_y[moves[where_other][1][1]]
							turn += 1
					#Esquerda
					if moves[where_other][3] != '  ':
						button_x = other.center()[0] - other.button_move
						button_y = other.center()[1]
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][3][0]]
							player.y = cdt_p_y[moves[where_other][3][1]]
							turn += 1

		#MOVER PARA DIREITA
		if moves[where_player][1] != '  ':
			button_x = player.center()[0] + player.button_move 
			button_y = player.center()[1]
			#Movimento normal
			if moves[where_player][1] != where_other:
				pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
				if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
					p_move.play()
					player.x = cdt_p_x[moves[where_player][1][0]]
					turn += 1
			#Movimentos especiais
			if moves[where_player][1] == where_other:
				#Pula o piao inimigo e vai reto
				if moves[where_other][1] != '  ':
					button_x = other.center()[0] + other.button_move
					button_y = other.center()[1]
					pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
					if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
						p_move.play()
						player.x = cdt_p_x[moves[where_other][1][0]]
						turn += 1
				#Pula o paio inimigo e vai para um dos lados
				if moves[where_other][1] == '  ':
					#Cima
					if moves[where_other][0] != '  ':
						button_x = other.center()[0]
						button_y = other.center()[1] - other.button_move
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][0][0]]
							player.y = cdt_p_y[moves[where_other][0][1]]
							turn += 1
					#Baixo
					if moves[where_other][2] != '  ':
						button_x = other.center()[0]
						button_y = other.center()[1] + other.button_move
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][2][0]]
							player.y = cdt_p_y[moves[where_other][2][1]]
							turn += 1
		
		#MOVER PARA BAIXO
		if moves[where_player][2] != '  ':
			button_x = player.center()[0]
			button_y = player.center()[1] + player.button_move
			#Movimento normal
			if moves[where_player][2] != where_other:
				pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
				if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
					p_move.play()
					player.y = cdt_p_y[moves[where_player][2][1]]
					turn += 1
			#Movimentos especiais
			if moves[where_player][2] == where_other:
				#Pula o piao inimigo e vai reto
				if moves[where_other][2] != '  ':
					button_x = other.center()[0]
					button_y = other.center()[1] + other.button_move
					pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
					if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
						p_move.play()
						player.y = cdt_p_y[moves[where_other][2][1]]
						turn += 1
				#Pula o paio inimigo e vai para um dos lados
				if moves[where_other][2] == '  ':
					#Direita
					if moves[where_other][1] != '  ':
						button_x = other.center()[0] + other.button_move
						button_y = other.center()[1]
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][1][0]]
							player.y = cdt_p_y[moves[where_other][1][1]]
							turn += 1
					#Esqueda
					if moves[where_other][3] != '  ':
						button_x = other.center()[0] - other.button_move
						button_y = other.center()[1]
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][3][0]]
							player.y = cdt_p_y[moves[where_other][3][1]]
							turn += 1
		
		#MOVER PARA ESQUERDA
		if moves[where_player][3] != '  ':
			button_x = player.center()[0] - player.button_move 
			button_y = player.center()[1]
			#Movimento normal
			if moves[where_player][3] != where_other:
				pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
				if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
					p_move.play()
					player.x = cdt_p_x[moves[where_player][3][0]]
					turn += 1
			#Movimentos especiais
			if moves[where_player][3] == where_other:
				#Pula o piao inimigo e vai reto
				if moves[where_other][3] != '  ':
					button_x = other.center()[0] - other.button_move
					button_y = other.center()[1]
					pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
					if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
						p_move.play()
						player.x = cdt_p_x[moves[where_other][3][0]]
						turn += 1
				#Pula o paio inimigo e vai para um dos lados
				if moves[where_other][3] == '  ':
					#Cima
					if moves[where_other][0] != '  ':
						button_x = other.center()[0]
						button_y = other.center()[1] - other.button_move
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][0][0]]
							player.y = cdt_p_y[moves[where_other][0][1]]
							turn += 1
					#Baixo
					if moves[where_other][2] != '  ':
						button_x = other.center()[0]
						button_y = other.center()[1] + other.button_move
						pg.draw.circle(window,player.button_color,(button_x,button_y),player.button_radius)
						if mouse_pressed and is_over(button_x,button_y,mouse,player.button_radius):
							p_move.play()
							player.x = cdt_p_x[moves[where_other][2][0]]
							player.y = cdt_p_y[moves[where_other][2][1]]
							turn += 1
	
	#Define se o jogador clicou no piao
	if mouse_pressed:
		if is_over(player.center()[0],player.center()[1],mouse,player.button_radius):
			if player.button_pressed == True:
				player.button_pressed = False
			else:
				walls.valid = True
				player.button_pressed = True

	if turn >= 3:
		turn = 1
	return turn    #OPTIMIZAR A FUNCAO DOS MOVIMENTOS

#Define o que aparece no jogo
def Game_window(window, board, player1, player2, mouse, mouse_pressed, turn, cdt_p_x, cdt_p_y, walls, moves, click_button, w_width, w_height, mov_erro, p_move, b_press, win):
	g_texts = sis_texts(1)
	reset = False
	option = 0
	#Coloca o tabuleiro e os pioes na tela
	window.blit(board,(25,25))
	player1.draw(window)
	player2.draw(window)

	#Efetua o movimento dos pioes ou a barreira sendo colocada
	if turn == 1:
		turn = mov_pawn(window, turn, mouse, mouse_pressed, player1, player2,cdt_p_x,cdt_p_y,moves, walls, p_move)

		#So e ativado quando o jogador 1 ganhar
		if where_p(player1.x, player1.y, cdt_p_x, cdt_p_y)[1] == '9':
			reset = end(window, turn, win, w_width, w_height)

		#Caso o jogador 1 nao se mova ele pode botar uma barreira
		if turn == 1:
			turn, moves = put_wall(window, turn, mouse, mouse_pressed,walls,player1,player2,cdt_p_x, cdt_p_y, moves, mov_erro, b_press)

		#Mostra na tela qual jogador deve fazer uma acao
		x = 25
		y = 550
		t_width = g_texts[1].get_width()
		window.blit(g_texts[1],(x, y))
		window.blit(player1.image,(x + 15 + t_width ,y + 5))
		
		#Printa a quantidade de barreiras que o jogador 1 tem
		barriers_text = f'{player1.wall} Barreiras restantes'
		b_r_render = g_texts[0].render(barriers_text, 1, (250,250,250))
		window.blit(b_r_render, (25, 650))
		
	elif turn == 2:
		turn = mov_pawn(window, turn, mouse, mouse_pressed, player1, player2,cdt_p_x,cdt_p_y,moves, walls, p_move)

		#So e ativado quando o jogador 2 ganhar
		if where_p(player2.x, player2.y, cdt_p_x, cdt_p_y)[1] == '1':
			reset = end(window, turn, win, w_width, w_height)

		#Caso o jogador 2 nao se mova ele pode botar uma barreira
		if turn == 2:
			turn, moves = put_wall(window, turn, mouse, mouse_pressed,walls,player1,player2,cdt_p_x, cdt_p_y, moves, mov_erro, b_press)

		#Mostra na tela qual jogador deve fazer uma acao
		window.blit(g_texts[2],(25,550))
		window.blit(player2.image,(410,555))

		#Printa a quantidade de barreiras que o jogador 2 tem
		barriers_text = f'{player2.wall} Barreiras restantes'
		b_r_render = g_texts[0].render(barriers_text, 1, (250,250,250))
		window.blit(b_r_render, (25, 650))

	#Botao para rotacionar a barreira
	t_width = g_texts[3].get_width()
	t_height = g_texts[3].get_height()
	x = 25
	y = 600
	width = t_width + 2
	if put_b(window, x, y, width, t_height, mouse, mouse_pressed, click_button, g_texts[3]):
		if walls.status_wall == '|':
			walls.status_wall = '-'
		else:
			walls.status_wall = '|'

	if walls.status_wall == '|':
		pg.draw.rect(window, (100,100,200), (x + width + 5, y, 10, t_height))
		pg.draw.rect(window, (0,0,0), (x + width + 5, y, 10, t_height), 1)
	elif walls.status_wall == '-':
		pg.draw.rect(window, (100,100,200), (x + width + 5, 615, t_height, 10))
		pg.draw.rect(window, (0,0,0), (x + width + 5, 615, t_height, 10), 1)

	#Printa 'barreira invalida' na tela, so mente se um dos jogadores tentar colocar uma barreira que trave um dos jogadores
	if not walls.valid:
		t_height = g_texts[4].get_height()
		t_width = g_texts[4].get_width()
		x = w_width - (t_width + 100)
		y = 25
		width = t_width + 25
		height = t_height*2 + 10
		pg.draw.rect(window, ((139,0,0)),(x, y, width, height))
		pg.draw.rect(window, (0,0,0), (x, y, width, height), 1)
		window.blit(g_texts[4], (x + width/2 - t_width/2, y + height/4 - t_height/2))
		t_width = g_texts[5].get_width()
		window.blit(g_texts[5], (x + width/2 - t_width/2, y + height*3/4 - t_height/2))

	#Botao de desistencia (ele consede a vitoria ao outro jogador)
	t_width = g_texts[6].get_width()
	t_height = g_texts[6].get_height()
	x = w_width - (t_width + 10)
	y = w_height - (t_height + 5)
	width = t_width + 2
	if put_b(window, x, y, width, t_height, mouse, mouse_pressed, click_button, g_texts[6]):
		reset = end(window, turn, win, w_width, w_height)

	#Essa condicao so e acionada caso um jogador ganhe ou alguem desistiu
	if reset:
		option, turn, moves = reset_game(player1, player2, walls, cdt_p_x, cdt_p_y)

	#A tela e atualizada
	pg.display.update()
	return option, turn, moves

#--------------------------------------FUNCOES DA JANELA DO MANUAL-------------------------------------
#Coloca os textos explicativos na tela
def print_text(stats, window, ma_texts, w_width, w_height):
	if stats == 'moves':
	#Coloca o manual dos dos movimentos normais na tela
		try:
			open_file = open('movimentos.txt', 'r')
			line = open_file.readline()
			text = ma_texts[0].render(line[:-1], 1, (255,255,255))
			t_width = text.get_width()
			t_height = text.get_height()
			x = w_width/2 - t_width/2
			y = 75
			window.blit(text,(x, y))
			y += t_height
			while line != '':
				line = open_file.readline()
				text = ma_texts[0].render(line[:-1], 1, (255,255,255))
				t_width = text.get_width()
				x = w_width/2 - t_width/2
				y += t_height
				t_height = text.get_height()
				window.blit(text,(x, y))
			open_file.close()
		except FileNotFoundError:
			print('O arquivo da explicacao dos movimentos nao foi encontrado')

	elif stats == 'especial moves':
		#Coloca o manual dos dos movimentos especiais na tela
		try:
			open_file = open('movimentos especiais.txt', 'r')
			line = open_file.readline()
			text = ma_texts[0].render(line[:-1], 1, (255,255,255))
			t_width = text.get_width()
			t_height = text.get_height()
			x = w_width/2 - t_width/2
			y = 75
			window.blit(text,(x, y))
			y += t_height
			while line != '':
				line = open_file.readline()
				text = ma_texts[0].render(line[:-1], 1, (255,255,255))
				t_width = text.get_width()
				x = w_width/2 - t_width/2
				y += t_height
				t_height = text.get_height()
				window.blit(text,(x, y))
			open_file.close()
		except FileNotFoundError:
			print('O arquivo da explicacao dos movimentos especiais nao foi encontrado')
	#Else foi usado aqui para que o objetivo do jogo fique na tela mesmo quando a variavel stats for ''
	else:
		#Coloca o manual do objetivo do jogo na tela
		try:
			open_file = open('objetivo do jogo.txt', 'r')
			line = open_file.readline()
			text = ma_texts[0].render(line[:-1], 1, (255,255,255))
			t_width = text.get_width()
			t_height = text.get_height()
			x = w_width/2 - t_width/2
			y = 75
			window.blit(text,(x, y))
			y += t_height
			while line != '':
				line = open_file.readline()
				text = ma_texts[0].render(line[:-1], 1, (255,255,255))
				t_width = text.get_width()
				x = w_width/2 - t_width/2
				y += t_height
				t_height = text.get_height()
				window.blit(text,(x, y))
			open_file.close()
		except FileNotFoundError:
			print('O arquivo da explicacao do objetivo do jogo nao foi encontrado')

#Define o que parece na tela do manual
def Manual_window(stats, option, window, w_width, w_height, mouse, mouse_pressed, click_button):
	ma_texts = sis_texts(3)
	can_click = True

	print_text(stats, window, ma_texts, w_width, w_height)

	#Cria a caixa onde os textos vao aparecer
	width = 800
	height = 500
	x = 25
	y = 15
	side_1 = 50
	side_2 = 500
	pg.draw.rect(window, (0,0,0), (x, y, side_1, side_2))
	pg.draw.rect(window, (0,0,0), (x, y, width + side_1, side_1))
	pg.draw.rect(window, (0,0,0), (x, y + height, width + side_1, side_1))
	pg.draw.rect(window, (0,0,0), (x + width, y, side_1, side_2))

	#Botao para mostrar o texto relativo ao objetivo do jogo
	if stats == 'moves' and can_click:
		width = ma_texts[4].get_width() + 5
		height = ma_texts[4].get_height() + 2
		x = w_width*4/10 - width/2
		y = w_height*5/6
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, ma_texts[4]):
			can_click = False
			stats = ''
	elif stats == 'especial moves' and can_click:
		width = ma_texts[4].get_width() + 5
		height = ma_texts[4].get_height() + 2
		x = w_width*8/10 - width/2
		y = w_height*5/6
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, ma_texts[4]):
			can_click = False
			stats = ''
	
	#Botao para mostrar o texto relativo os movimentos especiais
	if stats != 'especial moves' and can_click:
		width = ma_texts[3].get_width() + 5
		height = ma_texts[3].get_height() + 2
		x = w_width*8/10 - width/2
		y = w_height*5/6
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, ma_texts[3]):
			can_click = False
			stats = 'especial moves'

	#Botao para mostrar o texto relativo os movimentos
	if stats != 'moves' and can_click:
		width = ma_texts[2].get_width() + 5
		height = ma_texts[2].get_height() + 2
		x = w_width*4/10 - width/2
		y = w_height*5/6
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, ma_texts[2]):
			can_click = False
			stats = 'moves'

	#Botao para voltar ao menu
	width = ma_texts[1].get_width() + 5
	height = ma_texts[1].get_height() + 2
	x = w_width/10 - width/2
	y = w_height*5/6
	if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, ma_texts[1]):
		option = ''
		stats = ''
		sleep(0.2)

	pg.display.update()
	return option, stats

#--------------------------------------FUNCOES DA JANELA DAS CONFIGURACOES-----------------------------
#Redefine o que aparece no backgound
def change_bg(stats, window, w_width, w_height, click_button, bg, mouse, mouse_pressed, c_texts):
	#Abre o arquivo das imagens
	open_file = open('imagens.txt', 'r')
	lines = open_file.readlines()

	#Caracteristicas de todos os botoes
	width = c_texts[13].get_width()
	height = w_height/10
	text = c_texts[0].render('Em uso!', 1, (0,75,150))
	space = 50
	images = [
	'background/background_1.png\n','background/background_2.png\n','background/background_3.png\n',
	'background/background_4.png\n','background/background_5.png\n','background/background_6.png\n',
	'background/background_7.png\n','background/background_8.png\n','background/background_9.png\n'
			 ]
	n = 13

	#Primeira linha
	y = w_height/7
	x = w_width*2/7 - width + space

	try:
		for image in images[:3]:
			if lines[1] != image:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + image + lines[2] + lines[3]
					change.write(write)
					change.close()
					bg = pg.image.load(image[:-1])
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += w_width*2/7
			n += 1

		#Segunda linha
		y = w_height*3/7
		x = w_width*2/7 - width + space

		for image in images[3:6]:
			if lines[1] != image:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + image + lines[2] + lines[3]
					change.write(write)
					change.close()
					bg = pg.image.load(image[:-1])
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += w_width*2/7
			n += 1	

		#Terceira linha
		y = w_height*5/7
		x = w_width*2/7 - width + space

		for image in images[6:]:
			if lines[1] != image:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + image + lines[2] + lines[3]
					change.write(write)
					change.close()
					bg = pg.image.load(image[:-1])
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += w_width*2/7
			n += 1
	except FileNotFoundError:
		print('----------------------------------AVISO------------------------------------------')
		print(f'As imagens originais do jogo nao estao dentro da pasta correta ({image[:-1]}).')
		print('Ou nao existem.')
		print('----------------------------------AVISO------------------------------------------')

	#Voltar
	height = w_height/10
	width = w_width/7
	x = w_width*4/7 - width
	y = w_height*6/7
	if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[5]):
		stats = ''

	open_file.close()
	return stats, bg

#Redefine qual piao que sera usado
def change_p(stats, window, w_width, w_height, click_button, player1, player2, mouse, mouse_pressed, c_texts):
	open_file = open('imagens.txt', 'r')
	lines = open_file.readlines()

	#Caracteristicas de todos os botoes
	width = c_texts[27].get_width() + 5
	height = w_height/10
	text = c_texts[0].render('Em uso!', 1, (0,75,150))
	space = 30
	images =[
			'player/crown1.png\n','player/crown2.png\n','player/queen1.png\n','player/queen2.png\n',
			'player/pawn1.png\n','player/pawn2.png\n','player/pawn3.png\n','player/pawn4.png\n'
			]

	#------------------Jogador 1-------------------
	t_width = c_texts[22].get_width()
	t_height = c_texts[22].get_height()
	x = w_width/2 - t_width/2
	y = w_width/100
	window.blit(c_texts[22],(x, y))
	window.blit(player1.image,(x + t_width, y + t_height/2 - 32/2))
	n = 24

	#PRIMEIRA LINHA
	y = w_height*5/60
	x = w_width/2 - (width*4 + space*3)/2
	try:
		for image in images[:4]:
			if lines[2] != image and lines[3] != image[:-1]:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + lines[1] + image + lines[3]
					change.write(write)
					change.close()
					pawn1 = pg.image.load(image[:-1])
					player1.image = pawn1
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += width + space
			n += 1

		#SEGUNDA LINHA
		y = w_height*15/60
		x = w_width/2 - (width*4 + space*3)/2

		for image in images[4:]:
			if lines[2] != image and lines[3] != image[:-1]:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + lines[1] + image + lines[3]
					change.write(write)
					change.close()
					pawn1 = pg.image.load(image[:-1])
					player1.image = pawn1
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += width + space
			n += 1

		#---------------------------Jogador 2------------------------------
		t_width = c_texts[23].get_width()
		t_height = c_texts[23].get_height()
		x = w_width/2 - t_width/2
		y = w_width*30/100
		window.blit(c_texts[23],(x, y))
		window.blit(player2.image,(x + t_width, y + t_height/2 - 32/2))

		#PRIMEIRA LINHA
		y = w_height*30/60
		x = w_width/2 - (width*4 + space*3)/2
		n = 24

		for image in images[:4]:
			if lines[2] != image and lines[3] != image[:-1]:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + lines[1] + lines[2] + image[:-1]
					change.write(write)
					change.close()
					pawn1 = pg.image.load(image[:-1])
					player2.image = pawn1
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += width + space
			n += 1

		#SEGUNDA LINHA
		y = w_height*40/60
		x = w_width/2 - (width*4 + space*3)/2

		for image in images[4:]:
			if lines[2] != image and lines[3] != image[:-1]:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = lines[0] + lines[1] + lines[2] + image[:-1]
					change.write(write)
					change.close()
					pawn1 = pg.image.load(image[:-1])
					player2.image = pawn1
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += width + space
			n += 1
	except FileNotFoundError:
		print('----------------------------------AVISO------------------------------------------')
		print(f'As imagens originais do jogo nao estao dentro da pasta correta ({image[:-1]}).')
		print('Ou nao existem.')
		print('----------------------------------AVISO------------------------------------------')

	#Voltar
	width = w_width/7
	x = w_width*4/7 - width
	y = w_height*6/7 
	if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[5]):
		stats = ''

	return stats

#Redefine o tabuleiro que o jogo usa
def change_brd(stats, window, w_width, w_height, click_button, brd, mouse, mouse_pressed, c_texts):
	#Abre o arquivo das imagens
	open_file = open('imagens.txt', 'r')
	lines = open_file.readlines()

	#Caracteristicas de todos os botoes
	width = c_texts[11].get_width()
	height = w_height/10
	text = c_texts[0].render('Em uso!', 1, (0,75,150))
	space = 50
	images =[
			'tabuleiro/tab1.png\n','tabuleiro/tab2.png\n','tabuleiro/tab3.png\n',
			'tabuleiro/tab4.png\n','tabuleiro/tab5.png\n','tabuleiro/tab6.png\n'
			]

	#Primeira linha
	y = w_height*5/60
	x = w_width*2/7 - width + space
	n = 7

	try:
		for image in images[:3]:
			if lines[0] != image:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = image + lines[1] + lines[2] + lines[3]
					change.write(write)
					change.close()
					brd = pg.image.load(image[:-1])
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += w_width*2/7
			n += 1

		#Segunda linha
		y = w_height*13/60
		x = w_width*2/7 - width + space

		for image in images[3:]:
			if lines[0] != image:
				if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[n]):
					change = open('imagens.txt', 'w')
					write = image + lines[1] + lines[2] + lines[3]
					change.write(write)
					change.close()
					brd = pg.image.load(image[:-1])
			else:
				pg.draw.rect(window, (255,0,0), (x, y, width, height))
				pg.draw.rect(window, (0,0,0), (x, y, width, height), 3)
				t_width = text.get_width()
				t_height = text.get_height()
				window.blit(text,(x + width/2 - t_width/2, y + height/2 - t_height/2))
			x += w_width*2/7
			n += 1
	except FileNotFoundError:
		print('----------------------------------AVISO------------------------------------------')
		print(f'As imagens originais do jogo nao estao dentro da pasta correta ({image[:-1]}).')
		print('Ou nao existem.')
		print('----------------------------------AVISO------------------------------------------')

	#Coloca o tabuleiro atual na tela
	teste_brd = pg.transform.scale(brd,(450,450))
	x = w_width/2 - 450/2
	y = w_height*20/60
	window.blit(teste_brd,(x, y))

	#Voltar
	height = w_height/10
	width = w_width/7
	x = w_width/20
	y = w_height*5/6
	if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[5]):
		stats = ''

	open_file.close()
	return stats, brd

#Define o volume geral do jogo
def change_volume(volume, conf_sounds):
	change = float(volume[:-1])/100
	pg.mixer.Sound.set_volume(conf_sounds[0], change)
	pg.mixer.Sound.set_volume(conf_sounds[1], change*0.7)
	pg.mixer.Sound.set_volume(conf_sounds[2], change)
	pg.mixer.Sound.set_volume(conf_sounds[3], change)
	pg.mixer.Sound.set_volume(conf_sounds[4], change)
	pg.mixer.music.set_volume(change)

#Define o que aparece na tela de configuracao
def Config_window(option, stats, window, w_width, w_height, click_button, brd, bg, player1, player2, mouse, mouse_pressed, conf_sounds):
	c_texts = sis_texts(4)
	can_click = True
	if stats == 'background':
		stats, bg = change_bg(stats, window, w_width, w_height, click_button, bg, mouse, mouse_pressed, c_texts)
	elif stats == 'pawn':
		stats = change_p(stats, window, w_width, w_height, click_button, player1, player2, mouse, mouse_pressed, c_texts)
	elif stats == 'board':
		stats, brd = change_brd(stats, window, w_width, w_height, click_button, brd, mouse, mouse_pressed, c_texts)
	else:
		#Confg do volume geral
		color = (105,89,205)
		width = w_width*4/10
		height = 5
		t_width = c_texts[1].get_width() + 5
		t_height = c_texts[1].get_height()
		x = w_width/2 - width/2 + t_width/2
		y = w_height*1.5/10
		pg.draw.rect(window, color, (x, y, width, height))
		window.blit(c_texts[1],(x - t_width, y - t_height/2))
		volumes = ['0%', '20%', '40%', '60%', '80%', '100%']
		_volume_ = pg.mixer.music.get_volume()
		b_width = 30
		b_height = 30
		y -= b_height/2
		n = 1
		for volume in volumes:
			text = c_texts[0].render(volume, 2,(255,255,0))
			t_height = text.get_height()
			window.blit(text, (x, y - (height + t_height)))
			#OBS: o valor do som que a propria funcao do pygame returna possue uma margem de erro
			if _volume_ + 0.01 >= float(volume[:-1])/100 and _volume_ - 0.01 <= float(volume[:-1])/100:
				pg.draw.rect(window, (165,42,42), (x, y, b_width, b_height))
				pg.draw.rect(window, (0,191,255), (x, y, b_width, b_height), 2)
			else:
				if put_b(window, x, y, b_width, b_height, mouse, mouse_pressed, click_button):
					change_volume(volume, conf_sounds)
			x += width/5

		#confg da musica
		t_width = c_texts[6].get_width()
		x = w_width/2 - t_width/2
		y = w_height*2/10
		window.blit(c_texts[6], (x, y))
		width = w_width/10
		height = w_height/18
		space = 50
		on = c_texts[0].render('ON',1,(0,0,0))
		x = w_width/2 - width - space/2
		y = w_height*2.8/10
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, on):
			pg.mixer.music.play(-1)
		off = c_texts[0].render('OFF',1,(0,0,0))
		x = w_width/2 + space/2
		y = w_height*2.8/10
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, off):
			pg.mixer.music.stop()

		#Caracteristicas gerais dos botoes
		space = 30
		width = 350
		height = 70

		#Botao para entrar nas opcoes de plano de fundo
		t_width = c_texts[2].get_width()
		t_height = c_texts[2].get_height()
		x = w_width/2 - width/2
		y = w_height*4/5 - space*3 - height*3
		L_stats = ['background', 'pawn', 'board', '']
		for i in range (4):
			if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, c_texts[i + 2]):
				stats = L_stats[i]
				if stats == '':
					option = ''
			y += space + height

	#Atualiza a tela
	pg.display.update()
	return option, brd, bg, stats

#--------------------------------------FUNCAO DA JANELA DO MENU--------------------------------------
#Define o que aparece no menu
def Menu_window(w_width, w_height, window, option, brd, bg, pawn1, pawn2, mouse, mouse_pressed, click_button):
	m_texts = sis_texts(2)
	#Texto do inicio do jogo
	t_width = m_texts[0].get_width()
	y = 70
	window.blit(m_texts[0],(w_width/2 - t_width/2, y))

	#Espaco entre os botoes e o seu tamanho
	space = 30
	width = 350
	height = 70

	axillary = 0

	#Botao para iniciar o jogo
	x = w_width/2 - width/2
	y = 230
	for i in range(4):
		if put_b(window, x, y, width, height, mouse, mouse_pressed, click_button, m_texts[axillary+1]):
			option = axillary
			sleep(0.2)
		axillary += 1
		y += space + height
	pg.display.update()
	return option, brd, bg, pawn1, pawn2

#--------------------------------------FUNCAO PRINCIAPAL----------------------------------------------
def Start():
	#Variaveis que mudarao apos entrar no loop princiapal
	stats = ''
	moves = r_movs()
	play = True
	mouse_pressed = False
	option = ''
	turn = 1

	#Inicializa a musica de fundo e carrega os outros efeitos sonoros
	stop1, p_move, click_button, mov_erro, b_press, win = load_sounds()
	if not stop1:
		pg.mixer.Sound.set_volume(click_button ,0.7)
		pg.mixer.music.play(-1)
		conf_sounds = [p_move, click_button, mov_erro, b_press, win]


	#Dicionario das coordenadas das coordenadas cdt = coodinate
	cdt_p_x = {'A': 69, 'B': 116, 'C': 164, 'D': 211, 'E': 259, 'F': 306, 'G': 353, 'H': 401, 'I':448}
	cdt_p_y = {'1': 70, '2': 117, '3': 165, '4': 212, '5': 259, '6': 305, '7': 353, '8': 401, '9':449}

	#imagens para o back ground, tabuleiro, piao do jogador 1 e do jogador 2
	stop2, brd, bg, pawn1, pawn2 = load_images()

	#Criacao dos objetos
	walls = wall()
	player1 = pawn(cdt_p_x['E'],cdt_p_y['1'],pawn1)
	player2 = pawn(cdt_p_x['E'],cdt_p_y['9'],pawn2)

	#Define a janela do jogo
	w_width = 900
	w_height = 700
	window = pg.display.set_mode((w_width, w_height))
	pg.display.set_caption('Bloqueio!')
	try:
		icon = pg.image.load('icon.png')
		pg.display.set_icon(icon)
	except:
		print('----------------------------------AVISO------------------------------------------')
		print('Imagem do icone nao foi encontrada!')
		print('----------------------------------AVISO------------------------------------------')
	if stop1 or stop2:
		play = False
	#Loop primario
	while play:
		#print('stats: ', stats)
		#print('option: ', option)
		#print('turn: ', turn)
		#print('------------------')

		#Define o plano de fundo
		window.blit(bg,(0,0))

		#Nao permite que o botao do mouse fique permamentemente apertado
		if mouse_pressed == True:
			mouse_pressed = False

		for event in pg.event.get():
			#Defini qual posicao o mouse esta, e diz se algum de seus botoes foi apertado
			mouse = pg.mouse.get_pos()
			if event.type == pg.MOUSEBUTTONDOWN:
				mouse_pressed = True
			if event.type == pg.QUIT:
				play = False

		#Jogar
		if option == 0:
			option, turn, moves = Game_window(window, brd, player1, player2, mouse, mouse_pressed, turn, cdt_p_x, cdt_p_y, walls,\
											  moves, click_button, w_width, w_height, mov_erro, p_move, b_press, win)
		#Manual
		elif option == 1:
			option, stats = Manual_window(stats, option, window, w_width, w_height, mouse, mouse_pressed, click_button)
		#Configuracoes
		elif option == 2:
			option, brd, bg, stats = Config_window(option, stats, window, w_width, w_height, click_button, brd, bg,\
			                                                     player1, player2, mouse, mouse_pressed, conf_sounds)
		#Desligar
		elif option == 3:
			play = False

		#MENU
		else:
			option, brd, bg, pawn1, pawn2 = Menu_window(w_width, w_height, window, option, brd, bg, pawn1, pawn2, mouse, mouse_pressed,\
														click_button)

	#Fecha o programa
	pg.quit()

if __name__ == '__main__':
	Start()