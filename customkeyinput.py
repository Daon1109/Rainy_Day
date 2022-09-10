
############################################
import pygame
import design as d
############################################


def keyinput(SCREEN, clock):


    pygame.display.set_caption("Custom Key Input Window")

    # fonts
    c_font = d.arial(45)
    sb_font = d.arial(40)
    # color
    color = [0,0,0,0,0]
    rectcolor = d.darkgreen
    enterkeycolor = d.white



    # default key input
    customkey = [0,0,0,0,0]     # key의 input string값
    keydisplayed = [0,0,0,0,0]  # 밑 분할된 화면에 보이는 key값(text값)
    kd_rect = [0,0,0,0,0]       # keydisplayed 변수 Rect값
    for c in range(4):
        customkey[c] = str(c+1)
        keydisplayed[c] = c_font.render(customkey[c], True, (0,0,0))
        kd_rect[c] = keydisplayed[c].get_rect()
        kd_rect[c].centerx = 411+ 75 + (150 * c)
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
        message_rect[c].x = 416
        message_rect[c].centery = 90 + (90*c)
        # Setting keyinput(default)
        keyinput[c] = c_font.render(customkey[c], True, (0,0,0))
        input_rect[c] = keyinput[c].get_rect()
        input_rect[c].x = 411+150
        input_rect[c].centery = 90 + (90*c)



    # Display custom-key-input-window
    active = False
    eventbox = 4
    e_keyoverlap = 0
    e_noinput = 0
    errcnt = 0
    c_playing = True
    while c_playing:

        # background color: white
        SCREEN.fill(d.white)



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
                    if input_rect[c].collidepoint(event.pos) or message_rect[c].collidepoint(event.pos):
                        active = True
                        eventbox = c
                        break
                    else:
                        active = False
                        # return last box's color
                        eventbox = 4

                # Enter Key Process
                if pygame.Rect(461, 450, 500, 60).collidepoint(event.pos):
                    e_keyoverlap = 0      # identify whether key overlapped or not
                    e_noinput = 0         # identify if customkey has no value
                    for prvnt1 in range(4):
                        for prvnt2 in range(4):
                            if prvnt1 != prvnt2:
                                # ErrorMessage: key overlap
                                if customkey[prvnt1] == customkey[prvnt2]:
                                    e_keyoverlap = 1
                        # ErrorMessage: no input
                        if len(customkey[prvnt1]) == 0:
                            e_noinput = 1

                    # Error Message
                    if e_noinput == 1:
                        print("ERROR: NO Input")
                        errcnt = 0
                    elif e_keyoverlap == 1:
                        print("ERROR: key overlapped")
                        errcnt = 0
                    # successful input -> playing start
                    else:
                        c_playing = False

            if active:
                # Text input
                if event.type == pygame.KEYDOWN:

                    # Check for Backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        customkey[eventbox] = customkey[eventbox][8:-1]
        
                    # Unicode standard(string)
                    else:
                        customkey[eventbox] += event.unicode
                        if len(customkey[eventbox]) > 0:

                            # special keys
                            if customkey[eventbox] == " ":
                                customkey[eventbox] = ''
                            elif customkey[eventbox] == chr(9):
                                customkey[eventbox] = "TAB"
                            elif customkey[eventbox] == chr(27):
                                customkey[eventbox] = "ESC"
                            elif customkey[eventbox] == chr(127):
                                customkey[eventbox] = "DEL"
                            elif customkey[eventbox] == chr(13):
                                customkey[eventbox] = "ENTER"
                            else:
                                customkey[eventbox] = customkey[eventbox][0].upper()


        # UI 1234
        pygame.draw.line(SCREEN, (0,0,0), [411+150,600], [411+150,650], 3)
        pygame.draw.line(SCREEN, (0,0,0), [411+300,600], [411+300,650], 3)
        pygame.draw.line(SCREEN, (0,0,0), [411+450,600], [411+450,650], 3)
        pygame.draw.line(SCREEN, (0,0,0), [411,600], [1011,600], width=3)
        pygame.draw.line(SCREEN, (0,0,0), [411,650], [1011,650], width=3)
        pygame.draw.line(SCREEN, (0,0,0), [410,0], [410,800], width=3)
        pygame.draw.line(SCREEN, (0,0,0), [1012,0], [1012,800], width=3)

        for i in range(4):

            # Color Setting
            color[i] = d.black
            color[eventbox] = d.blue

            # UI 1234
            if len(customkey[i]) == 5:
                keydisplayed[i] = sb_font.render(customkey[i], True, color[i])
                kd_rect[i].centerx = 411 + 35 + (150 * i)
            elif len(customkey[i]) == 3:
                keydisplayed[i] = c_font.render(customkey[i], True, color[i])
                kd_rect[i].centerx = 411 + 50 + (150 * i)
            else:
                keydisplayed[i] = c_font.render(customkey[i], True, color[i])
                kd_rect[i].centerx = 411 + 75 + (150 * i)
            SCREEN.blit(keydisplayed[i], kd_rect[i])

            # UI keyinputbox
            keyinput[i] = c_font.render(customkey[i], True, color[i])
            SCREEN.blit(keyboxMessage[i], message_rect[i])
            SCREEN.blit(keyinput[i], input_rect[i])


        # Rect: Enter button
        # Change button's color by mouse's position
        mousepos = pygame.mouse.get_pos()
        if mousepos[0]>461 and mousepos[0]<911 and mousepos[1]>450 and mousepos[1]<510:
            rectcolor = d.lightgreen
        else:
            rectcolor = d.darkgreen
        # Drawing
        pygame.draw.rect(SCREEN, rectcolor, pygame.Rect(461, 450, 500, 60), border_radius=6)
        enterkey = c_font.render("GO", True, enterkeycolor)
        enter_rect = enterkey.get_rect()
        enter_rect.centerx = 711
        enter_rect.centery = 480
        SCREEN.blit(enterkey, enter_rect)

        # Error Message
        if errcnt > 180:
            e_keyoverlap = 0
            e_noinput = 0
        # errormessage setting
        if e_noinput == 1:
            errorMessage = c_font.render("ERROR: No Input", True, d.white)
        elif e_keyoverlap == 1:
            errorMessage = c_font.render("ERROR: Key Overlapped", True, d.white)
        else:   # Debugging
            errorMessage = c_font.render("NONE", True, d.white)
        em_rect = errorMessage.get_rect()
        em_rect.centerx = 711
        em_rect.centery = 250
        # making errormessage transparent
        if (e_keyoverlap + e_noinput) == 0:
            em_rect_pos = pygame.Rect(0,0,0,0)
            errorMessage.set_alpha(0)
        else:
            em_rect_pos = pygame.Rect(461, 200, 500, 100)
            errorMessage.set_alpha(255)
        pygame.draw.rect(SCREEN, d.red, em_rect_pos, border_radius=6)
        SCREEN.blit(errorMessage, em_rect)



        # Update Screen
        pygame.display.flip()
        # fps = 60
        clock.tick(60)
        # error message countdown
        errcnt +=1

    
    # Returning key input
    return customkey
