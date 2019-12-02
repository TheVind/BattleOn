import pygame
import random

#Initiate Pygame and fonts (text to screen)
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Ugandan BattleOn")

#Sets a font, to use for damage text
BigFont = pygame.font.Font('freesansbold.ttf', 40)
font = pygame.font.Font('freesansbold.ttf', 16)

#Dictionaries for weapon
woodenStick = {
    "price": 0,
    "name": "woodenStick",
    "critChance": 10,
    "attack": 5,
    "spellPower": 0,
    "armor": 0,
}

broadSword = {
    "name": "broadSword",
    "critChance": 20,
    "attack": 10,
    "spellPower": 0,
    "armor": 5,
    "price": 100
}
crystalStaff= {
    "name": "crystalStaff",
    "critChance": 50,
    "attack": 5,
    "spellPower": 300,
    "armor": 0,
    "price": 15
}

#Import images
#imports our loading screen, kinda scuffed - needs to be changed
loading = pygame.image.load("loadingScreen.jpg")
#Town image imported
townImage = pygame.image.load("bgtownFinal.jpg")
#Download fireball and lightning image
fireball = pygame.image.load("fireball.png")
lightning = pygame.image.load("lightning.png")
#Button imported
scuffedButton = pygame.image.load("saveGame.png")
#Gets saving background screen
savedScreen = pygame.image.load("saveScreen.jpg")
#Gets the battle background
battlebg = pygame.image.load("forest.jpg")
#Gets scuffed button
battleButton = pygame.image.load("battleB.png")
battleButtonRed = pygame.image.load("battleBRed.png")
exitButton = pygame.image.load("exit.png")
hoverExitButton = pygame.image.load("hoverExit.png")
hoverSaveGame = pygame.image.load("hoverSaveGame.png")
hoverWeaponShop = pygame.image.load("hoverWeaponShop.png")
hoverWeapons = pygame.image.load("hoverWeapons.png")
#Gets the wizard image
wizard = pygame.image.load("wizard.png")
zulul = pygame.image.load("ZULUL.png")
#Gets the monster
monster = pygame.image.load("monster.png")
# IMPORTS THE NUMBERS FOR THE BATTLE SCENE
normal2 = pygame.image.load("normal2.png")
normal1 = pygame.image.load("normal1.png")
greyed2 = pygame.image.load("greyed2.png")
hover1 = pygame.image.load("hover1.png")
hover2 = pygame.image.load("hover2.png")
hover3 = pygame.image.load("hover3.png")
normal3 = pygame.image.load("normal3.png")
greyed3 = pygame.image.load("greyed3.png")
hover4 = pygame.image.load("hover4.png")
normal4 = pygame.image.load("normal4.png")
greyed4 = pygame.image.load("greyed4.png")
hover5 = pygame.image.load("hover5.png")
normal5 = pygame.image.load("normal5.png")
greyed5 = pygame.image.load("greyed5.png")
hover6 = pygame.image.load("hover6.png")
normal6 = pygame.image.load("normal6.png")
greyed6 = pygame.image.load("greyed6.png")
hover7 = pygame.image.load("hover7.png")
normal7 = pygame.image.load("normal7.png")
greyed7 = pygame.image.load("greyed7.png")
hover8 = pygame.image.load("hover8.png")
normal8 = pygame.image.load("normal8.png")
greyed8 = pygame.image.load("greyed8.png")
hover9 = pygame.image.load("hover9.png")
normal9 = pygame.image.load("normal9.png")
greyed9 = pygame.image.load("greyed9.png")
normalBoss = pygame.image.load("normalBoss.png")
greyedBoss = pygame.image.load("greyedBoss.png")
hoverBoss = pygame.image.load("hoverBoss.png")
#Import pictures for end scene
winnerbg = pygame.image.load("youAreWinner.png")
continueButton = pygame.image.load("continue.png")
hoverContinueButton = pygame.image.load("hoverContinue.png")
resetSlotButton = pygame.image.load("resetSlot.png")
hoverResetSlotButton = pygame.image.load("hoverResetSlot.png")
#Loads death screen
uDed = pygame.image.load("uDed.png")
#Import weapon overview button
weaponButton = pygame.image.load("weapons.png")
#Import shop for weapons-button
weaponShopButton = pygame.image.load("weaponShop.png")
#Import the weapons
crystalStaffImage = pygame.image.load("crystalStaff.png")
crystalStaffGreyedImage = pygame.image.load("crystalStaffGREYED.png")
woodenStickImage = pygame.image.load("woodenStick.png")
woodenStickGreyedImage = pygame.image.load("woodenStickGREYED.png")
broadSwordImage = pygame.image.load("broadSword.png")
broadSwordGreyedImage = pygame.image.load("broadSwordGREYED.png")
#Import the Attack menu + hover
attackMenu = pygame.image.load("AttackBar.jpg")
atkHover = pygame.image.load("attackHover.jpg")
fireHover = pygame.image.load("fireballHover.jpg")
lightHover = pygame.image.load("lightningHover.jpg")
#topleft small icon
pygame.display.set_icon(zulul)

