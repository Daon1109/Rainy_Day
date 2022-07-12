

# 2022 School Project: Rhythm Game

import pygame
import key
import customkeyinput

# Restart pygame(init)
pygame.init()

 
# Save SCREEN object
SCREEN = pygame.display.set_mode((600,800))
##############################################################
# Bug: icon loading failed
icon = pygame.image.load("C:/Coding/Python/Pygame/icon.png")
pygame.display.set_icon(icon)
##############################################################


# Create Clock for fps
clock = pygame.time.Clock()

# Game font setting
scoreFont = pygame.font.SysFont("arial", 80, True, False)
messageFont = pygame.font.SysFont("arial", 45, True, False)
sb_font = pygame.font.SysFont("arial", 30, True, False)


#############################################################################################
# Custom key input
customkey = customkeyinput.keyinput(SCREEN,clock)
print(customkey)

keydisplayed = [0,0,0,0,0]
kd_rect = [0,0,0,0,0]
for c in range(4):
    # UI 1234 (Copied)
    keydisplayed[c] = messageFont.render(customkey[c], True, (0,0,0))
    kd_rect[c] = keydisplayed[c].get_rect()
    kd_rect[c].centery = 625
    if customkey[c] == "spacebar":
        keydisplayed[c] = sb_font.render(customkey[c], True, (0,0,0))
        kd_rect[c].centerx = 100 + (150 * c)    # idk why
    else:
        keydisplayed[c] = messageFont.render(customkey[c], True, (0,0,0))
        kd_rect[c].centerx = 75 + (150 * c)

    # string replaced with pygame.key (*reusing variable)
    customkey[c] = key.keyfunc(customkey[c])

#############################################################################################





# Title
pygame.display.set_caption("Rhythm Game Maybe")


# Loading image(block) and changing image's size
block = [0,0,0,0,0]
block_Rect = [0,0,0,0,0]
i=0
while i<4:
    # Loading image(block)
    block[i] = pygame.image.load("C:/Coding/Python/Pygame/block.png")
    block[i] = pygame.transform.scale(block[i], (150, 30))

    # Save block's Rect data
    block_Rect[i] = block[i].get_rect()
    block_Rect[i].x = 150*i
    block_Rect[i].y = 100

    i+=1





# Debugging: score message
scoreMessage =  messageFont.render("", True, (255,255,255))
score = 0
scoreText = scoreFont.render(str(score), True, (0,0,0))



# Playing Code
playing = True
cnt = 0         # blocks per keydown(score) counter
cast_t = 0      # consider specific range of time as the same moment
combo = 0       # 'combo' score
yco_hit = [0,0,0,0,0]
combo_identifier = [0,0,0,0,0]

while playing:


    # Event Process
    for event in pygame.event.get():

        # Quit Event Process
        if event.type == pygame.QUIT:
            playing = False
            print("\n\nScore: "+str(score)+"\n")
            pygame.quit()





        
        # Applying Customized Keys
        if event.type == pygame.KEYDOWN:
            
            #cnt=0

            # 다른 키 눌러도 점수 올라가는 에러 존재

            # something's wrong with variable cnt (**error occured while playing with spacebar)
            for k in range(4):
                if event.key == customkey[k]:
                    if block_Rect[k].y <= 660 and block_Rect[k].y >= 590:
                        # making image transparent
                        block[k].set_alpha(0)

                        # combo system #1
                        combo_identifier[k] = 1
                        yco_hit[k] = block_Rect[k].y

                        # cast_t counting
                        print("cast_t: "+str(cast_t))
                        if cast_t > 18:      # range: 0.4 sec (I didnt check it)
                            cnt = 1
                            cast_t = 0
                        else:
                            cnt += 1

                    # "MISS"
                    else:
                        cnt = 0


            # printing: terminal + scoring + setting score message
            if cnt == 0:
                print("MISS")
                scoreMessage =  messageFont.render("MISS -5", True, (232, 5, 65))
                score-=5
            elif cnt == 1:
                print("1 block")
                scoreMessage =  messageFont.render("1 block +10", True, (91, 196, 4))
                score+=10
            elif cnt == 2:
                print("2 blocks")
                scoreMessage =  messageFont.render("2 blocks +25", True, (4, 209, 206))
                score+=15
            elif cnt == 3:
                print("3 blocks")
                scoreMessage =  messageFont.render("3 blocks +40", True, (158, 4, 209))
                score+=15
            elif cnt == 4:
                print("4 blocks")
                scoreMessage =  messageFont.render("4 blocks +100", True, (252, 190, 18))
                score+=60

            print("combo: "+str(combo))







    # Background Settings
    # Warning: background color setting code can erase previous display settings
    SCREEN.fill((255,255,255))
    pygame.draw.line(SCREEN, (0,0,0), [150,600], [150,650], 3)
    pygame.draw.line(SCREEN, (0,0,0), [300,600], [300,650], 3)
    pygame.draw.line(SCREEN, (0,0,0), [450,600], [450,650], 3)
    pygame.draw.line(SCREEN, (0,0,0), [0,600], [600,600], width=3)
    pygame.draw.line(SCREEN, (0,0,0), [0,650], [600,650], width=3)


    # Scoreboard
    scoreText = scoreFont.render(str(score), True, (0,0,0))
    score_Rect = scoreText.get_rect()
    score_Rect.centerx = 300
    score_Rect.y = 100
    SCREEN.blit(scoreText, score_Rect)

    # Score message
    scoreM_Rect = scoreMessage.get_rect()
    scoreM_Rect.centerx = 300
    scoreM_Rect.y = 200
    SCREEN.blit(scoreMessage, scoreM_Rect)


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

        elif block_Rect[j].y == yco_hit[j]:

            # combo system #2
            if combo_identifier[j] == 1:
                combo += 1
            else:
                combo = 0
            combo_identifier[j] = 0


        # Copy block in surface (coordinate: block_Rect)
        SCREEN.blit(block[j], block_Rect[j])
        # UI 1234 blit
        SCREEN.blit(keydisplayed[j], kd_rect[j])
        j+=1


    # Update Screen
    pygame.display.flip()

    # fps = 60
    clock.tick(60)

    # counting cast_t
    cast_t += 1
