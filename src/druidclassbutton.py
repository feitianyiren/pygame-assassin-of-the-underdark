
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

from multiclassselectorbutton import *
from playerhumandruidresources import *

class DruidClassButton(MultiClassSelectorButton):
    "Druid Class Selector Window Button"
    def __init__(self, parent, callback, node):
	MultiClassSelectorButton.__init__(self, parent, callback, node, PlayerHumanDruidResources())
	self.x = 100
	self.y = 50
	self.w = 50 
	self.h = 50 
	if callback == None:
		self.callback = self.cb
	self.borderwidth = 1

    def cb(self):
	print "Druid class - Mutliclassselectorbutton clicked !"
