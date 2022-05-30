import pygame, random
from pygame.locals import *

class Cat(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.images = [
            pygame.image.load("images/cat1.png"),
        ]

        for i in range(len(self.images)):
            img = self.images[i]
            self.images[i] = pygame.transform.rotate(img,-90)

        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speed = [0,2]
        self.reset_position()

    def reset_position(self):
        self.rect.bottom = 0
        self.rect.left = random.randint(0, 500 - self.rect.width)

    def update(self):
        self.frame = pygame.time.get_ticks() // 60 % len(self.images)
        self.image = self.images[self.frame]

        self.rect.move_ip(self.speed)
        if self.rect.top > 500:
            self.reset_position()

    def draw(self,screen):
        screen.blit(self.image,self.rect)

