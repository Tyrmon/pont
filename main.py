from pygame import *
from random import *
class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x , self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 5:    
            self.rect.y -= self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:    
            self.rect.y -= self.speed
    

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
font.init()
font1 = font.SysFont('Arial',36)
lose1 = font1.render('player 1(L) lose', True,(155,0,55))
lose2 = font1.render('player 2(R) lose', True,(155,0,55))
window = display.set_mode((700,500))
display.set_caption("Ping-pong")
background = transform.scale(image.load("zxc.png"),(700,500))
clock = time.Clock()
fps = 80
player1 = Player('chis.png', 5,250, 10)
player2 = Player('hero1.png', 640,250, 10)
ball = Enemy('Night.png',250,250,5)
speed_y = 3
speed_x = 3

game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))  
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if ball.rect.x > 700:
            finish = True
            window.blit(lose1,(250,250))
        if ball.rect.x < 0:
            finish = True
            window.blit(lose2, (250,250))
            
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()           

    display.update()
    clock.tick(fps)    
    