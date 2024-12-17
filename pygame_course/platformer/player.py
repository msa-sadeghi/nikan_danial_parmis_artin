from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, x,y) -> None:
        self.images = []
        self.health = 100
        self.max_health = 100
        self.alive = True
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            img_w = img.get_width()
            img_h = img.get_height()
            img = pygame.transform.scale(img, (img_w* 0.5, img_h * 0.5))
            self.images.append(img)
        self.image = self.images[0]
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.image_number = 0
        self.last_update_time = 0
        self.direction = 1
        self.idling = True
        self.flip = False #1
        self.vel_y = 0
    def draw(self, screen):
        self.image = pygame.transform.flip(self.image, self.flip, False) #2
        screen.blit(self.image, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.rect.y += 5
        elif keys[pygame.K_LEFT]:
            self.flip = True#3
            self.rect.x -= 5
            self.direction = -1
            self.idling = False
        elif keys[pygame.K_RIGHT]:
            self.flip = False#4
            self.rect.x += 5
            self.direction = 1
            self.idling = False
        elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idling = True  
        
    
    def gravity(self):
        dy = 0
        self.vel_y += 1
        dy += self.vel_y
        self.rect.y  += dy
        
    
                
    def animation(self):
        self.image = self.images[self.image_number]
        if pygame.time.get_ticks() - self.last_update_time > 100:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images):
                self.image_number = 0
        if self.idling == True:
            self.image_number = 0
        
        
            
            
            
        