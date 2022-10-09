

# 2022 School Project: Rhythm Game

import pygame
import key
import design as d
import home
import customkeyinput


# Restart pygame(init)
pygame.init()


##############################################################
# Bug: icon loading failed
icon = pygame.image.load("C:/Coding/Python/Rainy_Day/images/icon.png")
pygame.display.set_icon(icon)
##############################################################

# Save SCREEN object
SCREEN = pygame.display.set_mode((1422,800))

# Create Clock for fps
clock = pygame.time.Clock()

# Game font setting
scoreFont = d.arial(80)
messageFont = d.arial(45)
sb_font = d.arial(40)


#############################################################################################
# START & level choosing (game home)
home.start_display(SCREEN, clock)
#home.levelchoose(SCREEN, clock)
#############################################################################################



#############################################################################################
# Custom key input
customkey = customkeyinput.keyinput(SCREEN,clock)
print(customkey)

keydisplayed = [0,0,0,0,0]
kd_rect = [0,0,0,0,0]
for c in range(4):
    # UI 1234 (Copied)
    keydisplayed[c] = messageFont.render(customkey[c], True, d.black)
    kd_rect[c] = keydisplayed[c].get_rect()
    kd_rect[c].centery = 625
    if len(customkey[c]) == 5:
        keydisplayed[c] = sb_font.render(customkey[c], True, d.black)
        kd_rect[c].centerx = 491 + (150 * c)    # idk why
    else:
        keydisplayed[c] = messageFont.render(customkey[c], True, d.black)
        kd_rect[c].centerx = 486 + (150 * c)

    # string replaced with pygame.key (*reusing variable)
    customkey[c] = key.keyfunc(customkey[c])

#############################################################################################





# Title
pygame.display.set_caption("Rainy Day")


# Loading image(block) and changing image's size
block = [0,0,0,0,0]
block_Rect = [0,0,0,0,0]
i=0
while i<4:
    # Loading image(block)
    block[i] = pygame.image.load("C:/Coding/Python/Rainy_Day/images/block.png")
    block[i] = pygame.transform.scale(block[i], (150, 30))

    # Saving Rect data
    block_Rect[i] = block[i].get_rect()
    block_Rect[i].x = 411+ 150*i
    block_Rect[i].y = 100
    i+=1

# Loading image(pause icon)
pauseicon = pygame.image.load("C:/Coding/Python/Rainy_Day/images/pause.png")
pauseicon = pygame.transform.scale(pauseicon, (80, 80))
pause_rect = pauseicon.get_rect()
pause_rect.centerx = 1360
pause_rect.centery = 48.5




# Debugging: score message
scoreMessage =  messageFont.render("", True, d.white)
score = 0
boost = 0
scoreText = scoreFont.render(str(score), True, d.black)

# Boost/Skill activation
booston = 0
hitblock = [0,0,0,0]

# Playing Code
playing = True
cnt = 0         # blocks per keydown(score) counter
cast_t = 0      # consider specific range of time as the same moment
combo = 0       # 'combo' score
combo_identifier = [0,0,0,0,0]

