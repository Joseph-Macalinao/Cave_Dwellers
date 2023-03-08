import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
import tkinter # use to get height and width of screen to make correct window size

from userCreation import userCreation
from character_create import createCharacter

INFO = tkinter.Tk()
WIDTH = INFO.winfo_screenwidth() 
HEIGHT = INFO.winfo_screenheight() - 60

GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def createSurfaceWithText (text, fontSize, textColor, backgroundColor = None): # makes textbox
    font = pygame.freetype.SysFont("Arial", fontSize, bold = True)
    surface, _ = font.render(text = text, fgcolor = textColor, bgcolor = backgroundColor)
    return surface.convert_alpha()


class UIText(Sprite): # makes text that can't be interacted with
    def __init__ (self, center, text, fontSize, textColor):
        
        super().__init__()

        defaultImage = createSurfaceWithText(text, fontSize, textColor)

        self.image = defaultImage
        self.rect = defaultImage.get_rect(center = center)


    def draw(self, surface):
        surface.blit(self.image, self.rect)


class UIImage(Sprite): # makes image
    def __init__(self, data, loc) -> None:

        super().__init__()

        self.data = data
        self.location = loc        


class UIElement(Sprite): # makes an interactive button that contains text

    def __init__ (self, center, text, fontSize, textColor, action = None):
        
        super().__init__()

        self.mouseOver = False

        defaultImage = createSurfaceWithText(text, fontSize, textColor)

        hoverImage = createSurfaceWithText(text, fontSize * 1.2, textColor)

        self.images = [defaultImage, hoverImage]
        self.rects = [defaultImage.get_rect(center = center), hoverImage.get_rect(center = center)]

        self.action = action

    
    @property
    def image(self):
        if self.mouseOver:
            return self.images[1]
        else:
            return self.images[0]

    @property
    def rect(self):
        if self.mouseOver:
            return self.rects[1]
        else:
            return self.rects[0]


    def update(self, mousePos, mouseUp):
        if self.rect.collidepoint(mousePos):
            self.mouseOver = True
            if mouseUp:
                return self.action
        else:
            self.mouseOver = False


    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameState(Enum): # enum of game states
    QUIT = -1
    TITLE = 0
    CHARCREATE = 1
    CHOOSECLASS = 2
    WARRIOR = 3
    WIZARD = 4
    PALDIN = 5
    BERSERK = 6
    SHOP = 7
    CAMP = 8
    

def gameLoop(screen, buttons, backgroundImg, otherImgs = None): # game loop: pretty self expanatory

    while True:

        mouseUp = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseUp = True

            if event.type == pygame.QUIT:
                pygame.quit()
       
        img = pygame.transform.scale(backgroundImg, (WIDTH, HEIGHT))
        screen.blit(img, img.get_rect())

        for button in buttons:
            uiAction = button.update(pygame.mouse.get_pos(), mouseUp)
            if uiAction is not None:
                return uiAction
            
        buttons.draw(screen)

        if otherImgs != None:
            for image in otherImgs:
                screen.blit(image.data, image.location)


        pygame.display.flip()



def titleScreen(screen): # title screen contents

    startButton = UIElement ( #start button
        center=(WIDTH / 2, HEIGHT / 2),
        fontSize=30,
        textColor=WHITE,
        text="> Begin Journey",
        action=GameState.CHARCREATE
    )

    quitButton = UIElement ( #quit button
        center=(50, HEIGHT - 50),
        fontSize=30,
        textColor=WHITE,
        text="> Quit",
        action=GameState.QUIT
    )


    titleText = UIText (
        center=(WIDTH/2, HEIGHT/2 - 175),
        fontSize=60,
        textColor=WHITE,
        text="Cave Dwellers"
    )

    UI = RenderUpdates(startButton, quitButton, titleText)

    backgroundImg = pygame.image.load("./TitleImage.xcf")

    return gameLoop(screen, UI, backgroundImg)


def charCreate(screen): #in-game screen contents
    menuButton = UIElement (
        center=(50, HEIGHT - 50),
        fontSize=20,
        textColor=WHITE,
        text="> Menu",
        action=GameState.TITLE
    )

    createCharText = UIText (
        center=(WIDTH/2, 100),
        fontSize=60,
        textColor=WHITE,
        text="Create Character"
    )

    continueButton = UIElement (
        center=(WIDTH/2, 250),
        fontSize=35,
        textColor=WHITE,
        text="Continue",
        action=GameState.CHOOSECLASS
    )

    UI = RenderUpdates(menuButton, createCharText, continueButton)

    backgroundImg = pygame.image.load("./TitleImage.xcf")

    return gameLoop(screen, UI, backgroundImg)


