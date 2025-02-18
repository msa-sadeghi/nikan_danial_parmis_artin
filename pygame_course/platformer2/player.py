import pygame
class Player:
    def __init__(self, x,y):
        self.animation_types = ("Idle", "Run")
        self.all_images = {}
        
        for animation_t in self.animation_types:
            
            if animation_t == "Idle":
                temp_list = []
                for i in range(1, 10):
                    img = pygame.image.load(f"Idle ({i}).png")
                    img_width = img.get_width()
                    img_height = img.get_height()
                    img = pygame.transform.scale(img, (img_width * 0.5, img_height * 0.5))
                    temp_list.append(img)
                    
                self.all_images["Idle"] = temp_list
            elif animation_t == "Run":
                temp_list = []
                for i in range(1,9):
                    img = pygame.image.load(f"Run ({i}).png")
                    img_width = img.get_width()
                    img_height = img.get_height()
                    img = pygame.transform.scale(img, (img_width * 0.5, img_height * 0.5))
                    temp_list.append(img)
                    
                self.all_images["Run"] = temp_list
                
        self.frame_index = 0
        self.image = self.all_images["Idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.last_time = pygame.time.get_ticks()
        self.moving_state = "Idle"
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.animation()
        
    def animation(self):
        self.image = self.all_images[self.moving_state][self.frame_index]
        if pygame.time.get_ticks() - self.last_time >= 100:
            
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.moving_state]):
                self.frame_index = 0
            self.last_time = pygame.time.get_ticks()
            
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.moving_state = "Run"
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.moving_state = "Run"
            
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving_state = "Idle"
            
        
        
                
                
                    
                    
            
        