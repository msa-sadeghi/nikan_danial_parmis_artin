from pygame.sprite import Sprite
import pygame
import os
class Ninja(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.images = []
        self.all_animations = os.listdir("./ninja_images")

        for anim in self.all_animations:
            anim_list = []
            img_list = os.listdir(f"./ninja_images/{anim}")
            for img in img_list:
                im = pygame.image.load(f"./ninja_images/{anim}/{img}")
                im = pygame.transform.scale_by(im, 0.3)
                anim_list.append(im)

            self.images.append(anim_list)

        self.anim = 4
        self.frame_index = 0
        self.image = self.images[self.anim][self.frame_index]
        self.rect = self.image.get_rect(topleft= (x,y))
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass  
