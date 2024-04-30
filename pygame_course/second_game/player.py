from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.idle_images  = []
        self.run_images  = []
        
        for i in range(5):
            img = pygame.image.load(f"player/Idle/{i}.png")
            img = pygame.transform.scale(img, (96,96))
            self.idle_images.append(img)
        
        for i in range(6):
            img = pygame.image.load(f"player/Run/{i}.png")
            img = pygame.transform.scale(img, (96,96))
            self.run_images.append(img)
        self.image = self.idle_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.image_number = 0
        self.update_time = pygame.time.get_ticks()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def animation(self):
        self.image = self.run_images[self.image_number]
        if pygame.time.get_ticks() - self.update_time > 200:
            self.update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.run_images):
                self.image_number = 0
            
            
        