#THIS SECTION NEEDS COMMENTS
class PlayerClass:

    def __init__(self, image, x=300, y=300, hp=100, mana=100, weapons=[woodenStick], equipped=woodenStick, gold=0, reachedLevel=1):
        #having this paramter makes us able to swap character model
        self.image = image
        self.x = x
        self.y = y
        self.startHP = int(hp)
        self.startMP = int(mana)
        self.HP = int(hp)
        self.MP = int(mana)
        self.weapons = weapons
        self.weaponEquipped = equipped
        #Parameter to gain/lose gold to get new weapon 
        self.gold = int(gold)
        self.startX = x
        self.startY = y
        self.moveBack = False
        self.reachedLevel = reachedLevel

    def moveAnimation(self):
        self.x += 20
        if self.x >= 500:
            self.moveBack = True
        if self.moveBack:
            self.x -= 40
        if self.startX > self.x:
            self.moveBack = False
            return False
        else:
            return True
    
    def checkMana(self):
        return True

    def resetXY(self):
        self.x = self.startX
        self.y = self.startY

    def dealDamage(self, critCh=10, a=0, sp=0, attack=0):
        dmg = random.randint(int(attack-(attack*0.1)),int(attack+(attack*0.1)))
        #Variable to generate chance to crit - random number between 1 and 10
        getCritChance = random.randint(1,10)
        #Checking for crit dynamically
        if (critCh/10) >= getCritChance:
            #the actual bonus dmg calculation
            dmg = dmg*2
        #Takes the armor of the monster, and finds out how much damage the armor absorbs
        armorPrevail = (a/100)*dmg
        #Returns the final damage value, with the amount of damage dealt minus the damage absorbed by armor
        return int(dmg - armorPrevail)

    def addWeapon(weapon):
        self.weapons.append(weapon)

    def goldChange(changeOfGold):
        self.gold += changeOfGold

    def fullHP(self):
        self.HP = self.startHP
    

#Defines the monster animation and attack
class MonsterClass:
#the init function defining all the default values when you first call it
#This functions holds all the paramteres we need the monster to have
    def __init__(self, image=loading, x=600, y=300, maxX = 440, HP=100, goldDrop=1, dmgMulti=1, difference=2, critCh=0, baseDamage=8):
        self.image = image
        #Image position for the x coordinate in pygame
        self.x = x
        #image position for the y coordinate in pygame
        self.y = y
        #variable to determine, which way the monster need to move, depeding on position of the x coordinate
        self.moveBack = False
        #Dmg number to pop up on screen - in testing
        self.damage = 0
        #The x starting position for the monster
        self.startingPosition = x
        #The threshold to which the monster can't move anymore, so it doesnt stand on top of player
        self.maxXPosition = maxX
        self.HP = HP
        self.startHP = HP
        self.goldDrop = goldDrop
        self.dmgMulti = dmgMulti
        self.difference = difference
        self.critCh = critCh
        self.baseDamage = baseDamage

    #function that moves the monster on screen + gives feedback to indicate when monster is done attack/ready to attack
    def moveAnimation(self, mx=20, my=0, startingPosi=600):
        #when variable moveBack = true add mx, which is 20px, to monsters x pos making it go backwards on the screen
        if self.moveBack:
            self.x += mx
        #When monsters x variable gets lower than maxX variable set moveBack = True, which runs the code above
        elif self.x < self.maxXPosition:
            self.x += mx
            self.moveBack = True
            #comment something
            return "attack"
        else:
            self.x -= mx
        if self.x > self.startingPosition:
            self.damage = 0
            self.moveBack = False
            self.x = startingPosi
            return "end"
        return False

    #Monster dmg function to determine dmg and crit
    def dealDamage(self, a=0):
        #the dmg calulation it self
        dmg = random.randint(((self.baseDamage-self.difference)*self.dmgMulti),((self.baseDamage+self.difference)*self.dmgMulti))
        #the calculation of the crit chance - default is set so the monster cannot crit - further explained in the spell class
        getCritChance = random.randint(1,10)
        if (self.critCh/10) >= getCritChance:
            dmg = dmg*2
        armorGain = (a/100)*dmg
        return int(dmg - armorGain)

