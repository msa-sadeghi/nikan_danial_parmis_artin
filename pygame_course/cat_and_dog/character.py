from pygame.sprite import Sprite
import pygame
import os
class Character(Sprite):
    def __init__(self, x,y, type):
        super().__init__()
        self.type = type
        self.animation_types = os.listdir(f"{type}")
        self.all_images = {}
        for animation in self.animation_types:
            images_list = []
            images = os.listdir(f"./{type}/{animation}")
            for i in images:
                img = pygame.image.load(f"./{type}/{animation}/{i}")
                img = pygame.transform.scale_by(img, 0.5)
                images_list.append(img)
            self.all_images[animation] = images_list

        self.frame_index = 0
        self.animation = "Idle"
        self.image = self.all_images[self.animation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)




