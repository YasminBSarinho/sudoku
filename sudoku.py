import sys
import pygame as pg
import random


pg.font.init()
fonte = pg.font.SysFont(None, 50)
fonteSecundaria = pg.font.SysFont('Arial', 30)
pg.display.set_caption("Sudoku")


tamanho_da_tela = 765, 565
tela = pg.display.set_mode(tamanho_da_tela)


cor_fundo = (47, 46, 46)
cor_grade = (219, 216, 227)
cor_texto = (181, 181, 181)


tabuleiros = [
   [
       [5, 3, 0, 0, 7, 0, 0, 0, 0],
       [6, 0, 0, 1, 9, 5, 0, 0, 0],
       [0, 9, 8, 0, 0, 0, 0, 6, 0],
       [8, 0, 0, 0, 6, 0, 0, 0, 3],
       [4, 0, 0, 8, 0, 3, 0, 0, 1],
       [7, 0, 0, 0, 2, 0, 0, 0, 6],
       [0, 6, 0, 0, 0, 0, 2, 8, 0],
       [0, 0, 0, 4, 1, 9, 0, 0, 5],
       [0, 0, 0, 0, 8, 0, 0, 7, 9]
   ],
   [
       [0, 0, 8, 0, 0, 0, 0, 0, 0],
       [5, 0, 0, 0, 0, 0, 0, 4, 0],
       [0, 0, 0, 6, 0, 0, 0, 0, 9],
       [6, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 4, 0, 0, 0, 0],
       [0, 0, 4, 0, 0, 3, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 8, 0, 0],
       [0, 0, 0, 0, 0, 0, 7, 0, 3],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ],
   [
       [0, 0, 0, 8, 0, 4, 0, 0, 3],
       [0, 0, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 0, 3, 0, 0, 0, 0],
       [0, 0, 4, 0, 0, 0, 0, 5, 0],
       [0, 0, 0, 2, 0, 0, 0, 6, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 7, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 6, 8, 0],
       [5, 0, 0, 0, 0, 0, 0, 0, 0]
   ],
   [
       [0, 0, 0, 1, 2, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 8, 0],
       [0, 0, 7, 0, 0, 0, 5, 0, 0],
       [3, 0, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 0, 0, 0, 7, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 7, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 6, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 4, 0]
   ]
]


tabuleiro_resposta = [
   [
       [5, 3, 4, 6, 7, 8, 9, 1, 2],
       [6, 7, 2, 1, 9, 5, 3, 4, 8],
       [1, 9, 8, 3, 4, 2, 5, 6, 7],
       [8, 5, 9, 7, 6, 1, 4, 2, 3],
       [4, 2, 6, 8, 5, 3, 7, 9, 1],
       [7, 1, 3, 9, 2, 4, 8, 5, 6],
       [9, 6, 1, 5, 3, 7, 2, 8, 4],
       [2, 8, 7, 4, 1, 9, 6, 3, 5],
       [3, 4, 5, 2, 8, 6, 1, 7, 9]
   ],


   [
       [1, 4, 8, 9, 3, 2, 6, 7, 5],
       [5, 9, 6, 7, 8, 1, 3, 4, 2],
       [7, 3, 2, 6, 5, 4, 1, 8, 9],
       [6, 7, 3, 1, 2, 9, 5, 6, 4],
       [8, 1, 9, 5, 4, 6, 2, 3, 7],
       [2, 5, 4, 8, 7, 3, 9, 1, 6],
       [4, 6, 7, 3, 1, 5, 8, 9, 2],
       [9, 8, 5, 2, 6, 7, 7, 2, 3],
       [3, 2, 1, 4, 9, 8, 4, 5, 1]
   ],
   [
       [2, 1, 6, 8, 9, 4, 5, 7, 3],
       [3, 4, 8, 5, 6, 7, 2, 1, 9],
       [7, 5, 9, 1, 3, 2, 8, 6, 4],
       [1, 6, 4, 9, 8, 3, 7, 5, 2],
       [8, 9, 7, 2, 5, 1, 4, 6, 3],
       [6, 2, 3, 4, 7, 5, 1, 9, 8],
       [4, 8, 1, 7, 2, 6, 9, 3, 5],
       [9, 7, 5, 3, 1, 9, 6, 8, 2],
       [5, 3, 2, 6, 4, 8, 3, 2, 1]
   ],
   [
       [6, 5, 4, 1, 2, 7, 8, 9, 3],
       [1, 3, 2, 4, 9, 5, 6, 8, 7],
       [9, 8, 7, 3, 6, 8, 5, 2, 4],
       [3, 1, 8, 2, 5, 4, 3, 7, 9],
       [5, 6, 9, 8, 3, 1, 7, 2, 4],
       [2, 4, 6, 9, 7, 8, 1, 3, 5],
       [8, 7, 3, 6, 4, 9, 2, 5, 1],
       [4, 9, 5, 7, 1, 6, 2, 3, 8],
       [7, 2, 1, 5, 8, 3, 9, 4, 6]
   ]
]


tabuleiro_escolhido = random.randint(0, len(tabuleiros) - 1)
tabuleiro_atual = tabuleiros[tabuleiro_escolhido]
tabuleiro_resposta_atual = tabuleiro_resposta[tabuleiro_escolhido]


