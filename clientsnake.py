import sys, pygame
import numpy as np
from time import time
from numpy import random
from random import randrange
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.

import sys
from socket import *
host = '127.0.0.1'
port1 = 9000
sock1 = socket()
sock1.connect((host, port1))
port2 = 9001
sock2 = socket()
sock2.connect((host, port2))
port3 = 9002
sock3 = socket()
sock3.connect((host, port3))
port4 = 9003
sock4 = socket()
sock4.connect((host, port4))
'''while True:
  data = raw_input('enter something')
  sock.send(data)
  data = sock.recv(1024)

  print 'Received ' + repr(data)'''

cv1=0
cv2=0

myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()
size = width, height = 1000,600
#player1
ctr = 4
velocityx=1
velocityy=0
posx=[-20,-30,-40,-50]
posy=[200,200,200,200]
#random time duration..
timera=[2.2,2,3,2.6]
body = [pygame.image.load("body1.png"), pygame.image.load("body1.png"), pygame.image.load("body1.png"),
         pygame.image.load("body1.png")]
bodyrect = [body[0].get_rect(), body[1].get_rect(), body[2].get_rect(), body[3].get_rect()]
#player2
ctr_=4
velocityx_ = -1
velocityy_ = 0
posx_ = [870, 880, 890, 900]
posy_ = [200, 200, 200, 200]

body_ = [pygame.image.load("body1.png"), pygame.image.load("body1.png"), pygame.image.load("body1.png"),
         pygame.image.load("body1.png")]
bodyrect_ = [body[0].get_rect(), body[1].get_rect(), body[2].get_rect(), body[3].get_rect()]
#food poison initialisation..
food = [pygame.image.load("body2.png"),pygame.image.load("body2.png"),pygame.image.load("body2.png"),pygame.image.load("body2.png")]
poison = [pygame.image.load("body3.png"),pygame.image.load("body3.png"),pygame.image.load("body3.png"),pygame.image.load("body3.png")]
foodrect = [food[0].get_rect(),food[1].get_rect(),food[2].get_rect(),food[3].get_rect()]
poisonrect = [poison[0].get_rect(),poison[1].get_rect(),poison[2].get_rect(),poison[3].get_rect()]
listx=[]
listy=[]
for i in range(-30,800,10):
    listx.append(i)
for i in range(-30,400,10):
    listy.append(i)
posfx=[0,0,0,0]
posfy=[0,0,0,0]
state=[0,0,0,0]
#initially setting food
for i in range(0,4,1):
 random_indexx = randrange(0, len(listx))
 random_indexy = randrange(0, len(listy))
 posfx[i]=listx[random_indexx]
 posfy[i]=listy[random_indexy]
 #for texting
def text_to_screen(screen, text, x, y, size = 50,
            color = (200, 000, 000), font_type =myfont):
    try:

        text = str(text)
        font = font_type
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
        pygame.display.flip()
    except Exception, e:
        print 'Font Error, saw it coming'
        raise e
