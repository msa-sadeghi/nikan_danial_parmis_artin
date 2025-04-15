from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.all_images = {}
        self.animation_types = (
                                 'Dead', 'Idle', 'Jump', 'JumpMelee',
                                 'JumpShoot', 'Melee', 'Run', 'RunShoot',
                                 'Shoot', 'Slide'
                                )
        for animation in self.animation_types:
            images_list = []
            n = len(os.listdir(f"./png/{animation}"))
            for i in range(1,n):
                img = pygame.image.load(f"./png/{animation}/{animation}{i}.png")
                img = pygame.transform.scale_by(img, 0.4)
                images_list.append(img)
            self.all_images[animation] = images_list

        self.image = self.all_images['Idle'][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.frame_index  = 0
        self.action = "Idle"
        self.last_animation_time = pygame.time.get_ticks()
        self.flip = False
        self.moving = False
        self.yvelocity = 0
        self.jump = False
    def draw(self, screen):
        self.image = self.all_images[self.action][self.frame_index]
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.animation()
    

    def animation(self):
        if pygame.time.get_ticks() - self.last_animation_time >= 100:
            self.frame_index += 1
            if  self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
            self.last_animation_time = pygame.time.get_ticks()

    def change_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.frame_index = 0

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.flip = True
            self.moving = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.flip = False
            self.moving = True
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False

        if keys[pygame.K_UP]:
            self.yvelocity = -10

        dy += self.yvelocity
        self.yvelocity += 1

        if self.rect.bottom + dy >= 500:
            self.yvelocity = 0
            dy = 500 - self.rect.bottom
            

        self.rect.x += dx
        self.rect.y += dy
        