#Class for the player, both dealing damage and animating
class SpellClass:
    def __init__(self, x=0, y=0, image=loading, manaCost=13, dmgMulti=2, difference=1, maxy=200, movex=20, movey=20):
        self.x = x
        self.y = y
        self.startX = x
        self.startY = y
        #Sets the image to use for the animation
        self.image = image
        self.manaCost = manaCost
        self.dmgMulti = dmgMulti
        self.difference = difference
        self.max = maxy
        self.movex = movex
        self.movey = movey
    #the moving of the spell picture - animation
    def moveAnimation(self):
        self.x += self.movex
        self.y += self.movey
        if self.max == self.y:
            return False
        else:
            return True
    def checkMana(self):
        if Player.MP < self.manaCost:
            return "noMana"
        else:
            return "enoughMana"
    def resetXY(self):
        self.x = self.startX
        self.y = self.startY
    def gainMana(self, mana, gain):
        return (mana+gain)

    def dealDamage(self, critCh=10, a=0, sp=0, attack=0):
        if not Player.MP < self.manaCost:
            dmg = random.randint(((5-self.difference)*self.dmgMulti),((5+self.difference)*self.dmgMulti))
        #Variable to generate chance to crit - random number between 1 and 10
            getCritChance = random.randint(1,10)
        #Checking for crit dynamically
            if (critCh/10) >= getCritChance:
            #the actual bonus dmg calculation
                dmg = dmg*2
        #Add dmg to your attack depending on the amount of spellpower your weapon has
            spellPowerGain = (sp/100)*dmg
            dmg = dmg + spellPowerGain
        #Takes the armor of the monster, and finds out how much damage the armor absorbs
            armorPrevail = (a/100)*dmg
            Player.MP -= self.manaCost
        #Returns the final damage value, with the amount of damage dealt minus the damage absorbed by armor
            return int(dmg - armorPrevail)
        return "noMana"

FireballClass = SpellClass(-200, -500, fireball, 13, 2, 1, 200, 20, 20)
LightningClass = SpellClass(660, -500, lightning, 3, 1, 1, 0, 0, 20)


#Sets variable to make the loop ask for a slot to load before anything else
scene = "startOfGame"

#Sets run to True, so the eternity loop, which Pygame is, can run as long as you want.
run = True
while run:
#The variables below are going to get repeated in the other loops, since we always need the state of mouse and keyboard
#Gets the value of the keys pressed
    keys = pygame.key.get_pressed()
#Gets the state of the mouse - useless for now
    mouseC = pygame.mouse.get_pressed()
#Gets location of mouse - useless for now? not sure why it doesnt work
    mouseL = pygame.mouse.get_pos()
    #Thoughts on how to load game upon pressing "start"
    while scene == "startOfGame":
        #This function is sort of like the sync() function we learned while talking about reading and writing to files in python
        #It basiclly forces the update to happen, which is often what is required in pygame to make something happen
        pygame.display.update()
        #This function is used to speed up or slow down the program to you wishes, it takes the paramter milliseconds
        pygame.time.delay(20)
        #win.blit is the function which we use to draw everything you see on the screen; like background, characters, text and even animations
        win.blit(loading, (0,0))
#Goes through all the event that happens (with the mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                scene = "exit"
#After you click, and release your finger from the left-click, do:
            if event.type == pygame.MOUSEBUTTONUP:
                #Gets location of mouse - useless for now? not sure why it doesnt work
                mouseL = pygame.mouse.get_pos()
#If the mouse is in this range mouseL[0] in range (X,X) and mouse[1] in range (Y,Y) - CHANGE COMMENT:
                if mouseL[0] in range(100,250) and mouseL[1] in range (200,350):
#If you click slot1, it will load slot1
                    slotNumber = 1
                    FileHandler = open("slot1.txt", "r")
                elif mouseL[0] in range(400,550) and mouseL[1] in range (200,350):
                    slotNumber = 2
                    FileHandler = open("slot2.txt", "r")
                elif mouseL[0] in range(700,850) and mouseL[1] in range (200,350):
                    slotNumber = 3
                    FileHandler = open("slot3.txt", "r")
#If you do not select a slot, it does nothing, and continues to the top of the loop
                else:
                    continue

#Sets an array to put in the output from the filehandler
                outputFromSlot = []
#Reads the lines in the file
                theLines = FileHandler.readlines()
#Goes through the lines, and put them into the array named outputFromSlot
                for line in theLines:
#Replaces "\n" with nothing, since this naturally occurs on the line, AND WE DONT WANT IT
                    outputFromSlot.append(line.replace("\n", ""))
#Closes the filehandler, since we do not need it anymore, since we have the values in a local array
                FileHandler.close()
                # Defines an array to put the weapons you have into
                weaponArray = []
                outputFromSlot[2] = outputFromSlot[2].split()
                for singleWeapon in outputFromSlot[2]:
                    weaponArray.append(singleWeapon)

#Sets the class of the player
                Player = PlayerClass(wizard, 70, 300, int(outputFromSlot[0]), int(outputFromSlot[1]), weaponArray, outputFromSlot[3], int(outputFromSlot[4]), int(outputFromSlot[5]))
    # Shifts to the town
                scene = "town"

    #Need something to trigger this thing, but it will write to the file selected
    while scene == "saveGame":
        pygame.display.update()
        pygame.time.delay(20)
        #Gets location of mouse - useless for now? not sure why it doesnt work
        mouseL = pygame.mouse.get_pos()
        win.blit(savedScreen,(0,0))
        if mouseL[0] in range(465,565) and mouseL[1] in range(500,540):
            win.blit(hoverExitButton,(465,500))
        else:
            win.blit(exitButton,(465,500))
        if not saveSlot == False:
            textRectSave = (BigFont.render(str(saveSlot), True, (255,255,255))).get_rect()
            textRectSave.center = (210,520)
            win.blit((BigFont.render(str(saveSlot), True, (255,255,255))), textRectSave)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                scene = "exit"
