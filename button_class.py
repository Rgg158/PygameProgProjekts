import pygame
import sys 

lastbutton = "ediens1"

class button():
    def __init__(self, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.clicked = False

    def draw(self, x, y, surface):
        self.rect.topleft = (x, y)
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                lastbutton = self
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        if action == False:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        return action