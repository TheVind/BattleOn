#import pygame
import random
#pygame.init()
#pygame.font.init()
#font = pygame.font.Font('freesansbold.ttf', 16)
#DMGFont = pygame.font.Font('freesansbold.ttf', 40)
battleAnimation = True
class animationClass:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def moveAnimation(self, m=200, mx=20, my=20):
        self.max = m
        self.x += mx
        self.y += my

    def dealDamage(self, md=2, d=1, ch=10, a=0, sp=0):
        dmg = random.randint(((5-d)*md),((5+d)*md))
        getCritChance = random.randint(1,10)
        if (ch/10) >= getCritChance:
            dmg = dmg*2
        spellPowerGain = (sp/100)*dmg
        dmg = dmg + spellPowerGain
        armorGain = (a/100)*dmg
        return int(dmg - armorGain)

fireballAni = animationClass(-300,-500)
print(str(fireballAni.x))
fireballAni.moveAnimation(200,20,20)
print(str(fireballAni.x))
lightningAni = animationClass(400,-500)
print(str(lightningAni.y))
lightningAni.moveAnimation(-100, 0, 10)
print(str(lightningAni.y))
while battleAnimation:
    print(str(lightningAni.y))
    lightningAni.moveAnimation(-100, 0, 10)
    if lightningAni.max <= lightningAni.y:
        battleAnimation = False
print(str(lightningAni.dealDamage(1,1,10,0,0)))

woodenStick = {
    "spellDMG": 5,
    "critChance": 10,
    "attack": 5,
    "spellPower": 0,
    "armor": 0
}
weapon = woodenStick
print(str(lightningAni.dealDamage(1,1,weapon["critChance"],weapon["armor"],weapon["spellPower"])))
#monster = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/monster.png")
#desert = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/desert.jpg")
#mand = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/mand.png")
#svaerd = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/svaerd.png")
#lightning = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/lightning.png")
#fireball = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/fireball.png")
#wizard = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/wizard.png")
#iceb = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/iceb.png")

#print(str(woodenStick["spellDMG"]))

