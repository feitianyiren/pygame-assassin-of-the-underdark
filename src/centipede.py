
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from gameobject import *
from stateimagelibrary import *
import random
from rng import *
from time import *

class Centipede(Gameobject):
    "Centipede"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 50 
        self.h = 66 

        self.hitpoints = 3
        
	self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/centipede1-50x66.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/centipede2-50x66.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)

	self.talkcounter = 0
	self.direction = "left"

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,room,player):
        sleep(.04) # FIX goblin sleep
	if room.collidewithenemy(self):
	    if (self.direction == "right"):
	        self.x -=6
	        self.direction = "left" 
	    elif (self.direction == "left"):
	        self.x +=6
	        self.direction = "right"
	    elif (self.direction == "down"):
	        self.y -=6
	        self.direction = "up" 
	    elif (self.direction == "up"):
	        self.y +=6
	        self.direction = "down"

	if player.x+28-room.relativex < self.x:
		self.x -= 3
		self.direction = "left"
	if player.x-28-room.relativex > self.x:
		self.direction = "right"
		self.x += 3	
	if player.y+10-room.relativey < self.y:
		self.direction = "up"
		self.y -= 3
	if player.y-10-room.relativey > self.y:
		self.direction = "down"
		self.y += 3

    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h +self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0 ## for game self.talker


    def fight(self,room,player):
        self.fightcounter = 1
        o = player.collidewithenemyweapon(room,self)
        if o:
            player.hitwithenemyweapon(RNG().rollcentipede())
