
#############################
import pygame
import design as d
#############################

def start_display(SCREEN, clock):
    pygame.display.set_caption("Rainy Day - start")

    # design_update
    titlepic = pygame.image.load("C:/Coding/Python/Rainy_Day/images/title.png")
    titlepic = pygame.transform.scale(titlepic, (800, 500))
    title_rect = titlepic.get_rect()
    title_rect.centerx = 711
    title_rect.centery = 300
    strt_font = d.arial(45)


    s_playing = True
    while s_playing:

        SCREEN.fill(d.bluegray)

        # Event Process
        for event in pygame.event.get():

            # Quit Event Process
            if event.type == pygame.QUIT:
                c_playing = False
                pygame.quit()

            # START button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(461, 520, 500, 80).collidepoint(event.pos):
                    s_playing = False

        
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

        SCREEN.blit(titlepic, title_rect)

        # Update Screen
        pygame.display.flip()
        # fps = 60
        clock.tick(60)

def levelchoose(SCREEN, clock):

    pygame.display.set_caption("Rainy Day")


    l_playing = True
    while l_playing:

        SCREEN.fill(d.white)

        # Event Process
        for event in pygame.event.get():

            # Quit Event Process
            if event.type == pygame.QUIT:
                c_playing = False
                pygame.quit()



        # Update Screen
        pygame.display.flip()
        # fps = 60
        clock.tick(60)


def popupScreen(clock):
    P_SCREEN = pygame.display.set_mode((400,600))

    back_icon = pygame.image.load("C:/Coding/Python/Rainy_Day/images/back.png")
    pygame.transform.scale(back_icon, (80, 80))
    back_rect = back_icon.get_rect()
    back_rect.centerx = 200
    back_rect.centery = 300
    replay_icon = pygame.image.load("C:/Coding/Python/Rainy_Day/images/replay.png")
    pygame.transform.scale(replay_icon, (80, 80))
    replay_rect = back_icon.get_rect()
    replay_rect.centerx = 200
    replay_rect.centery = 450

    playing = True
    while playing:

        P_SCREEN.fill(d.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