while playing:


    # Event Process
    for event in pygame.event.get():

        # Quit Event Process
        if event.type == pygame.QUIT:
            playing = False
            print("\n\nScore: "+str(score)+"\n")
            pygame.quit()


        # Event: Pause Playing
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pause_rect.collidepoint(event.pos):
                # pop-up screen
                home.popupScreen(clock)

        
        # Applying Customized Keys
        elif event.type == pygame.KEYDOWN:
            
            if booston == 0:
                if event.key in customkey:
                    for k in range(4):
                        if event.key == customkey[k]:
                            if block_Rect[k].y <= 660 and block_Rect[k].y >= 590:
                                # making image transparent
                                block[k].set_alpha(0)

                                # combo system #1
                                combo_identifier[k] = 1
                                combo +=1

                                # cast_t counting
                                # print("cast_t: "+str(cast_t))
                                if cast_t > 18:      # range: 0.4 sec (I didnt check it)
                                    cnt = 1
                                    cast_t = 0
                                else:
                                    cnt += 1

                            # MISS: range out
                            else:
                                cnt = 0
                                # combo system #2
                                print("combo reset")
                                combo = 0
                                combo_identifier = [0,0,0,0,0]
                        
                elif event.key == key.space:
                    ##########################################################################################
                    if boost<1000:  # Wrong Key
                        cnt = 0     # combo system #2
                        print("combo reset")
                        combo = 0
                        combo_identifier = [0,0,0,0,0]
                    else:
                        # boost: 15s
                        boost_t = 0
                        booston = 1
                        # boost reset
                        combo = 0
                        combo_identifier = [0,0,0,0,0]


                # MISS: wrong key
                else:
                    cnt = 0
                    # combo system #2
                    print("combo reset")
                    combo = 0
                    combo_identifier = [0,0,0,0,0]


                # printing: terminal + scoring + setting score message
                if cnt == 0:
                    print("MISS")
                    scoreMessage =  messageFont.render("MISS -5", True, (232, 5, 65))
                    score-=5
                elif cnt == 1:
                    print("1 block")
                    scoreMessage =  messageFont.render("1 block +10", True, (91, 196, 4))
                    score+=10
                    if boost<1000: boost+=10
                elif cnt == 2:
                    print("2 blocks")
                    scoreMessage =  messageFont.render("2 blocks +25", True, (4, 209, 206))
                    score+=15
                    if boost<1000: boost+=15
                elif cnt == 3:
                    print("3 blocks")
                    scoreMessage =  messageFont.render("3 blocks +40", True, (158, 4, 209))
                    score+=15
                    if boost<1000: boost+=15
                elif cnt == 4:
                    print("4 blocks")
                    scoreMessage =  messageFont.render("4 blocks +100", True, (252, 190, 18))
                    score+=60
                    if boost<1000: boost+=60

                print("combo: "+str(combo)+"\n")
                if boost<1000:
                    if combo>1:
                        boost = boost + (combo*2-5)
            
            # Boost activated
            else:
                for i in range(4):
                    if hitblock[i] == 0:
                        block[i].set_alpha(0)
                        hitblock[i] = 1
                        print("Boost!")
                        scoreMessage =  messageFont.render("Boost +15", True, d.orangeyellow)
                        score+=15
                        break




    # Background Settings
    # Warning: background color setting code can erase previous display settings
    SCREEN.fill((255,255,255))
    pygame.draw.line(SCREEN, (0,0,0), [411+150,600], [411+150,650], 3)
    pygame.draw.line(SCREEN, (0,0,0), [411+300,600], [411+300,650], 3)
    pygame.draw.line(SCREEN, (0,0,0), [411+450,600], [411+450,650], 3)
    pygame.draw.line(SCREEN, (0,0,0), [411,600], [1011,600], width=3)
    pygame.draw.line(SCREEN, (0,0,0), [411,650], [1011,650], width=3)
    pygame.draw.line(SCREEN, (0,0,0), [410,0], [410,800], width=3)
    pygame.draw.line(SCREEN, (0,0,0), [1012,0], [1012,800], width=3)


    # Pause/Replay Button
    '''     # changing scale
    mousepos = pygame.mouse.get_pos()
    if mousepos[0]>1320 and mousepos[0]<1400 and mousepos[1]>22 and mousepos[1]<97:
        pauseicon = pygame.transform.scale(pauseicon, (100, 93.75))
        pause_rect.centerx = 1360
        pause_rect.centery = 48.5
    else:
        pauseicon = pygame.transform.scale(pauseicon, (80, 75))
        pause_rect.centerx = 1360
    pause_rect.centery = 48.5
    '''
    SCREEN.blit(pauseicon, pause_rect)
  

    # Boost UI
    boost_length = boost/2
    boost_yco = 630 - boost_length
    boostrate = messageFont.render(str(boost/10)+"%", True, d.white)     # Boost Rate
    if boost_length < 500:
        booststr = "Boost"
        boost_color = d.darkblue
        boost_r_color = d.white
    else:
        boost = 1000
        if booston == 1:        # Boost activated
            booststr = "Boost ON"
            boost_yco = 130 + (5/9)*boost_t
            boost_length = 500 - (5/9)*boost_t
            boostrate = messageFont.render(str(15-int(boost_t/60)), True, d.white)
        else:
            booststr = "Spacebar!"
        boost_color = d.orangeyellow
        boost_r_color = d.white


    pygame.draw.rect(SCREEN, d.darkblue, pygame.Rect(1146,130,150,500), border_radius=3)
    pygame.draw.rect(SCREEN, d.orangeyellow, pygame.Rect(1146,boost_yco,150,boost_length), border_radius=3)
    pygame.draw.rect(SCREEN, boost_color, pygame.Rect(1121,650,200,50), border_radius=5)
    boostText = messageFont.render(booststr, True, boost_r_color)     # "Boost"
    boost_Rect = boostText.get_rect()
    boost_Rect.centerx = 1221
    boost_Rect.y = 650
    SCREEN.blit(boostText, boost_Rect)
    boostrate_Rect = boostrate.get_rect()   # Boost Rate
    boostrate_Rect.centerx = 1221
    boostrate_Rect.y = 180
    SCREEN.blit(boostrate, boostrate_Rect)


    # Scoreboard
    scoreText = scoreFont.render(str(score), True, d.black)
    score_Rect = scoreText.get_rect()
    score_Rect.centerx = 711
    score_Rect.y = 100
    SCREEN.blit(scoreText, score_Rect)

    # Score message
    scoreM_Rect = scoreMessage.get_rect()
    scoreM_Rect.centerx = 711
    scoreM_Rect.y = 200
    SCREEN.blit(scoreMessage, scoreM_Rect)

    # Combo Message
    comboMessage = messageFont.render("Combo: "+str(combo), True, d.black)
    combo_rect = comboMessage.get_rect()
    combo_rect.centerx = 711
    combo_rect.y = 250
    if combo > 1:
        comboMessage.set_alpha(255)
    else:
        comboMessage.set_alpha(0)
    SCREEN.blit(comboMessage, combo_rect)


    ##############################
    # 좌표증가 코드
    block_Rect[0].y +=3
    block_Rect[1].y +=5
    block_Rect[2].y +=7
    block_Rect[3].y +=10
    ##############################




    j=0
    while j<4:
        # Preventing block escaping screen
        if block_Rect[j].y > 1000:

            # y coordinate of block(reset)
            block_Rect[j].bottom = 0
            # making image appear
            block[j].set_alpha(255)
            # Boost (hitblock)
            if booston == 1:
                hitblock[j] = 0


        # combo system #3
        if block_Rect[j].y >660:
            if combo_identifier[j] == 0:
                print("combo reset")
                combo = -1
                combo_identifier = [0,0,0,0,0]


        # Copy block in surface (coordinate: block_Rect)
        SCREEN.blit(block[j], block_Rect[j])
        # UI 1234 blit
        SCREEN.blit(keydisplayed[j], kd_rect[j])
        j+=1


    # Update Screen
    pygame.display.flip()

    # fps = 60
    clock.tick(60)

    # timer
    cast_t += 1
    if booston == 1:
        boost_t +=1
        # Boost deactivation
        if boost_t > 900:
            boost = 0
            booston = 0
