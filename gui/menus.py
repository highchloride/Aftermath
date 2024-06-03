import pygame

class Menu:
    def __init__(self, x, y, width, height, fgColor, bgColor, content=None, fontname=None, fontsize=None):
        if(fontname):
            self.fontname = fontname #pygame.font.Font('fonts/JH_FALLOUT.TTF', fontsize)
            self.fontsize = fontsize
            self.font = pygame.font.Font(self.fontname, self.fontsize)
        
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.fg = fgColor
        self.bg = bgColor
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        #self.text = self.font.render(self.content, False, self.fg)
        #self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        #self.image.blit(self.text, self.text_rect)
    
