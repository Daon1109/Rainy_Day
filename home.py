
#############################
import pygame
import design as d
#############################

def start_display(SCREEN, clock):
    pygame.display.set_caption("Rainy Day - start")

    # make title image animated
    titlepic = [0,0,0,0]
    for i in range(4):
        titlepic[i] = pygame.image.load("C:/Coding/Python/Rainy_Day/images/title{num}.png".format(num=str(i+1)))    # Querystring
        titlepic[i] = pygame.transform.scale(titlepic[i], (800, 500))
    title_displayed = titlepic[0]
    title_rect = titlepic[0].get_rect()
    title_rect.centerx = 711
    title_rect.centery = 300
    strt_font = d.arial(45)

    changeTimer = 0

    # display
    playing = True
    while playing:

        SCREEN.fill(d.white)

        # Event Process
        for event in pygame.event.get():

            # Quit Event Process
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()

            # START button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(461, 520, 500, 80).collidepoint(event.pos):
                    playing = False

        
        # Rect: Enter button
        # Change button's color by mouse's position
        mousepos = pygame.mouse.get_pos()
        if mousepos[0]>461 and mousepos[0]<961 and mousepos[1]>520 and mousepos[1]<580:
            rectcolor = d.lightblue
        else:
            rectcolor = d.darkblue
        # Drawing
        pygame.draw.rect(SCREEN, rectcolor, pygame.Rect(461, 520, 500, 80), border_radius=6)
        enterkey = strt_font.render("START", True, d.white)
        enter_rect = enterkey.get_rect()
        enter_rect.centerx = 711
        enter_rect.centery = 560
        SCREEN.blit(enterkey, enter_rect)

        # title - gif
        if changeTimer>=0 and changeTimer<30:
            title_displayed = titlepic[1]
        elif changeTimer>=30 and changeTimer<60:
            title_displayed = titlepic[2]
        elif changeTimer>=60 and changeTimer<90:
            title_displayed = titlepic[3]
        elif changeTimer>120:
            changeTimer = 0
            title_displayed = titlepic[0]
        SCREEN.blit(title_displayed, title_rect)

        # gif import: timer
        changeTimer += 2
        # Update Screen
        pygame.display.flip()
        # fps = 60
        clock.tick(60)



def gameover_display(SCREEN, clock, score, boostcnt, combomax):

    # Score display
    scoreLG_font = d.arial(70)
    scoreLG = scoreLG_font.render("SCORE", True, d.black)
    scoreLG_rect = scoreLG.get_rect()
    scoreLG_rect.centerx = 711
    scoreLG_rect.centery = 100
    score_font = d.arial(150)
    scoretxt = score_font.render(str(score), True, d.black)
    score_rect = scoretxt.get_rect()
    score_rect.centerx = 711
    score_rect.centery = 300
    # etc
    etc_font = d.arial(30)
    boosttxt = etc_font.render("Boost Used:  "+str(boostcnt), True, d.black)
    boost_rect = boosttxt.get_rect()
    boost_rect.centerx = 711
    boost_rect.centery = 500
    combotxt = etc_font.render("Max Combo:  "+str(combomax), True, d.black)
    combo_rect = combotxt.get_rect()
    combo_rect.centerx = 711
    combo_rect.centery = 580

    playing = True
    while playing:

        SCREEN.fill(d.white)

        # Event Process
        for event in pygame.event.get():

            # Quit Event Process
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()

        SCREEN.blit(scoreLG, scoreLG_rect)
        SCREEN.blit(scoretxt, score_rect)
        SCREEN.blit(boosttxt, boost_rect)
        SCREEN.blit(combotxt, combo_rect)

        # Update Screen
        pygame.display.flip()
        # fps = 60
        clock.tick(60)
