
# Copyright (C) Johan Ceuppens 2010
# Copyright (C) Johan Ceuppens 2014
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
from stateimagelibrary import *
from playerkatta import *
from playerfighter import *
from playermagicuser import *
from playerthief import *
from playerelf import *
from playergnoll import *
from playerdrow import *
from playerhuman import *


class PlayerBase:
    def __init__(self):
       	1	 

class PlayerBase(PlayerBase,PlayerBase):
    "Player"

    PlayerBase.FIGHTER,PlayerBase.MAGICUSER,PlayerBase.THIEF = xrange(3)
    PlayerBase.ELF,PlayerBase.GNOLL,PlayerBase.KATTA,PlayerBase.HUMAN,PlayerBase.DROW = xrange(5)
    
    def __init__(self,PLAYERRACE,PLAYERCLASS,heartmeter):
        classByType = {
                PlayerBase.HUMAN : PlayerHuman,
                PlayerBase.GNOLL : PlayerGnoll,
                PlayerBase.KATTA : PlayerKatta,
                PlayerBase.ELF : PlayerElf,
                PlayerBase.DROW : PlayerDrow,
        }
        classByType2 = {
                PlayerBase.FIGHTER : PlayerFighter,
                PlayerBase.MAGICUSER : PlayerMagicuser,
                PlayerBase.THIEF : PlayerThief,
        }
	self.heartmeter = heartmeter
	self.hitpoints = 78
        self.x = 150 
        self.y = 150 
        self.w = 48 
        self.h = 48
	self.stimlib = Stateimagelibrary()	
        image = pygame.image.load('./pics/player1-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/player2-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/player3-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/player2-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/player1-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/player2-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/player3-30x30.bmp').convert()
        image.set_colorkey((0,0,0)) 
	self.stimlib.addpicture(image)	

        self.stimlibfight = Stateimagelibrary()	
        image = pygame.image.load('./pics/playerfight1-30x30.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerfight1-30x30.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerfight2-30x30.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerfight2-30x30.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerfight3-30x30.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)
        image = pygame.image.load('./pics/playerfight3-30x30.bmp').convert()
        image.set_colorkey((0,0,0))
        self.stimlibfight.addpicture(image)

        self.fightcounter = 0

        classByType[PLAYERRACE](heartmeter)
        classByType2[PLAYERCLASS](heartmeter)

    def drawstatic(self, screen):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return
	self.stimlib.drawstatic(screen,self.x,self.y,0)
	
    def draw(self, screen):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return
        self.stimlib.draw(screen, self.x,self.y)

    def fight(self,room):
        self.fightcounter = 1
##        self.x -= 30
##        self.y -= 30
##        self.w += 30
##        self.h += 30
        
        o = room.collidesword(room,self)
        
        if o:
            print 'hit!'
            room.hitwithsword(o)
##        self.x += 30
##        self.y += 30
##        self.w -= 30
##        self.h -= 30
##        
    def hit(self):
	self.heartmeter.index -= 1 
	if self.heartmeter.index <= 0:
		return 0 #FIXME1 FIX for gameover when collision with enemies 
	else:
		return 0	

    def askclass(self):
        return "Fighter"

    def askrace(self):
        return "Human"

    def askpicture(self):
        return './pics/taskbar-PC.bmp'

    def collidewithenemyweapon(self,room,o):
        if o.collide(room,self):
		return self ## NOTE : returns collided entity (single)
		
	return None

    def hitwithenemyweapon(self,damage):
	if damage > 0:
		print 'player is hit!'
        self.hitpoints -= damage

    def pickup(self,room):
        n = room.pickup(self)
	return n

    def fight(self,room):
        self.fightcounter = 1
        o = room.collidesword(self)
        if o:
            o.hitwithweapon(self.sword.roll())
       
    def setrubysword(self):
	self.sword = RubySword(0,0)

