# Materiał pochodzi z lekcji Real Python https://realpython.com/lessons/basic-pygame-program/
# importowanie i inicjowanie  środowiska
import pygame
from tic_tac_toe import board_status
pygame.init()
white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)
coordinates = "By Paulina and Arek"
#formatowanie rodzaju fontu dla konkretnego obiektów
font_obj = pygame.font.Font('freesansbold.ttf', 60)  
title_obj = pygame.font.Font('freesansbold.ttf', 60)
comments_obj = pygame.font.Font('freesansbold.ttf', 40)
#ustalenie obiektów
title_signe = title_obj.render("TIC TAC TOE", True, white, blue)
position_1_signe = font_obj.render("X", True, green, blue)
position_2_signe = font_obj.render(board_status[1], True, green, blue)
position_3_signe = font_obj.render(board_status[2], True, green, blue)
position_4_signe = font_obj.render(board_status[3], True, green, blue)
position_5_signe = font_obj.render("O", True, green, blue)
position_6_signe = font_obj.render(board_status[5], True, green, blue)
position_7_signe = font_obj.render(board_status[6], True, green, blue)
position_8_signe = font_obj.render(board_status[7], True, green, blue)
position_9_signe = font_obj.render("X", True, green, blue)
coordinates_input = comments_obj.render(coordinates, True, white, blue)
#pozycjonowanie obiektów
title_obj = title_signe.get_rect()
title_obj.center = (250, 50)
position_1_signe_obj = position_1_signe.get_rect()
position_1_signe_obj.center = (150, 150)
position_2_signe_obj = position_2_signe.get_rect()
position_2_signe_obj.center = (250, 150)
position_3_signe_obj = position_3_signe.get_rect()
position_3_signe_obj.center = (350, 150)
position_4_signe_obj = position_4_signe.get_rect()
position_4_signe_obj.center = (150, 250)
position_5_signe_obj = position_5_signe.get_rect()
position_5_signe_obj.center = (250, 250)
position_6_signe_obj = position_6_signe.get_rect()
position_6_signe_obj.center = (350, 250)
position_7_signe_obj = position_7_signe.get_rect()
position_7_signe_obj.center = (150, 350)
position_8_signe_obj = position_8_signe.get_rect()
position_8_signe_obj.center = (250, 350)
position_9_signe_obj = position_9_signe.get_rect()
position_9_signe_obj.center = (350, 350)
coordintes_signe_obj = coordinates_input.get_rect()
coordintes_signe_obj.center = (240, 450)
# narysujemy ekran na którym gra się będzie odbywać
screen = pygame.display.set_mode((500,500))
# gra do czasu aż wpisanie będzie "QUIT"
game_status = True

while game_status:
    # Czy gracz kliknął w zamknięcie OKNA?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
    # Tło naszego okna -BIAŁE
    screen.fill(blue)
    screen.blit(title_signe, title_obj)
    screen.blit(position_1_signe, position_1_signe_obj)
    screen.blit(position_2_signe, position_2_signe_obj)
    screen.blit(position_3_signe, position_3_signe_obj)
    screen.blit(position_4_signe, position_4_signe_obj)
    screen.blit(position_5_signe, position_5_signe_obj)
    screen.blit(position_6_signe, position_6_signe_obj)
    screen.blit(position_7_signe, position_7_signe_obj)
    screen.blit(position_8_signe, position_8_signe_obj)
    screen.blit(position_9_signe, position_9_signe_obj)
    screen.blit(position_9_signe, position_9_signe_obj)
    screen.blit(coordinates_input, coordintes_signe_obj)

        #początek (od lewej, od góry), koniec (od lewej, od góry), grubość
    pygame.draw.line(screen, white, (100, 100), (400, 100), 2)
    pygame.draw.line(screen, white, (100, 200), (400, 200), 2)
    pygame.draw.line(screen, white, (100, 300), (400, 300), 2)
    pygame.draw.line(screen, white, (100, 400), (400, 400), 2)
    pygame.draw.line(screen, white, (100, 100), (100, 400), 2)
    pygame.draw.line(screen, white, (200, 100), (200, 400), 2)
    pygame.draw.line(screen, white, (300, 100), (300, 400), 2)
    pygame.draw.line(screen, white, (400, 100), (400, 400), 2)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


    


