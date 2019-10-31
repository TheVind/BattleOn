import pygame
import random

#Initiate Pygame and fonts (text to screen)
pygame.init()
pygame.font.init()

#Sets a font, to use for damage text
DMGFont = pygame.font.Font('freesansbold.ttf', 40)

#Import images
sumfin = pygame.image.load("")

playerDict = {
    "healthpoints": 100,
    "manapoints": 100,
    "weapons": [woodenStick],
    "gold": 0
    #"xp": 0
}
class PlayerClass:
    def __init__(self, image=wizard, x=300, y=300):
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
    def __init__(self, image, x=600, y=300, maxX = 440, startingPos=600):
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
    def __init__(self, x=0, y=0, HP=100, mana=100, image=image):
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
woodenStick = {
    "spellDMG": 5,
    "critChance": 10,
    "attack": 5,
    "spellPower": 0,
    "armor": 0,
}
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
startOfGame = True

#Sets run to True, so the eternity loop, which Pygame is, can run as long as you want.
run = True
while run:
#Gets the value of the keys pressed
    keys = pygame.key.get_pressed()
    #Thoughts on how to load game upon pressing "start"
    while startOfGame:
        pygame.display.update()
        pygame.time.delay(20)
        slot1Handler = open("slot1.txt", "r")
        slot2Handler = open("slot2.txt", "r")
        slot3Handler = open("slot3.txt", "r")

#Renders the image
    pygame.display.update()
    pygame.time.delay(20)
    

    