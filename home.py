
#############################
import pygame
import design as d
#############################

def start_display(SCREEN, clock):
    pygame.display.set_caption("Rainy Day - start")


    # design
    title_font = d.arial(70)
    strt_font = d.arial(45)

    titlestr = title_font.render("Rainy Day", True, d.black)
    title_rect = titlestr.get_rect()
    title_rect.centerx = 711
    title_rect.centery = 250

    s_playing = True
    while s_playing:

        SCREEN.fill(d.white)

        # Event Process
        for event in pygame.event.get():

            # Quit Event Process
            if event.type == pygame.QUIT:
                c_playing = False
                pygame.quit()

            # START button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(511, 400, 400, 80).collidepoint(event.pos):
                    s_playing = False

        
        # Rect: Enter button
        # Change button's color by mouse's position
        mousepos = pygame.mouse.get_pos()
        if mousepos[0]>511 and mousepos[0]<911 and mousepos[1]>400 and mousepos[1]<460:
            rectcolor = d.lightgreen
        else:
            rectcolor = d.darkgreen
        # Drawing
        pygame.draw.rect(SCREEN, rectcolor, pygame.Rect(511, 400, 400, 80), border_radius=6)
        enterkey = strt_font.render("START", True, d.white)
        enter_rect = enterkey.get_rect()
        enter_rect.centerx = 711
        enter_rect.centery = 440
        SCREEN.blit(enterkey, enter_rect)

        
        SCREEN.blit(titlestr, title_rect)

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