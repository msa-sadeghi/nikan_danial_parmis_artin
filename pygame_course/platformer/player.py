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
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
            
            
        