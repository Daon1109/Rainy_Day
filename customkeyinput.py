
############################################
import pygame
############################################


def keyinput(SCREEN, clock):


    pygame.display.set_caption("Custom Key Input Window")

    # fonts
    c_font = pygame.font.SysFont("arial", 45, True, False)
    # color
    white = (255,255,255)
    black = (0,0,0)
    blue = (9,47,184)
    darkgreen = (8,102,43)
    lightgreen = (8,207,82)
    color = [0,0,0,0,0]
    rectcolor = darkgreen
    enterkeycolor = white



    # default key input
    customkey = [0,0,0,0,0]     # key의 input string값
    keydisplayed = [0,0,0,0,0]  # 밑 분할된 화면에 보이는 key값(text값)
    kd_rect = [0,0,0,0,0]       # keydisplayed 변수 Rect값
    for c in range(4):
        customkey[c] = str(c+1)
        keydisplayed[c] = c_font.render(customkey[c], True, (0,0,0))
        kd_rect[c] = keydisplayed[c].get_rect()
        kd_rect[c].centerx = 75 + (150 * c)
        kd_rect[c].centery = 625


    # key input box
    keyboxMessage = [0,0,0,0,0]     # "Key#n:" (keyinput variable)
    message_rect = [0,0,0,0,0]      # keyboxMessage 변수 Rect값
    keyinput = [0,0,0,0,0]          # input box의 text값
    input_rect = [0,0,0,0,0]        # keyinput 변수 Rect값

    for c in range(4):
        # Setting KeyboxMessage
        keyboxMessage[c] = c_font.render(("Key#"+str(c+1)+": "), True, (0,0,0))
        message_rect[c] = keyboxMessage[c].get_rect()
        message_rect[c].x = 0
        message_rect[c].centery = 90 + (90*c)
        # Setting keyinput(default)
        keyinput[c] = c_font.render(customkey[c], True, (0,0,0))
        input_rect[c] = keyinput[c].get_rect()
        input_rect[c].x = 150
        input_rect[c].centery = 90 + (90*c)



    # Display custom-key-input-window
    active = False
    eventbox = 4
    c_playing = True
    while c_playing:

        # background color: white
        SCREEN.fill((255,255,255))



        # Event Process
        for event in pygame.event.get():

            # Quit Event Process
            if event.type == pygame.QUIT:
                c_playing = False
                pygame.quit()


            # Event: Input boxes
            if event.type == pygame.MOUSEBUTTONDOWN:
                for c in range(4):
                    # click input_rect[c]:
                    if input_rect[c].collidepoint(event.pos):
                        active = True
                        eventbox = c
                        break
                    else:
                        active = False
                        # return last box's color
                        eventbox = 4

                # Enter Key Process
                if pygame.Rect(50, 450, 500, 60).collidepoint(event.pos):
                    c_playing = False

            if active:
                # Text input
                if event.type == pygame.KEYDOWN:

                    # Check for Backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        customkey[eventbox] = customkey[eventbox][:-1]
        
                    # Unicode standard(string)
                    else:
                        customkey[eventbox] += event.unicode
                        if len(customkey[eventbox]) >= 0:
                            customkey[eventbox] = customkey[eventbox][0].upper()


        # UI 1234
        pygame.draw.line(SCREEN, (0,0,0), [150,600], [150,650], 3)
        pygame.draw.line(SCREEN, (0,0,0), [300,600], [300,650], 3)
        pygame.draw.line(SCREEN, (0,0,0), [450,600], [450,650], 3)
        pygame.draw.line(SCREEN, (0,0,0), [0,600], [600,600], 3)
        pygame.draw.line(SCREEN, (0,0,0), [0,650], [600,650], 3)

        for i in range(4):

            # Color Setting
            color[i] = black
            color[eventbox] = blue

            # UI 1234
            keydisplayed[i] = c_font.render(customkey[i], True, color[i])
            SCREEN.blit(keydisplayed[i], kd_rect[i])

            # UI keyinputbox
            keyinput[i] = c_font.render(customkey[i], True, color[i])
            SCREEN.blit(keyboxMessage[i], message_rect[i])
            SCREEN.blit(keyinput[i], input_rect[i])


        # Rect: Enter button
        # Change button's color by mouse's position
        mousepos = pygame.mouse.get_pos()
        if mousepos[0]>50 and mousepos[0]<550 and mousepos[1]>450 and mousepos[1]<510:
            rectcolor = lightgreen
        else:
            rectcolor = darkgreen
        # Drawing
        pygame.draw.rect(SCREEN, rectcolor, pygame.Rect(50, 450, 500, 60), border_radius=6)
        enterkey = c_font.render("GO", True, enterkeycolor)
        enter_rect = enterkey.get_rect()
        enter_rect.centerx = 300
        enter_rect.centery = 480
        SCREEN.blit(enterkey, enter_rect)



        # Update Screen
        pygame.display.flip()
        # fps = 60
        clock.tick(60)

    
    # Returning key input
    return customkey
