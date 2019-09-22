import pygame
from paddle import Paddle
from ball import Ball
from settings import Settings
 
pygame.init()
 
# Define colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#initialize settings
settings = Settings()
 
# Open a new window
size = (settings.screen_width, settings.screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
#initialize left paddle
paddleLeft = Paddle(settings.paddle_color, settings.paddle_width, settings.paddle_height)
paddleLeft.rect.x = settings.leftStartX
paddleLeft.rect.y = settings.leftStartY

#initialize right paddle 
paddleRight = Paddle(settings.paddle_color, settings.paddle_width, settings.paddle_height)
paddleRight.rect.x = settings.rightStartX
paddleRight.rect.y = settings.rightStartY
 
#initialize ball
ball = Ball(settings.ball_color, settings.ball_width, settings.ball_height)
ball.rect.x = settings.ballStartX
ball.rect.y = settings.ballStartY
 
#sprite list
sprites_list = pygame.sprite.Group()
 
#Add objects to list
sprites_list.add(paddleLeft)
sprites_list.add(paddleRight)
sprites_list.add(ball)
 
#Flag to check if game is running
running = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
#Initialise player scores
scoreLeft = 0
scoreRight = 0
 
while running:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              running = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     running=False
 
    #Move both paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleLeft.moveUp(5)
    if keys[pygame.K_s]:
        paddleLeft.moveDown(5)
    if keys[pygame.K_UP]:
        paddleRight.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleRight.moveDown(5)    
 
    
    sprites_list.update()
    
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= settings.screen_right:
        scoreLeft += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.x <= 0:
        scoreRight += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y > settings.screen_top:
        ball.velocity[1] = -ball.velocity[1]
        
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]     
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleLeft) or pygame.sprite.collide_mask(ball, paddleRight):
    		ball.bounce()
    
    #Clear Screen to Black
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, settings.netStartPos, settings.netEndPos, settings.netWidth)
    
    #Draw Sprites
    sprites_list.draw(screen) 
 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreLeft), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreRight), 1, WHITE)
    screen.blit(text, (420,10))
 
    #Update Screen
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()