#  Memory Game

####  This file would be the main entry point.

# It would start up the game, create a Game Manager object, and run the main loop.

# It would also check for events, and any time an event happens, it would call
# an appropriate method in the Game Manager object to handle it.

# Ideally, in the main loop, it would call an update() and draw() method in the Game Manager
# then update the window.
import pygame
import sys
from constants import *
import pygwidgets
from GameMgr import *


pygame.init()
clock = pygame.time.Clock()

class Main:
    def __init__(self) -> None:
        self.nframe = 20
        self.current_frame = 0
        self.cnt = 0 
        self.cnt_try = self.cnt // 2
        self.cnt_correct = 0
        self.lst = []
        self.window = pygame.display.set_mode((window_width, window_height))
        self.background_img = pygame.image.load('images/background.png')
        self.Num_try_text = pygwidgets.DisplayText(self.window, (337, 323), fontSize=28)
        self.score_text = pygwidgets.DisplayText(self.window, (337, 352), fontSize=28)

        self.newGameButton = pygwidgets.CustomButton(self.window, (500, 320), \
                                                            up='images/newGame.png', \
                                                            down='images/newGameDown.png',\
                                                            over='images/newGameOver.png')
        self.oGameMgr = GameMgr(self.window)
        self.card_lst = self.oGameMgr.get()
        self.sound_buzz = pygame.mixer.Sound('sounds/buzz.wav')
        self.sound_ding = pygame.mixer.Sound('sounds/ding.wav')
        self.state = W_1_SELECTION
        self.card1 = None
        self.card2 = None
 
    def run(self):  
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.newGameButton.handleEvent(event):
                    self.oGameMgr.reset()
                    self.cnt = 0
                    self.cnt_correct = 0
                    self.state = W_1_SELECTION
                    self.card1 = None
                    self.card2 = None

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == W_1_SELECTION:
                        for ocard in self.card_lst:
                            if ocard.handleInside(event.pos):
                                self.cnt += 1
                                self.card1 = ocard
                                self.state = W_2_SELECTION
                                break

                    elif self.state == W_2_SELECTION:
                        for ocard in self.card_lst:
                            if ocard.handleInside(event.pos) and ocard != self.card1:
                                self.card2 = ocard
                                # self.cnt += 1
                                if self.oGameMgr.compare_images(self.card1, self.card2):
                                    self.cnt_correct += 1
                                    self.sound_ding.play()
                                    self.card1 = None
                                    self.card2 = None
                                    self.state = W_1_SELECTION
                                else:
                                    self.state = TIMEOUT
                                    self.sound_buzz.play() 
                                break

            if self.state == TIMEOUT:
                if self.current_frame >= self.nframe:
                    self.card1.hide()
                    self.card2.hide()
                    self.card1 = None
                    self.card2 = None
                    self.state = W_1_SELECTION
                    self.current_frame = 0
                else:
                    self.current_frame += 1

            self.window.blit(self.background_img, (0, 0))
            self.oGameMgr.draw()  
            self.newGameButton.draw()
            self.score_text.setValue(self.cnt_correct)
            self.score_text.draw()
            self.Num_try_text.setValue(self.cnt)
            self.Num_try_text.draw()
            pygame.display.update()  
            clock.tick(frame_per_second)

if __name__ == '__main__':
    game = Main()
    game.run()

    