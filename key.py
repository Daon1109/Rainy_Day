
import pygame

up = pygame.K_UP
down = pygame.K_DOWN
right = pygame.K_RIGHT
left = pygame.K_LEFT
space = pygame.K_SPACE


def keyfunc(keychar):

    if keychar == "A":
        key = pygame.K_a
    elif keychar == "B":
        key = pygame.K_b
    elif keychar == "C":
        key = pygame.K_c
    elif keychar == "D":
        key = pygame.K_d
    elif keychar == "E":
        key = pygame.K_e
    elif keychar == "F":
        key = pygame.K_f
    elif keychar == "G":
        key = pygame.K_g
    elif keychar == "H":
        key = pygame.K_h
    elif keychar == "I":
        key = pygame.K_i
    elif keychar == "J":
        key = pygame.K_j
    elif keychar == "K":
        key = pygame.K_k
    elif keychar == "L":
        key = pygame.K_l
    elif keychar == "M":
        key = pygame.K_m
    elif keychar == "N":
        key = pygame.K_n
    elif keychar == "O":
        key = pygame.K_o
    elif keychar == "P":
        key = pygame.K_p
    elif keychar == "Q":
        key = pygame.K_q
    elif keychar == "R":
        key = pygame.K_r
    elif keychar == "S":
        key = pygame.K_s
    elif keychar == "T":
        key = pygame.K_t
    elif keychar == "U":
        key = pygame.K_u
    elif keychar == "V":
        key = pygame.K_v
    elif keychar == "W":
        key = pygame.K_w
    elif keychar == "X":
        key = pygame.K_x
    elif keychar == "Y":
        key = pygame.K_y
    elif keychar == "Z":
        key = pygame.K_z
    elif keychar == "0":
        key = pygame.K_0
    elif keychar == "1":
        key = pygame.K_1
    elif keychar == "2":
        key = pygame.K_2
    elif keychar == "3":
        key = pygame.K_3
    elif keychar == "4":
        key = pygame.K_4
    elif keychar == "5":
        key = pygame.K_5
    elif keychar == "6":
        key = pygame.K_6
    elif keychar == "7":
        key = pygame.K_7
    elif keychar == "8":
        key = pygame.K_8
    elif keychar == "9":
        key = pygame.K_9
    elif keychar == "SPACE":
        key = pygame.K_SPACE
    elif keychar == "TAB":
        key = pygame.K_TAB
    elif keychar == "-":
        key = pygame.K_MINUS
    elif keychar == "=":
        key = pygame.K_EQUALS
    elif keychar == ";":
        key = pygame.K_SEMICOLON
    elif keychar == ",":
        key = pygame.K_COMMA
    elif keychar == "/":
        key = pygame.K_SLASH
    elif keychar == "\\":
        key = pygame.K_BACKSLASH
    elif keychar == ".":
        key = pygame.K_PERIOD
    elif keychar == "`":
        key = pygame.K_BACKQUOTE
    elif keychar == "\'":
        key = pygame.K_QUOTE
    elif keychar == "[":
        key = pygame.K_LEFTBRACKET
    elif keychar == "]":
        key = pygame.K_RIGHTBRACKET
    elif keychar == "ESC":
        key = pygame.K_ESCAPE
    elif keychar == "DEL":
        key = pygame.K_DELETE
    elif keychar == "ENTER":
        key = pygame.K_RETURN


    return key
