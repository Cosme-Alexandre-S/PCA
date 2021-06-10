import pygame
import pygame.font
import  main

pygame.init()
def quantidadejogador(quant):
     op = quant
     print (op)
     return op


def quantidadejogador2(quant):
    op = quant
    print(op)
    return op


preto = (0,0,0)
def text_botoes(texto, fonte):#cria os textos dos botões
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

letras = pygame.image.load('menu.jpeg')
virusvacina = pygame.image.load('vacina.jpeg')

LARGURA, ALTURA = 1024, 740
display = pygame.display.set_mode([LARGURA, ALTURA])#criando janela
pygame.display.set_caption("Menu")#mudando nome da janela
size = [110,50]

display.fill([0,0,0])  # preenchendo a janela de cor
display.blit(letras, (main.center_x(letras),-280))
display.blit(virusvacina, (main.center_x(virusvacina),170))

pos_1 = [LARGURA/2 - size[0]/2 ,ALTURA/2 - size[1]/2+50]
botao1 = pygame.Rect(pos_1,size)
pygame.draw.rect(display,[36, 128, 20], botao1)
textobotao = pygame.font.Font('freesansbold.ttf', 18)
textSurf, textRect = text_botoes("Iniciar", textobotao)
textRect.center = ((pos_1[0] + size[0]/2), (pos_1[1] + size[1]/2))
display.blit(textSurf, textRect)
pos_2 = [LARGURA/2 - size[0]/2 ,ALTURA/2 - size[1]/2 + 120]
botao2 = pygame.Rect(pos_2,size)
pygame.draw.rect(display, [36, 128, 20], botao2)
textobotao = pygame.font.Font('freesansbold.ttf', 18)
textSurf, textRect = text_botoes("Sair", textobotao)
textRect.center = ((pos_2[0] + size[0]/2), (pos_2[1] + size[1]/2))
display.blit(textSurf, textRect)



# def telaopcoes():#construindo a segunda tela (opcões da quantidade de jogadores)
#     display = pygame.display.set_mode([840, 480])
#     pygame.display.set_caption("Opcões")
#     display.fill([0, 0, 0])
#     virusvacina = pygame.image.load('vacina.jpeg')
#     display.blit(virusvacina, (350, 120))
#     letras2 = pygame.image.load('opcoes.jpeg')
#     display.blit(letras2, (-210, -300))
#
#     botao1op = pygame.Rect(150, 340, 110, 50)
#     pygame.draw.rect(display, [36, 128, 20], botao1op)
#     textobotao = pygame.font.Font('freesansbold.ttf', 18)
#     textSurf, textRect = text_botoes("1 jogador", textobotao)
#     textRect.center = ((150 + (110/2)), (340 + (50/2)))
#     display.blit(textSurf, textRect)
#
#     botao2op = pygame.Rect(300, 340, 110, 50)
#     pygame.draw.rect(display, [36, 128, 20], botao2op)
#     textobotao = pygame.font.Font('freesansbold.ttf', 18)
#     textSurf, textRect = text_botoes("2 jogadores", textobotao)
#     textRect.center = ((300 + (110 / 2)), (340 + (50 / 2)))
#     display.blit(textSurf, textRect)
#
#     botao3op = pygame.Rect(450, 340, 110, 50)
#     pygame.draw.rect(display, [36, 128, 20], botao3op)
#     textobotao = pygame.font.Font('freesansbold.ttf', 18)
#     textSurf, textRect = text_botoes("3 jogadores", textobotao)
#     textRect.center = ((450 + (110 / 2)), (340 + (50 / 2)))
#     display.blit(textSurf, textRect)
#
#     botao4op = pygame.Rect(600, 340, 110, 50)
#     pygame.draw.rect(display, [36, 128, 20], botao4op)
#     textobotao = pygame.font.Font('freesansbold.ttf', 18)
#     textSurf, textRect = text_botoes("4 jogadores", textobotao)
#     textRect.center = ((600 + (110 / 2)), (340 + (50 / 2)))
#     display.blit(textSurf, textRect)


    # if botao1op.collidepoint(pygame.mouse.get_pos()):
    #     print("botao1")
    #     if pygame.mouse.get_pressed()[0]:
    #         quantidadejogador(1)
    # elif botao2op.collidepoint(pygame.mouse.get_pos()):
    #     print("botao2")
    #     if pygame.mouse.get_pressed()[0]:
    #         quantidadejogador(2)
    # elif botao3op.collidepoint(pygame.mouse.get_pos()):
    #     if pygame.mouse.get_pressed()[0]:
    #         quantidadejogador(3)
    # elif botao4op.collidepoint(pygame.mouse.get_pos()):
    #     if pygame.mouse.get_pressed()[0]:
    #         quantidadejogador(4)


gameLoop = True

if __name__ == "__main__":
     while gameLoop:


          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    gameLoop = False
               if pygame.mouse.get_pressed()[0]:
                    if botao2.collidepoint(pygame.mouse.get_pos()):
                         gameLoop = False

                    elif botao1.collidepoint(pygame.mouse.get_pos()):
                        main.mainloop()





                          

          pygame.display.update()









