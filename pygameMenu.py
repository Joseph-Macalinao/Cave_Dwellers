import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
import tkinter # use to get height and width of screen to make correct window size


INFO = tkinter.Tk()
WIDTH = INFO.winfo_screenwidth() 
HEIGHT = INFO.winfo_screenheight() - 60

GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def createSurfaceWithText (text, fontSize, textColor): # makes textbox
    font = pygame.freetype.SysFont("Arial", fontSize, bold = True)
    surface, _ = font.render(text = text, fgcolor = textColor, bgcolor= None)
    return surface.convert_alpha()

class Player: #player class to keep track of stats !!might not need when combine with other code
    def __init__(self, gold = 0, health = 10, level = 1):
        self.gold = gold
        self.health = health
        self.level = level


class UIText(Sprite): # makes text that can't be interacted with
    def __init__ (self, center, text, fontSize, textColor):
        
        super().__init__()

        defaultImage = createSurfaceWithText(text, fontSize, textColor)

        self.image = defaultImage
        self.rect = defaultImage.get_rect(center = center)


    def draw(self, surface):
        surface.blit(self.image, self.rect)




class UIElement(Sprite): # makes textbox an interactive button

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
    CREATECHARACTER = 1
    CHOOSECLASS = 2
    


def gameLoop(screen, buttons, backgroundImg): # game loop: pretty self expanatory

    while True:
        mouseUp = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseUp = True

            if event.type == pygame.QUIT:
                pygame.quit()
        
        # screen.fill(GREEN)
        img = pygame.transform.scale(backgroundImg, (WIDTH, HEIGHT))
        screen.blit(img, img.get_rect())

        for button in buttons:
            uiAction = button.update(pygame.mouse.get_pos(), mouseUp)
            if uiAction is not None:
                return uiAction
            
        buttons.draw(screen)

        pygame.display.flip()


def titleScreen(screen): # title screen contents

    startButton = UIElement ( #start button
        center=(WIDTH / 2, HEIGHT / 2),
        fontSize=30,
        textColor=WHITE,
        text="> Begin Journey",
        action=GameState.CREATECHARACTER
    )

    quitButton = UIElement ( #quit button
        center=(50, HEIGHT - 50),
        fontSize=30,
        textColor=WHITE,
        text="> Quit",
        action=GameState.QUIT
    )

    titleText = UIText (
        center=(WIDTH/2, HEIGHT/2 - 100),
        fontSize=60,
        textColor=WHITE,
        text="Cave Dwellers"
    )

    UI = RenderUpdates(startButton, quitButton, titleText)

    backgroundImg = pygame.image.load("./TitleImage.xcf")

    return gameLoop(screen, UI, backgroundImg)


def createCharacter(screen): #in-game screen contents
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

    UI = RenderUpdates(menuButton, createCharText)

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

    UI = RenderUpdates(menuButton, chooseClassText)

    backgroundImg = pygame.image.load("./TitleImage.xcf")

    return gameLoop(screen, UI, backgroundImg)


if __name__ == "__main__":
    pygame.init() #initialize pygame

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Cave Dwellers")

    gameState = GameState.TITLE

    while True:
        if gameState == GameState.TITLE:
            gameState = titleScreen(screen)

        if gameState == GameState.CREATECHARACTER:
            player = Player()
            gameState = createCharacter(screen)

        if gameState == GameState.CHOOSECLASS:
            gameState = chooseClass(screen)

        if gameState == GameState.QUIT:
            pygame.quit()
            break