celula_selecionada = None




def fundo():
   tela.fill(pg.Color(cor_fundo))
   pg.draw.rect(tela, pg.Color(cor_grade), pg.Rect(15, 15, 540, 540), 2)
   for i in range(10):
       largura_linha = 3 if i % 3 == 0 else 1
       pg.draw.line(tela, pg.Color(cor_grade), (i * (540 // 9) + 15, 15), (i * (540 // 9) + 15, 555), largura_linha)
       pg.draw.line(tela, pg.Color(cor_grade), (15, i * (540 // 9) + 15), (555, i * (540 // 9) + 15), largura_linha)




def mostrar_numeros():
   offset_grade = 33
   linha = 0
   for i in range(9):
       coluna = -1
       for j in range(9):
           coluna += 1
           valor = tabuleiro_atual[i][j]
           numero = fonte.render(str(valor), True, pg.Color(cor_texto))
           if valor == 0:
               continue
           tela.blit(numero, pg.Vector2((coluna * 60) + offset_grade + 2, (linha * 60) + offset_grade - 3))
       linha += 1




def quadrante_selecionado(tabuleiro_data, x, y):
   quadrante = []
   for i in range(3):
       for j in range(3):
           quadrante.append(tabuleiro_data[(x // 3) * 3 + i][(y // 3) * 3 + j])
   return quadrante




def verificar(tabuleiro, linha, coluna, numero):
   for i in range(9):
       if tabuleiro[linha][i] == numero or tabuleiro[i][coluna] == numero:
           return False
   linha_inicial, coluna_inicial = 3 * (linha // 3), 3 * (coluna // 3)
   for i in range(3):
       for j in range(3):
           if tabuleiro[linha_inicial + i][coluna_inicial + j] == numero:
               return False
   return True




def verificar_solucao():
   for i in range(9):
       for j in range(9):
           if tabuleiro_atual[i][j] != tabuleiro_resposta_atual[i][j]:
               return False
   return True




def desenho_botao():
   largura = 150
   altura = 50
   posicao = (600, 15)
   pg.draw.rect(tela, pg.Color(cor_grade), pg.Rect(posicao[0], posicao[1], largura, altura))
   texto = fonte.render("Dica", True, pg.Color("black"))
   tela.blit(texto, (posicao[0] + 10, posicao[1] + 15))




def obter_ajuda(tabuleiro_atual, linha, coluna):
   if tabuleiro_atual[linha][coluna] == 0:
       num = tabuleiro_resposta_atual[linha][coluna]
       return num
   return None




def botao_ajuda():
   posicao_mouse = pg.mouse.get_pos()
   if celula_selecionada is not None:
       if celula_selecionada is not None:
           linha, coluna = celula_selecionada
           if tabuleiro_atual[linha][coluna] == 0:
               ajuda = obter_ajuda(tabuleiro_atual, linha, coluna)
               if ajuda is not None:
                   tabuleiro_atual[linha][coluna] = ajuda




def lidar_com_entrada():
   global celula_selecionada
   for evento in pg.event.get():
       if evento.type == pg.QUIT:
           pg.quit()
           sys.exit()
       elif evento.type == pg.MOUSEBUTTONDOWN:
           x, y = pg.mouse.get_pos()
           if 15 <= x <= 555 and 15 <= y <= 555:
               celula_selecionada = ((y - 15) // (540 // 9), (x - 15) // (540 // 9))
           elif 600 <= x <= 750 and 15 <= y <= 65:
               botao_ajuda()
       elif evento.type == pg.KEYDOWN and celula_selecionada is not None:
           tecla = evento.unicode
           if tecla.isdigit() and 1 <= int(tecla) <= 9:
               linha, coluna = celula_selecionada
               num = int(tecla)
               if verificar(tabuleiro_atual, linha, coluna, num):
                   tabuleiro_atual[linha][coluna] = num
               if verificar_solucao():
                   tabuleiro_atual[linha][coluna] = num
           elif tecla == "h" or tecla == "H":
               linha, coluna = celula_selecionada
               ajuda = obter_ajuda(tabuleiro_atual, linha, coluna)
               if ajuda is not None:
                   tabuleiro_atual[linha][coluna] = ajuda




def mostrar_tela():
   lidar_com_entrada()
   fundo()
   mostrar_numeros()
   desenho_botao()


   if verificar_solucao():
       largura = 200
       altura = 50
       posicao = (600, 15)
       pg.draw.rect(tela, pg.Color("green"), pg.Rect(posicao[0], posicao[1], largura, altura))
       texto = fonteSecundaria.render("Parabéns!", True, pg.Color("white"))
       tela.blit(texto, (posicao[0] + 10, posicao[1] + 10))
   if celula_selecionada is not None:
       x, y = celula_selecionada
       pg.draw.rect(tela, pg.Color((255, 157, 200)), (y * (540 // 9) + 15, x * (540 // 9) + 15, 540 // 9, 540 // 9), 2)


   pg.display.flip()




rodando = True
while rodando:
   mostrar_tela()

