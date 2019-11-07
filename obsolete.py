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
armor = 0
monsterTimer = 20
win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("BattleOn")
lightY = -500
mandX = 25
mandY = 25
shMonster = True
dmg = 0
yourTurn = True
shCritText = 0
dmgString = ""
shDMGText2 = False
shTimer = 41
fireX = -300
critchance = 1
fireY = -500
monsterHP = 100
manaStart = 100
HPStart = 100
monsterAttack = False
monsterPause = 100
critText = False
icebY = 1000
monster = pygame.image.load("monster.png")
desert = pygame.image.load("desert.jpg")
lightning = pygame.image.load("lightning.png")
fireball = pygame.image.load("fireball.png")
wizard = pygame.image.load("wizard.png")
iceb = pygame.image.load("iceb.png")
roundStart = True
run = True
while run:
    if roundStart:
        HP = HPStart
        mana = manaStart
        roundStart = False 
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
        if shMonster:
            win.blit(monster, (600,300))
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
    #win.blit(mand, (mandX,mandY))
    #win.blit(svaerd, (svaerdX,svaerdY))
    if lightAni:
        win.blit(lightning, (400,lightY))
        if lightY < -100:
            lightY += 10
        if lightY >= -100:
            lightAni = False
            lightY = -500
    if icebAni:
        win.blit(iceb, (-200, icebY))
        if icebY > 100:
            icebY -= 20
        if icebY <= 100:
            icebAni = False
            icebY = 1000
        textIceb = font.render("+7 armor", True, (255,0,0))
        textRectIceb = textIceb.get_rect()
        textRectIceb.center = (250, 150)
        win.blit(textIceb, textRectIceb)
    if fireAni:
        win.blit(fireball, (fireX,fireY))
        if fireY < 200:
            fireY += 20
            fireX += 20
        if fireY >= 200:
            fireAni = False
            fireY = -500
            fireX = -300
    if mana >= 2 and yourTurn and canAttack:
        if keys[pygame.K_l]:
            lightAni = True
            lightDMG = True
            yourTurn = False
    if mana >= 10 and yourTurn and canAttack:
        if keys[pygame.K_i]:
            icebAni = True
            icebDMG = True
            yourTurn = False
    if mana >= 13 and yourTurn and canAttack:
        if keys[pygame.K_f]:
            fireAni = True
            fireDMG = True
            yourTurn = False
    if fireDMG and dmgonce == False:
        dmg = random.randint(8,12)
        mana -= 13
        crit = random.randint(1,10)
        if critchance >= crit:
            dmg = (dmg*2) 
            critText = True
        monsterHP -= dmg
        dmgonce = True
        shDMGText = True
    if icebDMG and dmgonce == False:
        armor += 7
        mana -= 10
        dmgonce = True
    if lightDMG and dmgonce == False:
        dmg = random.randint(4,6)
        mana -= 2
        crit = random.randint(1,10)
        if critchance >= crit:
            dmg = (dmg*2)
            critText = True
        monsterHP -= dmg
        dmgonce = True
        shDMGText = True
    if not lightDMG and not fireDMG and not icebDMG and dmgonce:
        dmgonce = False
        shDMGText = False
    if shDMGText:
        dmgString = str(dmg)
        if critText:
            dmgString = "CRIT! " + dmgString
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
        if monsterPause > 50:
            shMonster = False
            if monsterTimer == 0 or monsterTimer == 20:
                win.blit(monster, (600,300))
            if monsterTimer == 1 or monsterTimer == 19:
                win.blit(monster, (580,300))
            if monsterTimer == 2 or monsterTimer == 18:
                win.blit(monster, (560,300))
            if monsterTimer == 3 or monsterTimer == 17:
                win.blit(monster, (540,300))
            if monsterTimer == 4 or monsterTimer == 16:
                win.blit(monster, (520,300))
            if monsterTimer == 5 or monsterTimer == 15:
                win.blit(monster, (500,300))
            if monsterTimer == 6 or monsterTimer == 14:
                win.blit(monster, (480,300))
            if monsterTimer == 7 or monsterTimer == 13:
                win.blit(monster, (460,300))
            if monsterTimer == 8 or monsterTimer == 12:
                win.blit(monster, (440,300))
            if monsterTimer == 9 or monsterTimer == 10:
                win.blit(monster, (420,300))
            if monsterTimer == 9:
                dmg = random.randint(6,10)
                dmg = int((dmg*((100-armor)/100)))
                HP -= dmg
                shDMGText = True
            if monsterTimer > 20:
                monsterAttack = False
                shMonster = True
                yourTurn = True
                canAttack = True
            monsterTimer += 1
        monsterPause += 1
pygame.quit()
