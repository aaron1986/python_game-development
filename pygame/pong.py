import pygame, sys
import random
import math
import time
pygame.init()

#Screen Width/Height
screen = pygame.display.set_mode((800,600))

#Background Image
background_image = pygame.image.load("tennis.jpg").convert()

#Score Font
pygame.font.init()
font = pygame.font.Font("Bombing.TTF", 50)

#Graphics Font
graphicsScore = "Game Score!"
graphicsFont = pygame.font.Font("Bombing.TTF", 50)

#Paddle Player1
paddle_player1 = pygame.Rect(5,50,5,60)
player1Score = 0

#Paddle Player2
paddle_player2 = pygame.Rect(790,50,5,60)
player2Score = 0

#Ball
ball = pygame.Rect(300,200,20,20)
ballAngle = math.radians(0)
ballSpeed = 10
ballDirection = -1

#Reset Ball
ball.x = 300
ball.y = 200
resetBall = ball.x, ball.y

#frame
clock = pygame.time.Clock()

#Process Player Input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                    
            timeChange = pygame.time.get_ticks() - totalTime
            totalTime = pygame.time.get_ticks()
            
        player1_up = pygame.key.get_pressed()[pygame.K_w] 
        player1_down = pygame.key.get_pressed()[pygame.K_s]

        player2_up = pygame.key.get_pressed()[pygame.K_UP]
        player2_down = pygame.key.get_pressed()[pygame.K_DOWN]
        
#Updating Game State Logic
        if player1_up:
            paddle_player1.y += -50 
        if player1_down:
            paddle_player1.y += 50 
        if player2_up:
            paddle_player2.y += -50 
        if player2_down:
            paddle_player2.y += 50 

        if paddle_player1.y < 0:
            paddle_player1.y = 0
        if paddle_player2.y < 0:
            paddle_player2.y = 0

        if paddle_player1.y > screen.get_height() - paddle_player1.height:
            paddle_player1.y = screen.get_height() - paddle_player1.height
        if paddle_player2.y > screen.get_height() - paddle_player2.height:
            paddle_player2.y = screen.get_height() - paddle_player2.height

               
#Update Ball
    ball.x += ballDirection * ballSpeed * math.cos(ballAngle)
    ball.y += ballDirection * ballSpeed * math.sin(ballAngle)
    if ball.x > 800 or ball.x < 0:
        ballSpeed *= 1
        if ball.x > 800:
            player1Score += 1
            applause = pygame.mixer.music.load('applause.wav')
            pygame.mixer.music.play()
            ball.x, ball.y = resetBall 
        if ball.x < 0:
            player2Score += 1
            applause = pygame.mixer.music.load('applause.wav')
            pygame.mixer.music.play()
            ball.x, ball.y = resetBall
            
    if player1Score >= 10 or player2Score >= 10:
               player1Score = 0
               player2Score = 0
               
#Paddle Collision
    if ball.colliderect(paddle_player1):
            if ball.x < 5:
                ballDirection *= -1
                ballAngle = random.randrange(20, 300)
                pong = pygame.mixer.music.load('serve.wav')
                pygame.mixer.music.play()
    if ball.colliderect(paddle_player2):
            if ball.x > 40:
                ballDirection *= -1
                ballAngle = random.randrange(20, 300)
                pong = pygame.mixer.music.load('serve.wav')
                pygame.mixer.music.play()
#Wall Collision
    if ball.y <= 0:
        ballAngle *= -1
    if ball.y >= 600:
        ballAngle *= -1
    

#Rendering
    screen.blit(background_image, [0,0])
    screen.blit(font.render(str(player1Score), 1, (178,34,34)),(200, 25))
    screen.blit(font.render(str(player2Score), 1, (178,24,24)),(600, 25))
    screen.blit(font.render(str(graphicsScore), 1, (245,255,250)), (330, 25))
    pygame.draw.rect(screen,(0,0,0), paddle_player1)
    pygame.draw.rect(screen,(0,0,0), paddle_player2)
    pygame.draw.rect(screen,(0,255,0), ball)
 
    clock.tick(50)
    pygame.display.flip()
