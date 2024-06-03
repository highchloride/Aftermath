import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, blocks):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/player.png').convert_alpha()
        self.image.set_colorkey(BLACK)
        # .convert_alpha allows for transparency around you character
        self.velocity = [0, 0]
        self._position = [0, 0]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * .5, 8)
        #self.moving = False
        self.x_change = 0
        self.y_change = 0
        #self.layer = PLAYER_LAYER
        self.blocks = blocks

    def position(self):
        return list(self._position)

    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        # self._old_position = self._position[:]
        # self._position[0] += self.velocity[0] * dt
        # self._position[1] += self.velocity[1] * dt
        # self.rect.topleft = self._position
        # self.feet.midbottom = self.rect.midbottom
        
        # if self._old_position[0] != None:
        #     if(self._old_position[0] - self._position[0] != 0):
        #         self.moving = True
        #     else:
        #         self.moving = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
        
        #hits = pygame.sprite.spritecollide(self, self.blocks, False)
        #for block in self.blocks:
            hits = self.rect.collidelist(self.blocks)   
            if hits:
                print(self.rect.center)
                #print(block.center)

    def move_back(self, dt):
        """ If called after an update, the sprite can move back to give the
            illusion of the sprite not moving.
        """
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom
