
# Copyright (C) Johan Ceuppens 2010-2014 
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

class WidgetFrame:
    ""
    def __init__(self, xx, yy, ww, hh):
	self.x = xx
	self.y = yy
	self.w = ww
	self.h = hh

    def draw(self, screen):
	1

    def setx(self,xx):
	self.x = xx

    def sety(self,yy):
	self.y = yy

    def getx(self):
	return self.x

    def gety(self):
	return self.y