#After you click, and release your finger from the left-click, do:
            if event.type == pygame.MOUSEBUTTONUP:
#If the mouse is in this range:
                if mouseL[0] in range(100,250) and mouseL[1] in range (200,350):
#If you click slot1, it will load slot1
                    FileHandler = open("slot1.txt", "w")
                    saveSlot = "Game saved to Slot 1"
                elif mouseL[0] in range(400,550) and mouseL[1] in range (200,350):
                    FileHandler = open("slot2.txt", "w")
                    saveSlot = "Game saved to Slot 2"
                elif mouseL[0] in range(700,850) and mouseL[1] in range (200,350):
                    FileHandler = open("slot3.txt", "w")
                    saveSlot = "Game saved to Slot 3"
#If you do not select a slot, it does nothing, and continues to the top of the loop
                elif mouseL[0] in range(465,545) and mouseL[1] in range(500,540):
                    #This is the way we change scene from loading to the town scene 
                    scene = "town"
                    continue
                else:
                    continue
                FileHandler.write(str(Player.HP))
                FileHandler.write("\n")
                FileHandler.write(str(Player.MP))
                FileHandler.write("\n")
                for singleWeapon in Player.weapons:
                    #FileHandler.write(singleWeapon["name"])
                    FileHandler.write(singleWeapon)
                    FileHandler.write(" ")
                FileHandler.write("\n") 
                FileHandler.write(Player.weaponEquipped)
                FileHandler.write("\n")
                FileHandler.write(str(Player.gold))
                FileHandler.write("\n")
                FileHandler.write(str(Player.reachedLevel))
                FileHandler.close()
                                 
    
    
    while scene == "town":
        pygame.time.delay(20)
        pygame.display.update()
        mouseL = pygame.mouse.get_pos()
        win.blit(townImage, (0,0))
        #pygame.draw.rect(win, (255,0,0), (50, 350, 150, 40))
        if mouseL[0] in range(850,1000) and mouseL[1] in range(350,390):
            win.blit(hoverSaveGame,(850,350))
        else:
            win.blit(scuffedButton, (850,350))
        if mouseL[0] in range(300,430) and mouseL[1] in range(350,390):
            win.blit(hoverWeapons,(300,350))
        else:    
            win.blit(weaponButton,(300,350))
        if mouseL[0] in range(550,720) and mouseL[1] in range(350,390):
            win.blit(hoverWeaponShop,(550,350))
        else:
            win.blit(weaponShopButton,(550,350))
        #Mouse over effect for the battle button (just for show)
        if mouseL[0] in range(50,200) and mouseL[1] in range(350,390):
            win.blit(battleButtonRed, (50,350))
        else:
            win.blit(battleButton, (50,350))
        #Function to quit the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                scene = "exit"
