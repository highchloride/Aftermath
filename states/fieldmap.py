#This draws the active map. Player, enemies, and collision blocks are all in the sprites.py file.
from pytmx.util_pygame import load_pygame
import pygame
import pytmx
from sprites import *
from config import *
from states.escmenu import EscMenu
from tools import Tool
from gui.menus import *
from gui.buttons import *
from gamestatemanager import GameState

class FieldMap(GameState):
    def __init__(self, game, screen):
        super().__init__()
        self.screen = screen
        self.game = game
        
        #create spritegroups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()
        self.borders = pygame.sprite.LayeredUpdates()
        #self.attacks = pygame.sprite.LayeredUpdates()
        
        #load spritesheets
        self.character_spritesheet = Spritesheet('img/player.png')
        #self.character_spritesheet = Spritesheet('img/player_stroke.png')
        self.tilemap_spritesheet = Spritesheet('img/WL_Master_Tileset.png')
        self.enemy_spritesheet = Spritesheet('img/actors.png')
        
        self.createUI()
        self.createConsole()
        self.createMap()  
                    
        #Create player
        #Start pos
        playerx = 20
        playery = 10
        self.player = Player(self.game, self, playerx, playery)

        #Audio player
        #pygame.mixer.music.load(MID_TOWN)
        #pygame.mixer.music.play()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.next_state = EscMenu(self.game, self.screen, self.image)
        return super().handle_events(events)

    def update(self):
        pass
               
    def draw(self, screen):
        #Renders the active map
        self.screen.fill(BLACK)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)
        
        self.updateUI()
        self.updateWeather()
        self.updateConsole()

        #Takes the screenshot for the menu background
        self.image = Tool.SimpleBlur(self.screen)

    def createUI(self):
        #Frame and buttons (there's probably a better way to do some of this)
        self.bot_bkg = Menu(0,600,SCREEN_WIDTH,120,DARKGREY,DARKGREY)
        self.top_bkg = Menu(0,0,SCREEN_WIDTH,40,DARKGREY,DARKGREY)
        self.left_bkg = Menu(0,40,20,560,DARKGREY,DARKGREY)
        self.right_bkg = Menu(1260,40,20,560,DARKGREY,DARKGREY)
        self.bot_btn1 = Button(21,650,180,60,WHITE,GREY,"ROSTER",FNT_TXT2,24)
        self.bot_btn2 = Button(216,650,180,60,WHITE,GREY,"GEAR",FNT_TXT2,24)
        self.bot_btn3 = Button(411,650,180,60,WHITE,GREY,"RADIO",FNT_TXT2,24)
        self.bot_btn4 = Button(606,650,180,60,WHITE,GREY,"USE",FNT_TXT2,24)
        self.bot_btn5 = Button(801,650,180,60,WHITE,GREY,"MENU",FNT_TXT2,24)
        
        #Weather module
        self.weather_bkg = Menu(994,614,253,93,BLACK,BLACK)
        self.weather_fg = Menu(998,618,246,86,BLUE,BLUE)
        self.weather_bolt1 = Menu(1242,702,5,5,GREY,GREY)
        self.weather_bolt2 = Menu(1242,616,5,5,GREY,GREY)
        self.weather_bolt3 = Menu(996,702,5,5,GREY,GREY)
        self.weather_bolt4 = Menu(996,616,5,5,GREY,GREY)
        self.weather_title = Menu(1100,610,43,9,BLACK,GREY,"WEATHER",FNT_TXT2,9)
    
    def updateUI(self):
        #UI Frame
        self.screen.blit(self.bot_bkg.image, self.bot_bkg.rect)
        self.screen.blit(self.top_bkg.image, self.top_bkg.rect)
        self.screen.blit(self.left_bkg.image, self.left_bkg.rect)
        self.screen.blit(self.right_bkg.image, self.right_bkg.rect)
        #UI Buttons
        self.screen.blit(self.bot_btn1.image, self.bot_btn1.rect)
        self.screen.blit(self.bot_btn2.image, self.bot_btn2.rect)
        self.screen.blit(self.bot_btn3.image, self.bot_btn3.rect)
        self.screen.blit(self.bot_btn4.image, self.bot_btn4.rect)
        self.screen.blit(self.bot_btn5.image, self.bot_btn5.rect)
    
    def updateWeather(self):
        #UI Weather Module
        self.screen.blit(self.weather_bkg.image, self.weather_bkg.rect)
        self.screen.blit(self.weather_fg.image, self.weather_fg.rect)
        self.screen.blit(self.weather_bolt1.image, self.weather_bolt1.rect)
        self.screen.blit(self.weather_bolt2.image, self.weather_bolt2.rect)
        self.screen.blit(self.weather_bolt3.image, self.weather_bolt3.rect)
        self.screen.blit(self.weather_bolt4.image, self.weather_bolt4.rect)
        self.screen.blit(self.weather_title.image, self.weather_title.rect)
    
    def createConsole(self):
        #Console
        self.txt_console = Menu(22,572,957,69,BLACK,BLACK)
    
    def updateConsole(self):
        #UI Console Output
        self.screen.blit(self.txt_console.image, self.txt_console.rect)
        
    def createMap(self):
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
                    elif layer.name == 'wall' or 'wall' in layer.name:
                        Block(self, x, y, tile)
                    elif layer.name == 'door' or 'door' in layer.name:
                        Door(self, x, y, tile)  
                        
                    if x == 20 or y == 15:
                        Border(self, x, y)
                    if (self.gameMap.width - x) == 20 or (self.gameMap.height - y) == 15:
                        Border(self, x, y)
                    
        Utility.moveMap(self,21,16)                     
                        