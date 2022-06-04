
# 2022 School Project: Rhythm Game

import pygame
import key

# Restart pygame(init)
pygame.init()

 
# Save SCREEN object
SCREEN = pygame.display.set_mode((600,800))
pygame.display.set_caption("Rhythm Game Maybe")

# Create Clock for fps
clock = pygame.time.Clock()

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







# Playing Code
playing = True
score = 0

while playing:

    # Event Process
    for event in pygame.event.get():

        # Quit Event Process
        if event.type == pygame.QUIT:
            playing = False
            print("\n\nScore: "+str(score))
            pygame.quit()

        # Spacekey_Tab: for testing, but pretty good code
        if event.type == pygame.KEYDOWN:
            if event.key == key.space:
                cnt = 0

                
                # 판정 코드
                for k in range(4):
                    if block_Rect[k].y <= 660 and block_Rect[k].y >= 590:

                        # making image transparent
                        block[k].set_alpha(0)
                        cnt+=1

                # printing: terminal + scoring
                if cnt == 0:
                    print("MISS")
                    score-=5
                elif cnt == 1:
                    print("1 block")
                    score+=10
                elif cnt == 2:
                    print("2 blocks")
                    score+=25
                elif cnt == 3:
                    print("3 blocks")
                    score+=40
                elif cnt == 4:
                    print("4 blocks")
                    score+=100



    # Background Settings
    SCREEN.fill((255,255,255))
    pygame.draw.line(SCREEN, (0,0,0), [0,600], [600,600], width=3)
    pygame.draw.line(SCREEN, (0,0,0), [0,650], [600,650], width=3)
    myFont = pygame.font.SysFont("arial", 80, True, False)

    # Scoreboard
    scoreText = myFont.render(str(score), True, (0,0,0))
    score_Rect = scoreText.get_rect()
    score_Rect.centerx = 300
    score_Rect.y = 100
    SCREEN.blit(scoreText, score_Rect)


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


        # Copy block in surface (coordinate: block_Rect)
        SCREEN.blit(block[j], block_Rect[j])
        j+=1


    # Update Screen
    pygame.display.flip()

    # fps = 60
    clock.tick(60)