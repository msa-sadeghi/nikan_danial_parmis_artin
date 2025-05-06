from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.all_images = []
        for i in range(5):
            img = pygame.image.load(f"./Objects/Bullet/Bullet_00{i}.png")
            img = pygame.transform.scale_by(img, 0.2)
            self.all_images.append(img)

        self.custome_number = 0
        self.image = self.all_images[self.custome_number]
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        group.add(self)

    def update(self, screen):
        
        img = pygame.transform.flip(self.image, self.direction == -1, False)
        img = pygame.transform.scale_by(img, 0.5)
        self.rect.x += 5 * self.direction
        screen.blit(img, self.rect)