def chooseClass(screen): #in-game screen contents
    menuButton = UIElement (
        center=(50, HEIGHT - 50),
        fontSize=20,
        textColor=WHITE,
        text="> Menu",
        action=GameState.TITLE
    )

    chooseClassText = UIText (
        center=(WIDTH/2, 100),
        fontSize=60,
        textColor=WHITE,
        text="Choose Class"
    )

    warriorButton = UIElement (
        center=(WIDTH/2, 200),
        fontSize=20,
        textColor=WHITE,
        text="> Warrior",
        action=GameState.WARRIOR
    )


    wizardButton = UIElement (
        center=(WIDTH/2, 300),
        fontSize=20,
        textColor=WHITE,
        text="> Wizard",
        action=GameState.WIZARD
    )

    paladinButton = UIElement (
        center=(WIDTH/2, 400),
        fontSize=20,
        textColor=WHITE,
        text="> Paladin",
        action=GameState.PALDIN
    )

    berserkButton = UIElement (
        center=(WIDTH/2, 500),
        fontSize=20,
        textColor=WHITE,
        text="> Berserk",
        action=GameState.BERSERK
    )

    warriorImg = UIImage(WARRIOR, (WIDTH/2 + 50, 150)) # load image WARRIOR in main
    wizardImg = UIImage(WIZARD, (WIDTH/2 + 50, 250))
    paladinImg = UIImage(PALADIN, (WIDTH/2 + 50, 350))
    berserkImg = UIImage(BERSERK, (WIDTH/2 + 50, 450))

    imgs = []
    imgs.append(warriorImg)
    imgs.append(wizardImg)
    imgs.append(paladinImg)
    imgs.append(berserkImg)

    UI = RenderUpdates(menuButton, chooseClassText, warriorButton, wizardButton, paladinButton, berserkButton)

    backgroundImg = pygame.image.load("./TitleImage.xcf")

    return gameLoop(screen, UI, backgroundImg, otherImgs=imgs)


def inGameMenu(screen):
    menuButton = UIElement (
        center=(50, HEIGHT - 50),
        fontSize=20,
        textColor=WHITE,
        text="> Menu",
        action=GameState.TITLE
    )

    titleText = UIText (
        center=(WIDTH/2, 100),
        fontSize=60,
        textColor=WHITE,
        text="Camp"
    )

    fightButton = UIElement (
        center=(WIDTH/2, 200),
        fontSize=20,
        textColor=WHITE,
        text="> Fight",
        #action=GameState.FIGHT
    )

    shopButton = UIElement (
        center=(WIDTH/2, 300),
        fontSize=20,
        textColor=WHITE,
        text="> Shop",
        action=GameState.SHOP
    )

    charInfoTxt = UIText (
        center=(WIDTH-250, 300),
        fontSize=25,
        textColor=WHITE,
        text=f"You currently have {CHARACTER.hp} hp and {CHARACTER.gold} gold",
    )

    charImg = UIImage(pygame.transform.rotozoom(CHARACTER.image, 0, 4), (400, HEIGHT - 400))

    imgs = []
    imgs.append(charImg)

    UI = RenderUpdates(menuButton, titleText, fightButton, shopButton, charInfoTxt)

    backgroundImg = pygame.image.load("camp.xcf")

    return gameLoop(screen, UI, backgroundImg, otherImgs=imgs)


def shopMenu(screen):
    backButton = UIElement (
        center=(75, HEIGHT - 50),
        fontSize=20,
        textColor=WHITE,
        text="> Back to camp",
        action=GameState.CAMP
    )

    titleText = UIText (
        center=(WIDTH/2, 100),
        fontSize=60,
        textColor=WHITE,
        text="Shop"
    )

    charInfoTxt = UIText (
        center=(WIDTH-250, 300),
        fontSize=25,
        textColor=WHITE,
        text=f"You currently have {CHARACTER.hp} hp and {CHARACTER.gold} gold",
    )

    charImg = UIImage(pygame.transform.rotozoom(CHARACTER.image, 0, 4), (400, HEIGHT - 400))

    imgs = []
    imgs.append(charImg)

    UI = RenderUpdates(backButton, titleText, charInfoTxt)

    backgroundImg = pygame.image.load("shop.xcf")

    return gameLoop(screen, UI, backgroundImg, otherImgs=imgs)

if __name__ == "__main__":
    pygame.init() #initialize pygame

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Cave Dwellers")

    WARRIOR = pygame.image.load("warrior.xcf").convert_alpha()
    WIZARD = pygame.image.load("wizard.xcf").convert_alpha()
    PALADIN = pygame.image.load("paladin.xcf").convert_alpha()
    BERSERK = pygame.image.load("berserk.xcf").convert_alpha()

    gameState = GameState.TITLE

    while True:
        if gameState == GameState.TITLE:
            gameState = titleScreen(screen)

        if gameState == GameState.CHARCREATE:
            gameState = charCreate(screen)

        if gameState == GameState.CHOOSECLASS:
            gameState = chooseClass(screen)

        if gameState == GameState.WARRIOR:
            #CHARACTER = userCreation("warrior")
            CHARACTER = createCharacter("warrior")
            CHARACTER.image = WARRIOR
            gameState = inGameMenu(screen)

        if gameState == GameState.WIZARD:
            #CHARACTER = userCreation("wizard")
            CHARACTER = createCharacter("wizard")
            CHARACTER.image = WIZARD
            gameState = inGameMenu(screen)

        if gameState == GameState.PALDIN:
            #CHARACTER = userCreation("paladin")
            CHARACTER = createCharacter("paladin")
            CHARACTER.image = PALADIN
            gameState = inGameMenu(screen)

        if gameState == GameState.BERSERK:
            #CHARACTER = userCreation("berserk")
            CHARACTER = createCharacter("berserk")
            CHARACTER.image = BERSERK
            gameState = inGameMenu(screen)

        if gameState == GameState.CAMP:
            gameState = inGameMenu(screen)

        if gameState == GameState.SHOP:
            gameState = shopMenu(screen)

        if gameState == GameState.QUIT:
            pygame.quit()
            break


