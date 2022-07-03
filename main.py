
# 2022 School Project: Rhythm Game
# easteregg 부분 잘라낼것

import pygame
import random
impoet customkeyinput
import key

# Restart pygame(init)
pygame.init()

 
# Save SCREEN object
SCREEN = pygame.display.set_mode((600,800))

# Create Clock for fps
clock = pygame.time.Clock()

#############################################################
# Custom key input
customkey = customkeyinput.keyinput(SCREEN,clock)
print(customkey)
#############################################################



pygame.display.set_caption("Rhythm Game Maybe")
# Game font setting
scoreFont = pygame.font.SysFont("arial", 80, True, False)
messageFont = pygame.font.SysFont("arial", 45, True, False)

# Game font setting
scoreFont = pygame.font.SysFont("arial", 80, True, False)
messageFont = pygame.font.SysFont("arial", 45, True, False)
blockFont = pygame.font.SysFont("arial", 25, True, False)

# default messages
scoreMessage =  messageFont.render("", True, (255,255,255))


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

# Setting block speed
speed = [0,0,0,0,0]
savedspeed = [0,0,0,0,0]
for sspd in range(4):
    speed[sspd] = random.randint(3,10)
    savedspeed[sspd] = speed[sspd]

##############################################################
# Bug: icon loading failed
icon = pygame.image.load("C:/Coding/Python/Pygame/icon.png")
pygame.display.set_icon(icon)
##############################################################








# Playing Code
playing = True
score = 0
block_cnt = 4

while playing:

    # Background Settings
    SCREEN.fill((255,255,255))
    pygame.draw.line(SCREEN, (0,0,0), [0,600], [600,600], width=3)
    pygame.draw.line(SCREEN, (0,0,0), [0,650], [600,650], width=3)



    # Event Process
    for event in pygame.event.get():

        # Quit Event Process
        if event.type == pygame.QUIT:
            playing = False
            print("\n\nScore: "+str(score)+"\n")
            pygame.quit()

        # Multiple key input
        pressed_keys = pygame.key.get_pressed()


        # Spacekey_Tab: for testing
        if event.type == pygame.KEYDOWN:
            if event.key == key.space:
                cnt = 0

                
                # judging if block is in range
                for k in range(4):
                    if block_Rect[k].y <= 660 and block_Rect[k].y >= 590:

                        # making image transparent
                        block[k].set_alpha(0)
                        cnt+=1

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
                    score+=25
                elif cnt == 3:
                    print("3 blocks")
                    scoreMessage =  messageFont.render("3 blocks +40", True, (158, 4, 209))
                    score+=40
                elif cnt == 4:
                    print("4 blocks")
                    scoreMessage =  messageFont.render("4 blocks +100", True, (252, 190, 18))
                    score+=100
            

        #############################################
        # 에러 덩어리
        # Dev: easteregg
        if pressed_keys[key.d] and pressed_keys[key.e] and pressed_keys[key.v]:
            SCREEN.fill((0,0,0))
            dev_esteg = scoreFont.render("Dev: Suho Ban\nGithub: Daon1109\nPosung Highschool Project\n\nThanks for playing!",True,(255,255,255))
            estegText_Rect = dev_esteg.get_rect()
            SCREEN.blit(dev_esteg, estegText_Rect)
            scoreMessage.set_alpha(0)
            scoreText.set_alpha(0)
            blockcntText.set_alpha(0)
            SPBText.set_alpha(0)
            for rset in range(4):
                speed[rset]=0
                block[rset].set_alpha(0)
        else:
            #SCREEN.fill((255,255,255))
            scoreText = scoreFont.render(str(score), True, (0,0,0))
            blockcntText = blockFont.render(("Block: "+str(block_cnt)), True, (0,0,0))
            spb = score / block_cnt
            SPBText = blockFont.render(("SPB: "+str(spb)), True, (0,0,0))
            for rturn in range(4):
                speed[rturn] = savedspeed[rturn]
            

    # Scoreboard
    score_Rect = scoreText.get_rect()
    score_Rect.centerx = 300
    score_Rect.y = 100
    SCREEN.blit(scoreText, score_Rect)

    # Score message
    scoreM_Rect = scoreMessage.get_rect()
    scoreM_Rect.centerx = 300
    scoreM_Rect.y = 200
    SCREEN.blit(scoreMessage, scoreM_Rect)

    # score per block
    blockcnt_Rect = blockcntText.get_rect()
    SPB_Rect = SPBText.get_rect()
    SCREEN.blit(blockcntText, [450, 150])
    SCREEN.blit(SPBText, [450, 200])




    #############################################
    # 좌표증가 코드
    block_Rect[0].y +=speed[0]
    block_Rect[1].y +=speed[1]
    block_Rect[2].y +=speed[2]
    block_Rect[3].y +=speed[3]
    #############################################



    j=0
    while j<4:
        # Preventing block escaping screen
        if block_Rect[j].y > 1000:
            # y coordinate of block(reset)
            block_Rect[j].bottom = 0
            # making image appear
            block[j].set_alpha(255)
            # count block
            block_cnt+=1
            # 지속적인 업데이트가 안됨. 왜지?


            ####################################################
            # changing speed(random)
            speed[j] = random.randint(3,10)
            savedspeed[j] = speed[j]
            ####################################################



        # Copy block in surface (coordinate: block_Rect)
        SCREEN.blit(block[j], block_Rect[j])
        j+=1


    # Update Screen
    pygame.display.flip()

    # fps = 60
    clock.tick(60)
