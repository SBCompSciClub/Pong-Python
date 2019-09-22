import pygame
BLACK = (0,0,0) 

class Paddle(pygame.sprite.Sprite):
    #Paddle Class
    
    def __init__(self, color, width, height):
        
        super().__init__()
        
        #initialize image
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        #get rectangle 
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
    	#move up
        self.rect.y -= pixels
        #Check if too far up 
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
    	#move down
        self.rect.y += pixels
        #Check if too far down
        if self.rect.y > 400:
          self.rect.y = 400