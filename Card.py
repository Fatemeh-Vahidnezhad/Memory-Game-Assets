#  Card Class

# This class is for keeping track of a single Card.
# The card images (card0.png through card8.png) are in the images folder.

# It should be responsible for showing the front or back of a card
# depending on the card's state.

import pygwidgets
from constants import *
import pygame
import random

class Card:
    def __init__(self, window, index, position) -> None:
        self.window = window
        backPath = 'images/cardBack.png'
        self.BACK = 'back'
        self.FRONT = 'front'
        self.path = 'images/'+'card' + str(index) + '.png'
        self.img = pygwidgets.ImageCollection(window, position, \
                                               {self.BACK:backPath, \
                                                self.FRONT: self.path},\
                                                      self.BACK)
        self.x, self.y = position
        self.width, self.height = self.img.getSize()   
        self.match = False


    def new_position(self, new_location):
        self.x, self.y = new_location
        self.img.setLoc(new_location)


    def reset(self):
        self.match = False
        self.img.replace(self.BACK)
    
    def image_matched(self):
        self.match = True
 
    def get_name(self):
        return self.path

    def hide(self):
        self.img.replace(self.BACK)

    def show(self):
        self.img.replace(self.FRONT)

    def handleInside(self, mouseloc):
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.Rect.collidepoint(mouseloc):
            if not self.match:
                self.show()
                return True

    def draw(self):
        self.img.draw()

# if __name__ == '__main__':
#     import pygame
#     import sys
        
#     # define a window:
#     Black = (0, 0, 0)
#     window_width = 1000
#     window_height = 600
#     frame_per_second = 60
#     clock = pygame.time.Clock()


#     pygame.init()
#     window = pygame.display.set_mode((window_width, window_height))
#     lst = []
#     ogame = Card(window,(100, 100))

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 # for value in self.imgs.values():
#                     ogame.handleInside(event.pos)
#                     # ogame.draw()

#         window.fill(Black)  
#         ogame.draw()  
        
#         pygame.display.update()  
#         clock.tick(frame_per_second)