ticks=[time(),time(),time(),time()]
mara1=mara2=0
while 1:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('SNAKE::1.0')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #pygame.draw.rect(screen,(255,255,255),(posy,posx,posy+10,posx+10))
    #hitting boundaries
    if mara1==1 and mara2==1:
        text_to_screen(screen, 'GAME OVER', 500, 100)
        text_to_screen(screen, 'SCORE::' + str((ctr - 4) * 10), 500, 200)
        text_to_screen(screen, 'SCORE::' + str((ctr_ - 4) * 10), 500, 300)
        pygame.time.delay(4000)
        sys.exit()
    if mara1==0:
     if posx[0]>910 or posx[0]<-51 or posy[0]<-51 or posy[0]>510:
            text_to_screen(screen,'GAME OVER',500,100)
            text_to_screen(screen,'SCORE::'+str((ctr-4)*10),500,200)
            pygame.draw.rect(screen,[255,0,0],[100,500,10,50])
            mara1=1
     #hitting itself
     for i in range(1,ctr,1):
      if((posx[0]==posx[i])and(posy[0]==posy[i])):
           text_to_screen(screen, 'GAME OVER', 500, 100)
           text_to_screen(screen, 'SCORE::' + str((ctr - 4) * 10), 500, 200)
           pygame.draw.rect(screen, [255, 0, 0], [100, 500, 10, 50])
           mara1=1
     #input keyboard comms
     sock1.send(str(velocityx))
     sock2.send(str(velocityy))
     if velocityy==0:
      if (pygame.key.get_pressed()[pygame.K_UP] != 0):
        velocityy=-1
        velocityx=0
      if (pygame.key.get_pressed()[pygame.K_DOWN] != 0):
        velocityy= 1
        velocityx= 0
     else:
      if (pygame.key.get_pressed()[pygame.K_LEFT] != 0):
        velocityy = 0
        velocityx = -1
      if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
        velocityy = 0
        velocityx = 1
     if ctr>1:
        for i in range(ctr-1,0,-1):
            posx[i]=posx[i-1]
            posy[i]=posy[i-1]
     posx[0]=posx[0]+velocityx*10
     posy[0]=posy[0]+velocityy*10
     for i in range(ctr):
      screen.blit(body[i],(posx[i],posy[i]))
     #on eating the food
     eat1=-1
     for io in range(0,4,1):
      if np.abs(posfy[io]-posy[0])<20 and np.abs(posfx[io]-posx[0])<20:
        random_indexx = randrange(0, len(listx))
        random_indexy = randrange(0, len(listy))
        eat1=io
        posfx[io] = listx[random_indexx]
        posfy[io] = listy[random_indexy]
        if state[io]==1:
         body.append(pygame.image.load("body1.png"))
         bodyrect.append(body[ctr].get_rect())
         posx.append(posx[ctr-1])
         posy.append(posy[ctr-1])
         ctr=ctr+1
         print('wow')
        else:
         if ctr==1:
             text_to_screen(screen,'GAME OVER', 500, 100)
             text_to_screen(screen,'SCORE::' + str((ctr - 4) * 10), 500, 200)
             pygame.draw.rect(screen, [255, 0, 0], [100, 500, 10, 50])
             mara1=1
         else:
             body.pop(ctr-1)
             bodyrect.pop(ctr-1)
             posx.pop(ctr-1)
             posy.pop(ctr-1)
             ctr=ctr-1
             print('no')
    #player2 added...
    if mara2==0:
     if posx_[0]>910 or posx_[0]<-51 or posy_[0]<-51 or posy_[0]>510:
            text_to_screen(screen,'GAME OVER',500,100)
            text_to_screen(screen,'SCORE::'+str((ctr_-4)*10),500,200)
            pygame.draw.rect(screen,[255,0,0],[100,500,10,50])
            mara2=1
     #hitting itself
     for i in range(1,ctr_,1):
      if(posx_[0]==posx_[i] and posy_[0]==posy_[i]):
           text_to_screen(screen, 'GAME OVER', 500, 100)
           text_to_screen(screen, 'SCORE::' + str((ctr_ - 4) * 10), 500, 200)
           pygame.draw.rect(screen, [255, 0, 0], [100, 500, 10, 50])
           mara2=1
     #input keyboard comms
     '''if velocityy_==0:
      if (pygame.key.get_pressed()[pygame.K_w] != 0):
        velocityy_=-1
        velocityx_=0
      if (pygame.key.get_pressed()[pygame.K_s] != 0):
        velocityy_= 1
        velocityx_= 0
     else:
      if (pygame.key.get_pressed()[pygame.K_a] != 0):
        velocityy_ = 0
        velocityx_ = -1
      if (pygame.key.get_pressed()[pygame.K_d] != 0):
        velocityy_ = 0
        velocityx_ = 1'''
     velocityx_=int(sock3.recv(1024))
     velocityy_=int(sock4.recv(1024))
     print velocityx_
     if ctr_>1:
        for i in range(ctr_-1,0,-1):
            posx_[i]=posx_[i-1]
            posy_[i]=posy_[i-1]
     posx_[0]=posx_[0]+velocityx_*10
     posy_[0]=posy_[0]+velocityy_*10
     for i in range(ctr_):
      screen.blit(body_[i],(posx_[i],posy_[i]))
    #on eating the food
     eat2=-1
     for io in range(0,4,1):
      if np.abs(posfy[io]-posy_[0])<20 and np.abs(posfx[io]-posx_[0])<20:
        random_indexx = randrange(0, len(listx))
        random_indexy = randrange(0, len(listy))
        eat2=io
        posfx[io] = listx[random_indexx]
        posfy[io] = listy[random_indexy]
        if state[io]==1:
         body_.append(pygame.image.load("body1.png"))
         bodyrect_.append(body_[ctr_].get_rect())
         posx_.append(posx_[ctr_-1])
         posy_.append(posy_[ctr_-1])
         ctr_=ctr_+1
         print('wow')
        else:
         if ctr_==1:
             text_to_screen(screen,'GAME OVER', 500, 100)
             text_to_screen(screen,'SCORE::' + str((ctr_ - 4) * 10), 500, 200)
             pygame.draw.rect(screen, [255, 0, 0], [100, 500, 10, 50])
             mara2=1
         else:
             body_.pop(ctr_-1)
             bodyrect_.pop(ctr_-1)
             posx_.pop(ctr_-1)
             posy_.pop(ctr_-1)
             ctr_=ctr_-1
             print('no')


    # random food pos added
    random_indexx = randrange(0, len(listx))
    random_indexy = randrange(0, len(listy))
    for uo in range(0,4,1):
     if (time() - ticks[uo]) < timera[uo]:
        if (state[uo] == 0):
            screen.blit(poison[uo], (posfx[uo], posfy[uo]))
        else:
            screen.blit(food[uo], (posfx[uo], posfy[uo]))
     else:
        if (state[uo] == 0):
            state[uo] = 1
            ticks[uo] = time()
        else:
            state[uo] = 0
            ticks[uo] = time()
    for bo,co in zip(posx_,posy_):
        if ((np.abs(bo - posx[0]) < 20 and np.abs(co - posy[0]) == 0) or (np.abs(co - posy[0]) < 20 and np.abs(bo - posx[0]) == 0) and (cv1==0)):
            cv1=1
            if ctr == 1:
                text_to_screen(screen, 'GAME OVER', 500, 100)
                text_to_screen(screen, 'SCORE::' + str((ctr - 4) * 10), 500, 200)
                pygame.draw.rect(screen, [255, 0, 0], [100, 500, 10, 50])
                mara1 = 1
            else:
                body.pop(ctr - 1)
                bodyrect.pop(ctr - 1)
                posx.pop(ctr - 1)
                posy.pop(ctr - 1)
                ctr = ctr - 1
                print('no')
            break
        else:
            cv1=0

    for bo,co in zip(posx,posy):
        if((np.abs(bo-posx_[0])<20 and np.abs(co-posy_[0])==0)or(np.abs(co-posy_[0])<20 and np.abs(bo-posx_[0])==0)and(cv2==0)):
            cv2=1
            if ctr_ == 1:
                text_to_screen(screen, 'GAME OVER', 500, 100)
                text_to_screen(screen, 'SCORE::' + str((ctr_ - 4) * 10), 500, 200)
                pygame.draw.rect(screen, [255, 0, 0], [100, 500, 10, 50])
                mara2 = 1
            else:
                body_.pop(ctr_ - 1)
                bodyrect_.pop(ctr_ - 1)
                posx_.pop(ctr_ - 1)
                posy_.pop(ctr_ - 1)
                ctr_ = ctr_ - 1
                print('no')
            break
        else:
            cv2=0
    pygame.time.delay(100)
    pygame.display.flip()