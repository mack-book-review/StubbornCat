import pygame
from pygame.locals import *

class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load("images/mouse_normal.png"),
            pygame.image.load("images/mouse2.png"),
            pygame.image.load("images/mouse3.png"),
            pygame.image.load("images/mouse4.png"),
            pygame.image.load("images/mouse5.png"),
            pygame.image.load("images/mouse6.png")
        ]

        for i in range(len(self.images)):
            img = self.images[i]
            self.images[i] = pygame.transform.rotate(img,90)

        self.dead_image = pygame.transform.rotate(pygame.image.load("images/red mouse.png"),90)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.mouse_pos = (0,0)
        self.is_dead = False

    def die(self):
        self.is_dead = True

    def reset(self):
        self.is_dead = False
        self.frame = 0
        self.image = self.images[self.frame]


    def update(self):
        if not self.is_dead:
            self.frame = pygame.time.get_ticks()//60 % len(self.images)
            self.image = self.images[self.frame]

            self.rect.center = pygame.mouse.get_pos()
        else:
            self.image = self.dead_image

    def draw(self,screen):
        screen.blit(self.image,self.rect)