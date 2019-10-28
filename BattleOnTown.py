import pygame
pygame.init()
townbg = pygame.image.load("/Users/jeppe/Visual Studio/Pygame/BattleOn/bgtown.jpg")
wizard = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/wizard.png")
win = pygame.display.set_mode((1300,700))
pygame.display.set_caption("BattleOn")
run = True

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(townbg, (0,0))
    win.blit(wizard, (200,600))
pygame.quit()