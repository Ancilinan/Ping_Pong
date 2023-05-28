import pygame
from pygame import *
from random import randint
pygame.init()

mixer.init()
font.init()

FPS = 90
clock = time.Clock()

window = display.set_mode((700, 500))
display.set_caption('ПингПонг')

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

   def move_redplayer(self):
      if keys[K_w] and self.rect.y > 10:
         self.rect.y -= self.speed
      if keys[K_s] and self.rect.y < 410:
         self.rect.y += self.speed

   def move_blueplayer(self):
      if keys[K_UP] and self.rect.y > 10:
         self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < 410:
         self.rect.y += self.speed


background = GameSprite("background.jpg", 0, 0, 700, 500, 0)

redplayer = GameSprite("RedLine.png", 10, 200, 20, 80, 5)
blueplayer = GameSprite("BlueLine.png", 665, 200, 20, 80, 5)#Расположение по X, Расположение по Y, ширина, длина, скорость.

ball = GameSprite("ball.png", 325, 250, 50, 50, 0)

mixer.music.load("megalovania.ogg")
mixer.music.play()

speed_x = 3
speed_y = 3

game = True
finish = False

font1 = font.SysFont("Arial", 35)
lose1 = font1.render('Синий игрок победил!', True, (16, 198, 222))

font2 = font.SysFont("Arial", 35)
lose2 = font2.render('Красный игрок победил!', True, (245, 10, 10))

while game:

   for el in event.get():
       if el.type == QUIT:
           game = False

   if finish == False:
      background.reset()

   if finish == False:
      redplayer.reset()

   if finish == False:
      blueplayer.reset()

   if finish != True:
      ball.rect.x += speed_x
      ball.rect.y += speed_y

   if ball.rect.y > 450:
      speed_y *= -1
      
   if ball.rect.y < 0:
      speed_y *= -1
      
   if sprite.collide_rect(redplayer, ball):
      speed_x *= -1
      
   if sprite.collide_rect(blueplayer, ball):
      speed_x *= -1

   if ball.rect.x < -50:
      finish = True
      window.blit(lose1, (200, 200))
      
   if ball.rect.x > 700:
      finish = True
      window.blit(lose2, (200, 200))

   keys = key.get_pressed()
   redplayer.move_redplayer()
   blueplayer.move_blueplayer()
   ball.reset()

   clock.tick(FPS)
   display.update()