#After you click, and release your finger from the left-click, do:
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseL[0] in range(850,1000) and mouseL[1] in range(350,390):
                    saveSlot = False
                    scene = "saveGame"
                elif mouseL[0] in range(50,200) and mouseL[1] in range(350,390):
                    townLoop = True
                    while townLoop:
                        pygame.time.delay(20)
                        pygame.display.update()
                        mouseL = pygame.mouse.get_pos()
                        win.blit(townImage, (0,0))
                        if mouseL[0] in range(150,250) and mouseL[1] in range(150,250):
                            win.blit(hover1,(150,150))
                        else:
                            win.blit(normal1,(150,150))
                        if mouseL[0] in range(300,400) and mouseL[1] in range(150,250) and Player.reachedLevel >= 2:
                            win.blit(hover2,(300,150))
                        elif Player.reachedLevel < 2:
                            win.blit(greyed2,(300,150))
                        else:
                            win.blit(normal2,(300,150))
                        if mouseL[0] in range(450,550) and mouseL[1] in range(150,250) and Player.reachedLevel >= 3:
                            win.blit(hover3,(450,150))
                        elif Player.reachedLevel < 3:
                            win.blit(greyed3,(450,150))
                        else:
                            win.blit(normal3,(450,150))
                        if mouseL[0] in range(150,250) and mouseL[1] in range(300,400) and Player.reachedLevel >= 4:
                            win.blit(hover4,(150,300))
                        elif Player.reachedLevel < 4:
                            win.blit(greyed4,(150,300))
                        else:
                            win.blit(normal4,(150,300))
                        if mouseL[0] in range(300,400) and mouseL[1] in range(300,400) and Player.reachedLevel >= 5:
                            win.blit(hover5,(300,300))
                        elif Player.reachedLevel < 5:
                            win.blit(greyed5,(300,300))
                        else:
                            win.blit(normal5,(300,300))
                        if mouseL[0] in range(450,550) and mouseL[1] in range(300,400) and Player.reachedLevel >= 6:
                            win.blit(hover6,(450,300))
                        elif Player.reachedLevel < 6:
                            win.blit(greyed6,(450,300))
                        else:
                            win.blit(normal6,(450,300))
                        if mouseL[0] in range(150,250) and mouseL[1] in range(450,550) and Player.reachedLevel >= 7:
                            win.blit(hover7,(150,450))
                        elif Player.reachedLevel < 7:
                            win.blit(greyed7,(150,450))
                        else:
                            win.blit(normal7,(150,450))
                        if mouseL[0] in range(300,400) and mouseL[1] in range(450,550) and Player.reachedLevel >= 8:
                            win.blit(hover8,(300,450))
                        elif Player.reachedLevel < 8:
                            win.blit(greyed8,(300,450))
                        else:
                            win.blit(normal8,(300,450))
                        if mouseL[0] in range(450,550) and mouseL[1] in range(450,550) and Player.reachedLevel >= 9:
                            win.blit(hover9,(450,450))
                        elif Player.reachedLevel < 9:
                            win.blit(greyed9,(450,450))
                        else:
                            win.blit(normal9,(450,450))
                        if mouseL[0] in range(600,700) and mouseL[1] in range(150,550) and Player.reachedLevel >= 10:
                            win.blit(hoverBoss,(600,150))
                        elif Player.reachedLevel < 10:
                            win.blit(greyedBoss,(600,150))
                        else:
                            win.blit(normalBoss,(600,150))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                scene = "exit"
                                townLoop = False
                            if event.type == pygame.MOUSEBUTTONUP:
                                if mouseL[0] in range(150,250) and mouseL[1] in range(150,250):
                                    scene = "battle"
                                    monsterLevel = 1
                                    townLoop = False
                                elif mouseL[0] in range(300,400) and mouseL[1] in range(150,250):
                                     if Player.reachedLevel >= 2:
                                        scene = "battle"
                                        monsterLevel = 2
                                        townLoop = False
                                elif mouseL[0] in range(450,550) and mouseL[1] in range(150,250):
                                     if Player.reachedLevel >= 3:
                                        scene = "battle"
                                        monsterLevel = 3
                                        townLoop = False
                                elif mouseL[0] in range(150,250) and mouseL[1] in range(300,400):
                                     if Player.reachedLevel >= 4:
                                        scene = "battle"
                                        monsterLevel = 4
                                        townLoop = False
                                elif mouseL[0] in range(300,400) and mouseL[1] in range(300,400):
                                     if Player.reachedLevel >= 5:
                                        scene = "battle"
                                        monsterLevel = 5
                                        townLoop = False
                                elif mouseL[0] in range(450,550) and mouseL[1] in range(300,400):
                                     if Player.reachedLevel >= 6:
                                        scene = "battle"
                                        monsterLevel = 6
                                        townLoop = False
                                elif mouseL[0] in range(150,250) and mouseL[1] in range(450,550):
                                     if Player.reachedLevel >= 7:
                                        scene = "battle"
                                        monsterLevel = 7
                                        townLoop = False
                                elif mouseL[0] in range(300,400) and mouseL[1] in range(450,550):
                                     if Player.reachedLevel >= 8:
                                        scene = "battle"
                                        monsterLevel = 8
                                        townLoop = False
                                elif mouseL[0] in range(450,550) and mouseL[1] in range(450,550):
                                     if Player.reachedLevel >= 9:
                                        scene = "battle"
                                        monsterLevel = 9
                                        townLoop = False
                                elif mouseL[0] in range(600,700) and mouseL[1] in range(150,550):
                                     if Player.reachedLevel >= 10:
                                        scene = "battle"
                                        monsterLevel = 10
                                        townLoop = False
                                else:
                                    townLoop = False
                elif mouseL[0] in range(550,700) and mouseL[1] in range(350,390):
                    townLoop = True
                    while townLoop:
                        win.blit(townImage, (0,0))
                        mouseL = pygame.mouse.get_pos()
                        if mouseL[0] in range(50,175) and mouseL[1] in range(50,175):
                            weaponString = "Name: %s, Price: %s, Crit chance: %s, Attack: %s, Spell Power: %s, Armor: %s" % (woodenStick["name"], woodenStick["price"], woodenStick["critChance"], woodenStick["attack"], woodenStick["spellPower"], woodenStick["armor"])
                        elif mouseL[0] in range(200,325) and mouseL[1] in range(50,175):
                            weaponString = "Name: %s, Price: %s, Crit chance: %s, Attack: %s, Spell Power: %s, Armor: %s" % (broadSword["name"], broadSword["price"], broadSword["critChance"], broadSword["attack"], broadSword["spellPower"], broadSword["armor"])
                        elif mouseL[0] in range(350,475) and mouseL[1] in range(50,175):
                            weaponString = "Name: %s, Price: %s, Crit chance: %s, Attack: %s, Spell Power: %s, Armor: %s" % (crystalStaff["name"], crystalStaff["price"], crystalStaff["critChance"], crystalStaff["attack"], crystalStaff["spellPower"], crystalStaff["armor"])
                        else:
                            weaponString = ""
                        weaponInfo = font.render(weaponString, True, (255,255,255))
                        weaponInfoRect = weaponInfo.get_rect()
                        weaponInfoRect.center = (550,260)
                        win.blit(weaponInfo, weaponInfoRect)
                        textForGold = "Gold: " + str(Player.gold)
                        textRectHP = (BigFont.render(str(textForGold), True, (255,255,255))).get_rect()
                        textRectHP.center = (250,550)
                        win.blit((BigFont.render(str(textForGold), True, (255,255,255))), textRectHP)
                        if "woodenStick" not in Player.weapons:
                            win.blit(woodenStickImage,(50,50))
                        else:
                            win.blit(woodenStickGreyedImage,(50,50))
                        if "broadSword" not in Player.weapons:
                            win.blit(broadSwordImage,(200,50))
                        else:
                            win.blit(broadSwordGreyedImage,(200,50))
                        if "crystalStaff" not in Player.weapons:
                            win.blit(crystalStaffImage,(350,50))
                        else:
                            win.blit(crystalStaffGreyedImage,(350,50))
                        pygame.time.delay(20)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                scene = "exit"
                                townLoop = False
                            if event.type == pygame.MOUSEBUTTONUP:
                                if mouseL[0] in range(50,175) and mouseL[1] in range(50,175):
                                    if "woodenStick" not in Player.weapons:
                                        Player.weapons.append("woodenStick")
                                elif mouseL[0] in range(200,325) and mouseL[1] in range(50,175):
                                    if "broadSword" not in Player.weapons and Player.gold >= broadSword["price"]:
                                        Player.gold -= broadSword["price"]
                                        Player.weapons.append("broadSword")
                                elif mouseL[0] in range(350,475) and mouseL[1] in range(50,175):
                                    if "crystalStaff" not in Player.weapons and Player.gold >= crystalStaff["price"]:
                                        Player.gold -= crystalStaff["price"]
                                        Player.weapons.append("crystalStaff")
                                else:
                                    townLoop = False
                #If you click inside the "Weapons" button, do:
                elif mouseL[0] in range(300,450) and mouseL[1] in range(350,390):
                    #Enters a loop, to not make it run through as few things as possible for each iteration
                    townLoop = True
                    while townLoop:
                        #Makes new background, since the graphics (which have been amended) otherwise stays
                        win.blit(townImage, (0,0))
                        #If you do not have "Wooden Stick" in you inventory, you cannot equip it, therefore it displays a greyed out image
                        if "woodenStick" not in Player.weapons:
                            win.blit(woodenStickGreyedImage,(50,50))
                        #If it didn't match on the if-sentence above, you must have it in your inventory, and you can therefore equip it.
                        else:
                            #If you have "Wooden Stick" equipped, it draws a green bar around it, so you can see which weapon you have equipped.
                            if "woodenStick" == Player.weaponEquipped:
                                #Draws the bar around it.
                                pygame.draw.rect(win, (0,255,0), (45, 45, 135, 135))
                            #Draws the non-greyed out image of "Wooden Stick" (after the green box, since you want the Wooden Stick to be in the front)
                            win.blit(woodenStickImage,(50,50))
                        #Same as with "Wooden Stick"
                        if "broadSword" not in Player.weapons:
                            win.blit(broadSwordGreyedImage,(200,50))
                        else:
                            if "broadSword" == Player.weaponEquipped:
                                pygame.draw.rect(win, (0,255,0), (195, 45, 135, 135))
                            win.blit(broadSwordImage,(200,50))
                        #Same as with "Wooden Stick"
                        if "crystalStaff" not in Player.weapons:
                            win.blit(crystalStaffGreyedImage,(350,50))
                        else:
                            if "crystalStaff" == Player.weaponEquipped:
                                pygame.draw.rect(win, (0,255,0), (345, 45, 135, 135))
                            win.blit(crystalStaffImage,(350,50))
                        pygame.time.delay(20)
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                scene = "exit"
                                townLoop = False
                            if event.type == pygame.MOUSEBUTTONUP:
                                mouseL = pygame.mouse.get_pos()
                                if mouseL[0] in range(50,175) and mouseL[1] in range(50,175):
                                    if "woodenStick" in Player.weapons:
                                        Player.weaponEquipped = "woodenStick"
                                elif mouseL[0] in range(200,325) and mouseL[1] in range(50,175):
                                    if "broadSword" in Player.weapons:
                                        Player.weaponEquipped = "broadSword"
                                elif mouseL[0] in range(350,475) and mouseL[1] in range(50,175):
                                    if "crystalStaff" in Player.weapons:
                                        Player.weaponEquipped = "crystalStaff"
                                else:
                                    townLoop = False
                                print(Player.weaponEquipped)
                else:
                    continue

