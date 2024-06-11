import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('fonts/gothic821condensed.ttf', 128)
        
        self.character_spritesheet = Spritesheet('img/player.png')
        self.tilemap_spritesheet = Spritesheet('img/WL_Master_Tileset.png')
        self.enemy_spritesheet = Spritesheet('img/actors.png')
        self.intro_background = pygame.image.load('./img/introBackground.png')
        self.gameover_background = pygame.image.load('./img/introBackground.png')
        
    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    Player(self, j, i)

        
    def new(self):
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        
        #self.player = Player(self, 1, 2)
        
        self.createTilemap()
        
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        
    def update(self):
        #game loop updates
        self.all_sprites.update()
                
    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        
    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def game_over(self):
        text = self.font.render('GAME OVER', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        restart_button = Button((SCREEN_WIDTH/2) - 200, SCREEN_HEIGHT - 100, 200, 50, WHITE, BLACK, 'Restart', 32)
        quit_button = Button((SCREEN_WIDTH/2) + 200, SCREEN_HEIGHT - 100, 100, 50, WHITE, BLACK, 'Quit', 32)
        
        for sprite in self.all_sprites:
            sprite.kill()
            
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
                
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                
            self.screen.blit(self.gameover_background, (0, 0))
            self.screen.blit(text, text_rect.topleft)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
                    
        
    def intro_screen(self):
        intro = True
        
        title = self.font.render('AFTERMATH', True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH/2, 100))
        
        play_button = Button((SCREEN_WIDTH/2) - 50, SCREEN_HEIGHT - 100, 100, 50, WHITE, BLACK, 'Play', 32)
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                    
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect.topleft)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
            

    
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()