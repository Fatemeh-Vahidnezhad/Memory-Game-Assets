#  Game Manager Class

#  This would be the place where all the game logic would exist.

# It would be responsible for starting a game by randomizing a list of "cards" (images)
# where there are two of each of nine different "cards"  (card0 to card9),

# This class is responsible for running the logic of the game.
# I would suggest building the game as a "state machine" with 3 states.
from Card import *
import random
import pygame


class GameMgr:
    def __init__(self, window) -> None:
        self.window = window
        self.cards = []
        # making indexs
        self.index = [i for i in range(9)]*2
        # making locations
        self.location = []
        for row in range(0,3):
            row = row * 60 + 110
            for col in range(0,6):
                col = col * 70 + 200
                self.location.append((col, row))

        # making cards
        for index, position in zip(self.index, self.location):
            oCard = Card(self.window, index, position)
            self.cards.append(oCard)
        self.reset()


    def reset(self):
        random.shuffle(self.location)
        for card, position in zip(self.cards, self.location):
            card.new_position(position)
            card.reset()


    def compare_images(self, ocard1, ocard2):
        if ocard1.get_name() == ocard2.get_name():
            ocard1.image_matched()
            ocard2.image_matched()
            return True
    
    def get(self):
        return self.cards

    def draw(self):
        for ocard in self.cards:
            ocard.draw()

# if __name__ == '__main__':
#     import pygame
#     import sys
        
#     # define a window:
#     Black = (0, 0, 0)
#     window_width = 1000
#     window_height = 600
#     frame_per_second = 30
#     clock = pygame.time.Clock()


#     pygame.init()
#     window = pygame.display.set_mode((window_width, window_height))
#     lst = []
#     ogame = GameMgr(window)
#     img = ogame.get()
   
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 for value in img:
#                     value.handleInside(event.pos)
#                     # ogame.draw()

#         window.fill(Black)  

#         ogame.draw()  
        
#         pygame.display.update() 
#         clock.tick(frame_per_second)
