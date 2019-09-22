import pygame
from random import randint

BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #Ball Class
    
    def __init__(self, color, width, height):
        super().__init__()
        
        #initialize image
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw Rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #velocty array [x,y]
        self.velocity = [randint(4,8),randint(-8,8)]
        
        #get rectangle 
        self.rect = self.image.get_rect()
        
    def update(self):
        #update ball position with velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        #bounce ball 
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)