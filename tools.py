from PIL import Image, ImageFilter
import pygame
from config import *

class ImageTool:
    def __init__(self):
        pass

    #incoming(pygame.Surface)->pygame string->PIL image->Blur->PIL bytes->Pygame surface->Return
    def SimpleBlur(incoming: pygame.Surface):
        image = pygame.image.tostring(incoming, "RGBA", False)
        image = Image.frombytes("RGBA", (SCREEN_WIDTH, SCREEN_HEIGHT), image)
        blurred = image.filter(ImageFilter.BLUR())
        blurred = image.filter(ImageFilter.BLUR())
        image = blurred.tobytes()
        image = pygame.image.frombytes(image, (SCREEN_WIDTH, SCREEN_HEIGHT), "RGBA")
        return image
    
