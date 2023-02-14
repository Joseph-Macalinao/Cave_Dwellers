import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
from pygame.sprite import RenderUpdates
import tkinter # use to get height and width of screen to make correct window size


INFO = tkinter.Tk()
WIDTH = INFO.winfo_screenwidth() 
HEIGHT = INFO.winfo_screenheight()

GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def createSurfaceWithText (text, fontSize, textColor, backgroundColor): # makes textbox
    font = pygame.freetype.SysFont("Arial", fontSize, bold = True)
    surface, _ = font.render(text = text, fgcolor = textColor, bgcolor= backgroundColor)
    return surface.convert_alpha()

class Player: #player class to keep track of stats !!might not need when combine with other code
    def __init__(self, gold = 0, health = 10, level = 1):
        self.gold = gold
        self.health = health
        self.level = level


class UIElement(Sprite): # makes textbox an interactive button

    def __init__ (self, center, text, fontSize, textColor, backgroundColor, action = None):
        
        super().__init__()

        self.mouseOver = False

        defaultImage = createSurfaceWithText(text, fontSize, textColor, backgroundColor)

        hoverImage = createSurfaceWithText(text, fontSize * 1.2, textColor, backgroundColor)

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
    NEWGAME = 1
    NEXTLEVEL = 2


def gameLoop(screen, buttons): # game loop: pretty self expanatory

    while True:
        mouseUp = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseUp = True

            if event.type == pygame.QUIT:
                pygame.quit()
        
        screen.fill(BLACK)

        for button in buttons:
            uiAction = button.update(pygame.mouse.get_pos(), mouseUp)
            if uiAction is not None:
                return uiAction
            
        buttons.draw(screen)

        pygame.display.flip()


def titleScreen(screen): # title screen contents

    startButton = UIElement ( #start button
        center=(500, 500),
        fontSize=30,
        backgroundColor=GREEN,
        textColor=WHITE,
        text="Begin Journey",
        action=GameState.NEWGAME
    )

    quitButton = UIElement ( #quit button
        center=(HEIGHT/2, WIDTH/2),
        fontSize=30,
        backgroundColor=GREEN,
        textColor=WHITE,
        text="Quit",
        action=GameState.QUIT
    )

    buttons = RenderUpdates(startButton, quitButton)

    return gameLoop(screen, buttons)


def playLevel(screen): #in-game screen contents
    menuButton = UIElement (
        center=(100,550),
        fontSize=20,
        backgroundColor=GREEN,
        textColor=WHITE,
        text="Menu",
        action=GameState.TITLE
    )

    buttons = RenderUpdates(menuButton)

    return gameLoop(screen, buttons)


if __name__ == "__main__":
    pygame.init() #initialize pygame

    screen = pygame.display.set_mode([WIDTH, HEIGHT-60])
    pygame.display.set_caption("Cave Dwellers")

    gameState = GameState.TITLE

    while True:
        if gameState == GameState.TITLE:
            gameState = titleScreen(screen)

        if gameState == GameState.NEWGAME:
            player = Player()
            gameState = playLevel(screen)

        if gameState == GameState.NEXTLEVEL:
            player.level += 1
            gameState = playLevel(screen)

        if gameState == GameState.QUIT:
            pygame.quit()
            break


