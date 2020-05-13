import assets
import variable
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['player_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = variable.RESOLUTION[0]/variable.DIVISIONS[0]
        self.rect.bottom = variable.RESOLUTION[1] - 40
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > variable.RESOLUTION[0] - variable.WIDTH_SQUARE:
            self.rect.right = variable.RESOLUTION[0] - variable.WIDTH_SQUARE
        if self.rect.left < variable.WIDTH_SQUARE:
            self.rect.left = variable.WIDTH_SQUARE
        if self.rect.top < variable.HEIGHT_SQUARE:
            self.rect.top = variable.HEIGHT_SQUARE
        if self.rect.bottom > variable.RESOLUTION[1] - variable.HEIGHT_SQUARE:
            self.rect.bottom = variable.RESOLUTION[1] -variable.HEIGHT_SQUARE

    


