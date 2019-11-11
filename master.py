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
    "name": "woodenStick",
    "spellDMG": 5,
    "critChance": 10,
    "attack": 5,
    "spellPower": 0,
    "armor": 0,
}

broadSword = {
    "name": "broadSword",
    "spellDMG": 2,
    "critChance": 20,
    "attack": 10,
    "spellPower": 0,
    "armor": 5,
    "price": 43252
}
crystalStaff= {
    "name": "crystalStaff",
    "spellDMG": 20,
    "critChance": 10,
    "attack": 5,
    "spellPower": 10,
    "armor": 0,
    "price": 113212
}

#Import images
#imports our loading screen, kinda scuffed - needs to be changed
loading = pygame.image.load("loadingScreen.jpg")
#Town image imported
townImage = pygame.image.load("bgtownFinal.jpg")
#Button imported
scuffedButton = pygame.image.load("saveGame.png")
#Gets saving background screen
savedScreen = pygame.image.load("saveScreen.jpg")
#Gets the battle background
battlebg = pygame.image.load("forest.jpg")
#Gets scuffed button
battleButton = pygame.image.load("battleB.png")
battleButtonRed = pygame.image.load("battleBRed.png")
#Gets the wizard image
wizard = pygame.image.load("wizard.png")
zulul = pygame.image.load("ZULUL.png")
#Gets the monster
monster = pygame.image.load("monster.png")
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
#topleft small icon
pygame.display.set_icon(zulul)

#THIS SECTION NEEDS COMMENTS
class PlayerClass:

    def __init__(self, image, x=300, y=300, hp=100, mana=100, weapons=[woodenStick], equipped=woodenStick, gold=0):
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

    def addWeapon(weapon):
        self.weapons.append(weapon)

    def goldChange(changeOfGold):
        self.gold += changeOfGold

    def changeHP(HPChange):
        if HPChange == "toFull":
            self.HP = self.startHP
        else:
            self.HP += HPChange
    

#Defines the monster animation and attack
class MonsterClass:
#the init function defining all the default values when you first call it
#This functions holds all the paramteres we need the monster to have
    def __init__(self, image=loading, x=600, y=300, maxX = 440):
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



#Some players values we dont know what to do with
        #self.HP = HP
        #self.mana = mana

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
                    FileHandler = open("slot1.txt", "r")
                elif mouseL[0] in range(400,550) and mouseL[1] in range (200,350):
                    FileHandler = open("slot2.txt", "r")
                elif mouseL[0] in range(700,850) and mouseL[1] in range (200,350):
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
#Adds the values from the file (now the array), to the dictionary/class where player stats are stored.
                #Makes the "Weapon Equipped" an integer, so it is easier to work with
                #outputFromSlot[3] = int(outputFromSlot[3])
                        #First removes the "[]," from the string, and next splitting it up 
                         #outputFromSlot[2] = outputFromSlot[2].translate({ord(i):None for i in '[,]'}).split()
                # Defines an array to put the weapons you have into
                weaponArray = []
                outputFromSlot[2] = outputFromSlot[2].split()
                # Iterates over the names in the list of weapons you have, and adds them accordingly.
                #for word in outputFromSlot[2]:
                #    if word == "woodenStick" and word not in weaponArray and not word == "":
                #        weaponArray.append(woodenStick)
                #    elif word == "crystalStaff" and word not in weaponArray and not word == "":
                #        weaponArray.append(crystalStaff)
                #    elif word == "broadSword" and word not in weaponArray and not word == "":
                #        weaponArray.append(broadSword)
                for singleWeapon in outputFromSlot[2]:
                    weaponArray.append(singleWeapon)

#Sets the class of the player
                Player = PlayerClass(wizard, 70, 300, int(outputFromSlot[0]), int(outputFromSlot[1]), weaponArray, outputFromSlot[3], int(outputFromSlot[4]))
                """for vaaben in weaponArray:
                    print(vaaben)
                print(str(weaponArray))"""
                #if "woodenStick" in Player.weapons["name"]:
                    #print(weaponArray[1]["attack"])
#Changes scene to town, so the while-loop exits
                scene = "town"

    #Need something to trigger this thing, but it will write to the file selected
    while scene == "saveGame":
        pygame.display.update()
        pygame.time.delay(20)
        win.blit(savedScreen,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                scene = "exit"
#After you click, and release your finger from the left-click, do:
            if event.type == pygame.MOUSEBUTTONUP:
#Gets location of mouse - useless for now? not sure why it doesnt work
                mouseL = pygame.mouse.get_pos()
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
                FileHandler.close()
                #This is the way we change scene from loading to the town scene
                scene = "town"                   
    
    
    while scene == "town":
        pygame.time.delay(20)
        pygame.display.update()
        mouseL = pygame.mouse.get_pos()
        win.blit(townImage, (0,0))
        #pygame.draw.rect(win, (255,0,0), (50, 350, 150, 40))
        win.blit(scuffedButton, (850,350))
        win.blit(weaponButton,(300,350))
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
                    scene = "saveGame"
                elif mouseL[0] in range(50,200) and mouseL[1] in range(350,390):
                    scene = "battle"
                elif mouseL[0] in range(550,700) and mouseL[1] in range(350,390):
                    weaponLoop = True
                    while weaponLoop:
                        win.blit(townImage, (0,0))
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
                                weaponLoop = False
                            if event.type == pygame.MOUSEBUTTONUP:
                                mouseL = pygame.mouse.get_pos()
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
                                    weaponLoop = False
                #If you click inside the "Weapons" button, do:
                elif mouseL[0] in range(300,450) and mouseL[1] in range(350,390):
                    #Enters a loop, to not make it run through as few things as possible for each iteration
                    weaponLoop = True
                    while weaponLoop:
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
                                weaponLoop = False
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
                                    weaponLoop = False
                                print(Player.weaponEquipped)
                else:
                    continue

#Loads the variables before battle
    if scene == "battle":
#Loads the monster
        Monster = MonsterClass(monster, 800, 300, 440)
#Sets some variables for the fighting scene
        yourTurn = True
        canAttack = True
#Sets the weapon
        #weapon = Player.weapons[Player.weaponEquipped]
        if Player.weaponEquipped == "woodenStick":
            weapon = woodenStick
        elif Player.weaponEquipped == "crystalStaff":
            weapon = crystalStaff
        elif Player.weaponEquipped == "broadSword":
            weapon = broadSword
#Shifts to the battle scene
        scene = "battleScene"

#The battle scene! - not much going on atm tho
    while scene == "battleScene":
        pygame.time.delay(20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #run = False
                #scene = "exit"
                canAttack = False

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
        
        #If statement to control the flow of the turn based combat
        #making monster stand still when it's players turn to attack
        if canAttack:
            win.blit(Monster.image,(Monster.x,Monster.y))
        else:
            #Getting feedback from our moveAnimation either "end" or "attack" depending on which value or monster.x has
            state = Monster.moveAnimation(20,0,Monster.startingPosition)
            if state == "end":
                canAttack = True
            elif state == "attack":
                DMG = Monster.dealDamage(3,2,0,weapon["armor"])
                Player.HP -= DMG
                if Player.HP <= 0:
                    Player.HP = 0
                    pygame.time.delay(1000)
                    win.blit(uDed,(0,0))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    scene = "town"
            #Renders the monster's image according to the assigned x- and y values
            win.blit(Monster.image,(Monster.x,Monster.y))

#Quits the window, after the loop ends
pygame.quit()