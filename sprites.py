import pygame
from pygame.sprite import Sprite
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Utility:
    def moveMap(fieldmap, x,y):
        for sprite in fieldmap.all_sprites:
            if x > 0:
                sprite.rect.x -= (x * TILE_SIZE)
            elif x < 0:
                sprite.rect.x += (x * TILE_SIZE)
            if y > 0:
                sprite.rect.y -= (y * TILE_SIZE)
            elif y < 0:
                sprite.rect.y += (y * TILE_SIZE)
            

class Player(pygame.sprite.Sprite):
    def __init__(self, game, fieldmap, x, y):
        
        self.game = game
        self.fieldmap = fieldmap
        self._layer = PLAYER_LAYER
        self.groups = self.fieldmap.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        #self.ignore

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        self.animation_loop = 1
                
        self.image = self.fieldmap.character_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        #Use the self.game.character_spritesheet.get_sprite() function to create a list of at least 3 sequential frames in the corresponding named variable. This will feed these frames into the animator for the Player character.
        self.down_animations = []
        self.up_animations = []
        self.left_animations = []
        self.right_animations = []
        
        # print('Player created at ' + str(self.x) + ' and ' + str(self.y))
      
    def update(self):
        self.movement()
        #self.animate() #Uncomment to use animations
        self.collide_enemy()
        self.collide_door()
        #self.collide_border()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_border('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_border('y')
        
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.fieldmap.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            for sprite in self.fieldmap.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            for sprite in self.fieldmap.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.fieldmap.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def collide_border(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.fieldmap.borders, False)
            if hits:
                print("That's beyond your range, Patrolman.")
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right 
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.fieldmap.borders, False)
            if hits:
                print("That's beyond your range, Patrolman.")
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
    
    def collide_door(self):
        hits = pygame.sprite.spritecollide(self, self.fieldmap.doors, False)
        if hits:
            print("door!")
            
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.fieldmap.enemies, False)
        if hits:
            #self.kill()
            pygame.event.post(pygame.event.Event(self.game.ON_DEATH))
            
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.fieldmap.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right 
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.fieldmap.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.fieldmap.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

    def animate(self):
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to down frame 1
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1
        
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to up frame 1
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1
        
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to left frame 1
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to right frame 0
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(1,3)

        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        #Use the self.game.enemy_spritesheet.get_sprite() function to create a list of at least 3 sequential frames in the corresponding named variable. This will feed these frames into the animator for the Enemy sprite.        
        self.down_animations = []
        self.up_animations = []
        self.left_animations = []
        self.right_animations = []
    
    def update(self):
        self.movement()
        #self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
                
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
                    
    def animate(self):        
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to down frame 1
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1
        
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to up frame 1
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1
        
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to left frame 1
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.y_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0,0,TILE_SIZE,TILE_SIZE) #equal to right frame 0
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:    #MUST EQUAL ANIMATION FRAMES
                    self.animation_loop = 1

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image):
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        #self.image = self.game.tilemap_spritesheet.get_sprite(256, 288, self.width, self.height)
        self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Border(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.borders
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        #self.image = self.game.tilemap_spritesheet.get_sprite(256, 288, self.width, self.height)
        self.image = pygame.image.load(TRANSPARENT_TILE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image):
        
        self.game = game
        self._layer = DOOR_LAYER
        self.groups = self.game.all_sprites, self.game.doors
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        #self.image = self.game.tilemap_spritesheet.get_sprite(256, 288, self.width, self.height)
        self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image):
        
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        #self.image = self.game.tilemap_spritesheet.get_sprite(32, 480, self.width, self.height)
        self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y