#Loads the variables before battle
    if scene == "battle":
#Loads the monster
        if monsterLevel == 1:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 1, 1, 2, 0, 8)
        elif monsterLevel == 2:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 5, 1, 4, 10, 8)
        elif monsterLevel == 3:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 10, 1, 2, 0, 10)
        elif monsterLevel == 4:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 20, 2, 2, 0, 7)
        elif monsterLevel == 5:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 40, 2, 2, 0, 8)
        elif monsterLevel == 6:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 80, 2, 5, 50, 8)
        elif monsterLevel == 7:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 160, 3, 2, 0, 8)
        elif monsterLevel == 8:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 320, 4, 4, 0, 7)
        elif monsterLevel == 9:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 640, 4, 2, 0, 10)
        elif monsterLevel == 10:
            Monster = MonsterClass(monster, 800, 300, 440, 100, 10000000000000000000, 3, 2, 0)
        else:
            print("ERROR!!!")
#Sets some variables for the fighting scene
        canAttack = True
        Player.fullHP()
#Sets the weapon
        #weapon = Player.weapons[Player.weaponEquipped]
        if Player.weaponEquipped == "woodenStick":
            weapon = woodenStick
        elif Player.weaponEquipped == "crystalStaff":
            weapon = crystalStaff
        elif Player.weaponEquipped == "broadSword":
            weapon = broadSword

