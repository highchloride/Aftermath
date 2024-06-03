#This draws the active map. Player, enemies, and collision blocks are all in the sprites.py file.
from pytmx.util_pygame import load_pygame
import pygame
import pytmx
from sprites import *
from config import *
from tools import ImageTool

class FieldMap:
    def __init__(self, game, screen):
        self.screen = screen
        self.game = game
        
        #create spritegroups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()
        #self.attacks = pygame.sprite.LayeredUpdates()
        
        #load spritesheets
        self.character_spritesheet = Spritesheet('img/player.png')
        #self.character_spritesheet = Spritesheet('img/player_stroke.png')
        self.tilemap_spritesheet = Spritesheet('img/WL_Master_Tileset.png')
        self.enemy_spritesheet = Spritesheet('img/actors.png')
        
        #Loads the tiled map
        self.gameMap = pytmx.load_pygame(MAP_TEST)
        #Holds a blurred screenshot of the current screen. Used for menu backgrounds.
        self.image = None
        
        #Render tilemap data to sprites
        for layer in self.gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = self.gameMap.get_tile_image_by_gid(gid)
                if tile != None:
                    if layer.name == 'ground' or 'ground' in layer.name:
                        Ground(self, x, y, tile)
                    if layer.name == 'wall' or 'wall' in layer.name:
                        Block(self, x, y, tile)
                    if layer.name == 'door' or 'door' in layer.name:
                        Door(self, x, y, tile)                                        

        playerx = 20
        playery = 10

        Player(self.game, self, playerx, playery)


        pygame.mixer.music.load(MID_TOWN)
        #pygame.mixer.music.play()
               
    def run(self):
        #Renders the active map
        self.screen.fill(BLACK)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        self.image = ImageTool.SimpleBlur(self.screen)
        