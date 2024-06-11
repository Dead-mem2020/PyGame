import pygame

#inicializace pygame
pygame.init()

#vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height))

player = pygame.Rect((300, 250, 50, 50))

#hlavní herní cyklus
lets_continue = True 



while lets_continue:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (250, 0, 0), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player.move_ip(0, -1)


    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            lets_continue = False

    pygame.display.update()


#ukončení pygame, důležité zadat jako první před další prací
pygame.quit()