# Variable to keep track on whether or not you have queued an attack
        runAnimation = False
#Shifts to the battle scene
        scene = "battleScene"

#The battle scene! - not much going on atm tho
    while scene == "battleScene":
        pygame.time.delay(20)
        mousePos = pygame.mouse.get_pos()
        pygame.display.update()
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #run = False
                #scene = "exit"
                canAttack = False


            if event.type == pygame.MOUSEBUTTONUP:
                if mousePos[0] in range(530, 630) and mousePos[1] in range(410, 490) and canAttack and not runAnimation:
            # Sets the variable used to make animation and deal damage equal to the class defined as fireball
                    spellVariable = FireballClass
            # Queues the attack through this variable
                    runAnimation = True
                elif mousePos[0] in range(530, 630) and mousePos[1] in range(500, 560) and canAttack and not runAnimation:
            # Same as above, but for lightning
                    spellVariable = LightningClass
                    runAnimation = True
                elif mousePos[0] in range(530, 630) and mousePos[1] in range(350, 400) and canAttack and not runAnimation:
                    spellVariable = Player
                    runAnimation = True
            #Hertil !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            

        #Renders the background for the scene
        win.blit(battlebg, (0,0))
        #Renders the model for the player
        win.blit(Player.image, (Player.x,Player.y))
        #Defines the text to show inside the mana bar
        textRectMana = (font.render(str(Player.MP), True, (255,255,255))).get_rect()
        #Defines the text to show inside the HP bar
        textRectHP = (font.render(str(Player.MP), True, (255,255,255))).get_rect()
        #Defines the position of the mana bar
        textRectMana.center = (250, 310)
        #Defines the position of the HP bar
        textRectHP.center = (250,260)
        #Draws the hp bar and makes it shorter in percentage as the player loses health
        hpBar = pygame.draw.rect(win, (0,128,0), (150,250,(200*(Player.HP/Player.startHP)),50))
        #Draws the mana bar and makes it shorter in percentage as the player uses mana
        manaBar = pygame.draw.rect(win, (0,0,255), (150,300,(200*(Player.MP/Player.startMP)),50))
        #NEED COMMENTS HERE
        win.blit((font.render(str(Player.HP), True, (255,255,255))), textRectHP)
        win.blit((font.render(str(Player.MP), True, (255,255,255))), textRectMana)
        #Load the attack menu + hover effects
        #not sure why it has to be here, tried a couple places, but this place is the only way i can get the hover to work
        if mousePos[0] in range(530, 630) and mousePos[1] in range(410, 490) and canAttack and not runAnimation:
            win.blit(fireHover, (530, 350))
        elif mousePos[0] in range(530, 630) and mousePos[1] in range(500, 560) and canAttack and not runAnimation:
            win.blit(lightHover, (530, 350))
        elif mousePos[0] in range(530, 630) and mousePos[1] in range(350, 400) and canAttack and not runAnimation:
            win.blit(atkHover, (530, 350))
        elif not runAnimation and canAttack:
            win.blit(attackMenu, (530, 350))


        #Below is code for the Monster's HP bar
        textRectHPMonster = (font.render(str(Monster.HP), True, (255,255,255))).get_rect()
        textRectHPMonster.center = (920,260)
        hpBarMonster = pygame.draw.rect(win, (0,128,0), (820,250,(200*(Monster.HP/Monster.startHP)),50))
        win.blit((font.render(str(Monster.HP), True, (255,255,255))), textRectHPMonster)
        #Monster.HP -= FireballClass.dealDamage(2,1,10,0,0)
        #If statement to control the flow of the turn based combat
        #making monster stand still when it's players turn to attack
        if canAttack:
            win.blit(Monster.image,(Monster.x,Monster.y))
        else:
            #Getting feedback from our moveAnimation either "end" or "attack" depending on which value or monster.x has
            state = Monster.moveAnimation(20,0,Monster.startingPosition)
            if state == "end":
                canAttack = True
                textRectDMG = (BigFont.render(str(DMG), True, (255,0,0))).get_rect()
                textRectDMG.center = (250,200)
                win.blit((BigFont.render(str(DMG), True, (255,0,0))), textRectDMG)
                win.blit(Monster.image,(Monster.x,Monster.y))
                pygame.display.update()
                pygame.time.delay(500)
            elif state == "attack":
                DMG = Monster.dealDamage(weapon["armor"])
                Player.HP -= DMG
                if Player.HP <= 0:
                    Player.HP = 0
                    pygame.time.delay(1000)
                    win.blit(uDed,(0,0))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    Player.HP = Player.startHP
                    Player.MP = Player.startMP
                    scene = "town"
            #Renders the monster's image according to the assigned x- and y values
            win.blit(Monster.image,(Monster.x,Monster.y))
    # If you have queued an attack, this becomes True, and executes
        if runAnimation and not spellVariable.checkMana() == "noMana":
            #Since you have asked to run the animation, it will now show the image for the spell queued
            win.blit(spellVariable.image,(spellVariable.x,spellVariable.y))
            #Moves the animation and checks if it has reached its maximum position based on the return function
            runAnimation = spellVariable.moveAnimation()
            #If it has reached its max position, it becomes false, and the if-sentence below is therefore true
            if not runAnimation:
                #After it finishes, it deals damage to the mob
                if not spellVariable.checkMana() == "noMana":
                    #Makes so you cannot attack again, and so the mob attacks
                    canAttack = False
                    # Calculates the damage you are doing to the monster
                    DMG = spellVariable.dealDamage(weapon["critChance"],0,weapon["spellPower"], weapon["attack"])
                    # Extracts the damage you dealt from the monster's HP
                    Monster.HP -= DMG
                #Resets the spells x and y coordinates
                    spellVariable.resetXY()
                    textRectDMG = (BigFont.render(str(DMG), True, (255,0,0))).get_rect()
                    textRectDMG.center = (890,200)
                    win.blit((BigFont.render(str(DMG), True, (255,0,0))), textRectDMG)
                    pygame.display.update()
                    pygame.time.delay(500)
                #Checks if you have killed the monster, if you have, it executes
                    if Monster.HP <= 0:
                # Monster's HP is set to 0, since it otherwise could be in minus
                        Monster.HP = 0
                # Updates the HP bar
                        pygame.display.update()
                # Lets you watch the dead mob for a while
                        pygame.time.delay(1000)
                # CHECK STRING ---- SKAL SLETTES !!!! ---- men et tjek for hvor meget guld du har før og efter mobbet dropper guld
                        print(str(Player.gold))
                # Rewards the player with some gold drop after the mob dies
                        Player.gold += Monster.goldDrop
                        print(str(Player.gold))
                        Player.HP = Player.startHP
                        Player.MP = Player.startMP
                        if Player.reachedLevel < monsterLevel + 1:
                            Player.reachedLevel = monsterLevel + 1
                        print("Monster Level:", str(Player.reachedLevel))
                # Changes the scene back to town
                        if Player.reachedLevel == 11:
                            townLoop = True
                            while townLoop:
                                pygame.display.update()
                                pygame.time.delay(20)
                                mouseL = pygame.mouse.get_pos()
                                win.blit(winnerbg,(0,0))
                                if mouseL[0] in range(100,250) and mouseL[1] in range(400,440):
                                    win.blit(hoverContinueButton,(100,400))
                                else:
                                    win.blit(continueButton,(100,400))
                                if mouseL[0] in range(800,950) and mouseL[1] in range(400,440):
                                    win.blit(hoverResetSlotButton,(800,400))
                                else:
                                    win.blit(resetSlotButton,(800,400))
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        run = False
                                        scene = "exit"
                                if event.type == pygame.MOUSEBUTTONUP:
                                    if mouseL[0] in range(100,250) and mouseL[1] in range(400,440):
                                        townLoop = False
                                    elif mouseL[0] in range(800,950) and mouseL[1] in range(400,440):
                                        Player = PlayerClass(wizard, 70,300,100,100,["woodenStick"],"woodenStick",0,1)
                                        townLoop = False
                                    else:
                                        continue

                        scene = "town"

#Quits the window, after the loop ends
pygame.quit()