import pygame
import random
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("BattleOn")
monster = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/monster.png")
desert = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/desert.jpg")
mand = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/mand.png")
svaerd = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/svaerd.png")
lightning = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/lightning.png")
fireball = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/fireball.png")
wizard = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/wizard.png")
iceb = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/iceb.png")
fireAni = False
def fireAnimation(coordinat, fireY, fireX):
    fireAni = True
    if coordinat == "x":
        fireX += 20
        return fireX
    elif coordinat == "y":
        fireY += 20
        return fireY
    else:
        fireY = -500
        fireX = -300
    if fireY >= 200:
        fireAni = False
fireAnimation("reset", -500, -300)
run = True
roundStart = True
while run:
    ### The basic function in Pygame: Timedelay (amount of frames), update-function, close-function, and get key-input-function
    if roundStart:
        background = random.randint(1,1)
        if background == 1:
            bg = desert
        roundStart = False
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    keys = pygame.key.get_pressed()
    win.blit(bg,(0,0))
    if keys[pygame.K_f]:
        fireAni = True
        fireY = -500
        fireX = -300
    if fireAni:
        win.blit(fireball,(fireAnimation("x", fireY, fireX),fireAnimation("y", fireY, fireX)))
pygame.quit()