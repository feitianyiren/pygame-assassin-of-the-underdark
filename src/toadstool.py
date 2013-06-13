
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

class Toadstool(Gameobject):
    "Box"
    def __init__(self, xx,yy):
        Gameobject.__init__(self,xx,yy)
        self.w = 48
        self.h = 48 
        self.image = pygame.image.load('./pics/toadstool1-48x48.bmp').convert()
        self.image.set_colorkey((0,0,0)) 

    def setimage(self, imagefilename,r,g,b):
        self.image = pygame.image.load(imagefilename).convert()
        self.image.set_colorkey((r,g,b)) 

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision in toadstool!"	
	    return 2 
	else:
	    return 0
