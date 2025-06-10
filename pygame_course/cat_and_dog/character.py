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
        self.animation_time = pygame.time.get_ticks()
        self.idle = True
        self.flip = False
        self.slide = False
        self.jump = False
        self.yspeed = 0
    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(img, self.rect)
        self.do_animation()

    def do_animation(self):
        self.image = self.all_images[self.animation][self.frame_index]
        if pygame.time.get_ticks() - self.animation_time > 100:
            self.animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.animation]):
                self.frame_index = 0

    def move_horizontal(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.jump = True
            self.yspeed = -15
        else:
            self.jump = False
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.slide = True
        elif not keys[pygame.K_LEFT] and not keys[pygame.K_DOWN]:
            self.slide = False
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.slide = True
        elif not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
            self.slide = False


        if keys[pygame.K_LEFT]:
            self.idle = False
            self.flip = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.idle = False
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True
        
        dy += self.yspeed
        self.yspeed += 1
        if self.rect.bottom + dy > 500:
            dy = 500 - self.rect.bottom
            self.yspeed = 0
        self.rect.x += dx
        self.rect.y += dy

    def change_animation(self, new_animation):
        if self.animation != new_animation:
            self.animation = new_animation
            self.frame_index = 0
            self.animation_time = pygame.time.get_ticks()







