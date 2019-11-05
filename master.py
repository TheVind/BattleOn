import pygame
import random

#Initiate Pygame and fonts (text to screen)
pygame.init()
pygame.font.init()
win = pygame.display.set_mode((1100, 600))

#Sets a font, to use for damage text
DMGFont = pygame.font.Font('freesansbold.ttf', 40)

woodenStick = {
    "spellDMG": 5,
    "critChance": 10,
    "attack": 5,
    "spellPower": 0,
    "armor": 0,
}

#Import images
#imports our loading screen, kinda scuffed - needs to be changed
loading = pygame.image.load("loadingScreen.jpg")
#Town image imported
townImage = pygame.image.load("bgtown.jpg")
#The player dictionary - the stats of our player + weapon and gold count.
playerDict = {
    "healthpoints": 100,
    "manapoints": 100,
    "weapons": [woodenStick],
    "equippedWeapon": woodenStick,
    "gold": 0
    #"xp": 0
}
class PlayerClass:
    def __init__(self, image, x=300, y=300):
        self.image = image
        self.x = x
        self.y = y
        self.HP = 100
        self.MP = 100
        self.weapons = [woodenStick]
        self.weaponEquipped = woodenStick
        self.gold = 0
    def addWeapon(weapon):
        self.weapons.append(weapon)
    def goldChange(changeOfGold):
        self.gold += changeOfGold
    def changeHP(HPChange):
        if HPChange == toFull:
            self.HP = 100
        else:
            self.HP += HPChange
    

#Defines the monster animation and attack
class MonsterClass:
#the init function defining all the default values when you first call it
#This functions holds all the paramteres we need the monster to have
    def __init__(self, image=loading, x=600, y=300, maxX = 440, startingPos=600):
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
        self.startingPosition = startingPos
        #The threshold to which the monster can't move anymore, so it doesnt stand on top of player
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
    #Monster dmg function to determine dmg and crit
    def dealDamage(self, dmgMulti=1, d=2, critCh=0, a=0):
        #the dmg calulation it self
        dmg = random.randint(((8-d)*dmgMulti),((8+d)*dmgMulti))
        #the calculation of the crit chance - default is set so the monster cannot crit - further explained in the spell class
        getCritChance = random.randint(1,10)
        if (critCh/10) >= getCritChance:
            dmg = dmg*2
        armorGain = (a/100)*dmg
        return int(dmg - armorGain)

#Class for the player, both dealing damage and animating
class SpellClass:
    def __init__(self, x=0, y=0, HP=100, mana=100, image=loading):
        self.x = x
        self.y = y
        #Sets the image to use for the animation
        self.image = image
    #the moving of the spell picture - animation
    def moveAnimation(self, m=200, mx=20, my=20):
        self.max = m
        self.x += mx
        self.y += my
    
    def gainMana(self, mana, gain):
        return (mana+gain)

    def dealDamage(self, dmgMulti=2, difference=1, critCh=10, a=0, sp=0):
        dmg = random.randint(((5-difference)*dmgMulti),((5+difference)*dmgMulti))
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
        #Returns the final damage value, with the amount of damage dealt minus the damage absorbed by armor
        return int(dmg - armorPrevail)

#Defines the weapons to use
broadSword = {
    "spellDMG": 2,
    "critChance": 20,
    "attack": 10,
    "spellPower": 0,
    "armor": 5
}
crystalStaff= {
    "spellDMG": 20,
    "critChance": 10,
    "attack": 5,
    "spellPower": 10,
    "armor": 0
}


#Some players values we dont know what to do with
        #self.HP = HP
        #self.mana = mana

#Sets variable to make the loop ask for a slot to load before anything else
scene = "startOfGame"

#Sets run to True, so the eternity loop, which Pygame is, can run as long as you want.
run = True
while run:
#Gets the value of the keys pressed
    keys = pygame.key.get_pressed()
#Gets the state of the mouse
    mouseC = pygame.mouse.get_pressed()
#Gets location of mouse
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
#After you click, and release your finger from the left-click, do:
            if event.type == pygame.MOUSEBUTTONUP:
#If the mouse is in this range mouseL[0] in range (X,X) and mouse[1] in range (Y,Y):
#Changed every mouseL variable to pymgae.mouse.get_pos() it worked flawlessly - Andreas
                if pygame.mouse.get_pos()[0] in range(100,250) and pygame.mouse.get_pos()[1] in range (200,350):
#If you click slot1, it will load slot1
                    FileHandler = open("slot1.txt", "r")
                elif pygame.mouse.get_pos()[0] in range(400,550) and pygame.mouse.get_pos()[1] in range (200,350):
                    FileHandler = open("slot2.txt", "r")
                elif pygame.mouse.get_pos()[0] in range(700,850) and pygame.mouse.get_pos()[1] in range (200,350):
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
                    outputFromSlot.append(line)
#Closes the filehandler, since we do not need it anymore, since we have the values in a local array
                FileHandler.close()
#Adds the values from the file (now the array), to the dictionary/class where player stats are stored.
                #player = PlayerClass(dsadsadsa)
                playerDict["healthpoints"] = outputFromSlot[0]
                playerDict["manapoints"] = outputFromSlot[1]
                playerDict["weapons"] = outputFromSlot[2]
                playerDict["equippedWeapon"] = outputFromSlot[3]
                playerDict["gold"] = outputFromSlot[4]
                print(str(playerDict["healthpoints"] + " " + playerDict["manapoints"] + " " + playerDict["weapons"] + " " + playerDict["equippedWeapon"] + " " + playerDict["gold"]))
#Changes scene, so the while-loop exits
                scene = "town"

    #Need something to trigger this thing, but it will write to the file selected
    while scene == "saveGame":
        pygame.display.update()
        pygame.time.delay(20)
        for event in pygame.event.get():
#After you click, and release your finger from the left-click, do:
            if event.type == pygame.MOUSEBUTTONUP:
#If the mouse is in this range:
                if mouseL[0] in range(100,250) and mouseL[1] in range (200,350):
#If you click slot1, it will load slot1
                    FileHandler = open("slot1.txt", "w")
                elif mouseL[0] in range(400,550) and mouseL[1] in range (200,350):
                    FileHandler = open("slot2.txt", "w")
                elif mouseL[0] in range(700,850) and mouseL[1] in range (200,350):
                    FileHandler = open("slot3.txt", "w")
#If you do not select a slot, it does nothing, and continues to the top of the loop
                else:
                    continue
                FileHandler.write(playerDict["healthpoints"])
                FileHandler.write("\n")
                FileHandler.write(playerDict["manapoints"])
                FileHandler.write("\n")
                FileHandler.write(playerDict["weapons"])
                FileHandler.write("\n") 
                FileHandler.write(playerDict["equippedWeapon"])
                FileHandler.write("\n")
                FileHandler.write(playerDict["gold"])
                FileHandler.close()
                scene = "town"                   
    
    
    while scene == "town":
        win.blit(townImage, (0,0))
        pygame.time.delay(20)
        pygame.display.update()

#Renders the image
    #pygame.display.update()
    #pygame.time.delay(20)
    

    