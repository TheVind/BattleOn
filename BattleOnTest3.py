import pygame
import random

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 16)
DMGFont = pygame.font.Font('freesansbold.ttf', 40)
lightAni = False
fireAni = False
icebAni = False
dmgonce = False
shDMGText = False
canAttack = True
monsterTimer = 20
win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("BattleOn")
yourTurn = True
shCritText = 0
dmgString = ""
shDMGText2 = False
shTimer = 41
monsterHP = 100
monsterAttack = False
monsterTimer = 20
win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("BattleOn")
shMonster = True
dmg = 0
yourTurn = True
monsterPause = 100
critText = False
icebY = 1000
monster1 = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/monster.png")
desert = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/desert.jpg")
mand = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/mand.png")
svaerd = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/svaerd.png")
lightning = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/lightning.png")
fireball = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/fireball.png")
wizard = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/wizard.png")
iceb = pygame.image.load("/USers/jeppe/Visual Studio/Pygame/BattleOn/iceb.png")
roundStart = True
class monsterAni:

    def __init__(self, image, x=600, y=300, maxX = 440, startingPos=600):
        self.image = image
        self.x = x
        self.y = y
        self.moveBack = False
        self.damage = 0
        self.startingPosition = startingPos
        self.maxXPosition = maxX

    def moveAnimation(self, mx=20, my=0, startingPosi=600):
        if self.moveBack:
            self.x += mx
        elif self.x < self.maxXPosition:
            self.x += mx
            self.moveBack = True

        else:
            self.x -= mx
        if self.x > self.startingPosition:
            self.damage = 0
            self.moveBack = False
            self.x = startingPosi

    def dealDamage(self, md=1, d=2, ch=0, a=0):
        dmg = random.randint(((8-d)*md),((8+d)*md))
        getCritChance = random.randint(1,10)
        if (ch/10) >= getCritChance:
            dmg = dmg*2
        armorGain = (a/100)*dmg
        return int(dmg - armorGain)
    
class animationClass:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def moveAnimation(self, m=200, mx=20, my=20):
        self.max = m
        self.x += mx
        self.y += my
    
    def gainMana(self, mana, gain):
        return (mana+gain)

    def dealDamage(self, md=2, d=1, ch=10, a=0, sp=0):
        dmg = random.randint(((5-d)*md),((5+d)*md))
        getCritChance = random.randint(1,10)
        if (ch/10) >= getCritChance:
            dmg = dmg*2
        spellPowerGain = (sp/100)*dmg
        dmg = dmg + spellPowerGain
        armorGain = (a/100)*dmg
        return int(dmg - armorGain)
