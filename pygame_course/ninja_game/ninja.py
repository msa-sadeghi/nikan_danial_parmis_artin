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
        self.direction = 1
        self.update_time = pygame.time.get_ticks()
        self.moving_state = "Idle"
        self.y_speed = 0

    def draw(self, screen):
        self.animation()
        screen.blit(
            pygame.transform.flip(self.image, self.direction == -1, False), 
            self.rect)
    def animation(self):
        if pygame.time.get_ticks() - self.update_time >= 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.images[self.anim]):
            self.frame_index = 0
        self.image = self.images[self.anim][self.frame_index]  

    def change_animation(self, anim_index):
        if anim_index != self.anim:
            self.anim = anim_index
            self.frame_index = 0

    def move(self):
        x_movement = 0  
        y_movement = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving_state = "Moving"
            self.direction = -1
            x_movement -= 5
        if keys[pygame.K_RIGHT]:
            self.moving_state = "Moving"
            self.direction = 1
            x_movement += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving_state = "Idle"

        if keys[pygame.K_UP]:
            self.y_speed = -14
        y_movement += self.y_speed
        self.y_speed += 1
        self.rect.x += x_movement
        self.rect.y += y_movement