woodenStick = {
    "spellDMG": 5,
    "critChance": 10,
    "attack": 5,
    "spellPower": 0,
    "armor": 0,
    "healthpoints": 100,
    "manapoints": 100
}
manaDMG = False
run = True
while run:
    if roundStart:
        weapon = woodenStick
        HP = weapon["healthpoints"]
        mana = weapon["manapoints"]
        manaStart = weapon["manapoints"]
        HPStart = weapon["healthpoints"]
        armor = weapon["armor"]
        roundStart = False
        monsterF = monsterAni(monster1, 600, 300, 440, 600)
    #if monsterHP < 1 or HP < 1:
        #
    if mana < 2 and canAttack == True:
        yourTurn = False
    fireDMG = False
    lightDMG = False
    icebDMG = False
    critText = False
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    keys = pygame.key.get_pressed()
    win.blit(desert, (0,0))
    monsterHPT = str(monsterHP)
    text19 = font.render(monsterHPT, True, (255,0,0))
    textRect19 = text19.get_rect()
    textRect19.center = (750, 260)
    if monsterHP > 0:
        win.blit(monsterF.image, (monsterF.x,monsterF.y))
        monsterHPBAR = pygame.draw.rect(win, (0,128,0), (650,250,(monsterHP*2),50))
        win.blit(text19, textRect19)
    manaT = str(mana)
    HPT = str(HP)
    if HP > 0:
        win.blit(wizard, (70,300))
    manaText = font.render(manaT, True, (255,0,0))
    HPText = font.render(HPT, True, (255,0,0))
    textRectMana = manaText.get_rect()
    textRectHP = HPText.get_rect()
    textRectMana.center = (250, 310)
    textRectHP.center = (250,260)
    if mana > 0:
        manaBAR = pygame.draw.rect(win, (0,0,255), (150,300,(200*(mana/manaStart)),50))
    if HP > 0:
        HPBAR = pygame.draw.rect(win, (0,128,0), (150,250,(200*(HP/HPStart)),50))
    win.blit(manaText, textRectMana)
    win.blit(HPText, textRectHP)
    if lightAni:
        win.blit(lightning, (400,lightningAni.y))
        lightningAni.moveAnimation(-100,0,10)
        if lightningAni.y >= lightningAni.max:
            lightAni = False
    if icebAni:
        win.blit(iceb, (iceAni.x, iceAni.y))
        iceAni.moveAnimation(100,0,-20)
        textIceb = font.render("+7 armor", True, (255,0,0))
        textRectIceb = textIceb.get_rect()
        textRectIceb.center = (250, 150)
        win.blit(textIceb, textRectIceb)
        if iceAni.y <= iceAni.max:
            icebAni = False
    if fireAni:
        win.blit(fireball, (pyroAni.x,pyroAni.y))
        pyroAni.moveAnimation(200,20,20)
        if pyroAni.y >= pyroAni.max:
            fireAni = False
    if mana >= 2 and yourTurn and canAttack:
        if keys[pygame.K_l]:
            lightningAni = animationClass(400,-500)
            lightAni = True
            lightDMG = True
            yourTurn = False
    if keys[pygame.K_m]:
        manaAni = animationClass(9999,9999)
        manaDMG = True
        yourTurn = False
    if mana >= 10 and yourTurn and canAttack:
        if keys[pygame.K_i]:
            iceAni = animationClass(-200,1000)
            icebAni = True
            icebDMG = True
            yourTurn = False
    if mana >= 13 and yourTurn and canAttack:
        if keys[pygame.K_f]:
            pyroAni = animationClass(-300,-500)
            fireAni = True
            fireDMG = True
            yourTurn = False
    if fireDMG and dmgonce == False:
        dmg = pyroAni.dealDamage(2,1,weapon["critChance"],0,weapon["spellPower"])
        mana -= 13
        monsterHP -= dmg
        dmgonce = True
        shDMGText = True
    if manaDMG and dmgonce == False:
        mana = manaAni.gainMana(mana, 15)
        dmgonce = True
    if icebDMG and dmgonce == False:
        armor += 7
        mana -= 10
        dmgonce = True
    if lightDMG and dmgonce == False:
        dmg = lightningAni.dealDamage(1,1,weapon["critChance"],0,weapon["spellPower"])
        mana -= 2
        monsterHP -= dmg
        dmgonce = True
        shDMGText = True
    if not lightDMG and not fireDMG and not icebDMG and not manaDMG and dmgonce:
        dmgonce = False
        shDMGText = False
    if shDMGText:
        dmgString = str(dmg)
        shDMGText = False
        shDMGText2 = True
    if shDMGText2:
        shTimer = 0
        shDMGText2 = False
    if shTimer <= 40:    
        dmgText = DMGFont.render(dmgString, True, (255,0,0))
        textRectDMG = dmgText.get_rect()
        textRectDMG.center = (900, 150)
        win.blit(dmgText, textRectDMG)
        shTimer += 1
    if yourTurn == False:
        canAttack = False
        monsterAttack = True
        yourTurn = True
        monsterPause = 0
        monsterTimer = 0
    if monsterAttack and monsterHP > 0:
        if monsterPause > 40:
            monsterF.moveAnimation(20, 0, 600)
            if monsterTimer == 9:
                dmg = monsterF.dealDamage(1, 2, 0, armor)
                HP -= dmg
                shDMGText = True
            if monsterTimer > 17:
                monsterAttack = False
                yourTurn = True
                canAttack = True
            monsterTimer += 1
        monsterPause += 1
pygame.quit()
