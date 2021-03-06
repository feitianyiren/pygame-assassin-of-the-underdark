#!/usr/local/bin/python
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

from maproom1 import *
from maproom2 import *
from maproom3 import *

from rng import *
from multiraceselector import *
from multiclassselector import *
from charactersheetwindow import *
from pythonshellwindow import *
##from selector import *
from taskbar import *
from time import *
from sys import *
from inventory import *
from spellbook import *
from heartmeter import *
from manameter import *
from playergnollfighter import *
from playerhumanfighter import *
from playerhumanfightermagicuser import *
from playerhumanfighterthief import *
from playerhumanmagicuserthief import *
from playerkattafighter import *
from playerkattafightermagicuser import *
from playerkattafighterthief import *
from playerkattamagicuserthief import *
from playerelffighter import *
from playerdrowfighter import *
from bomb import *
from playergnollmagicuser import *
from playergnollfightermagicuser import *
from playergnollfighterthief import *
from playergnollmagicuserthief import *
from playerhumanmagicuser import *
from playerkattamagicuser import *
from playerelfmagicuser import *
from playerdrowmagicuser import *
from playergnollthief import *
from playerhumanthief import *
from playerkattathief import *
from playerelfthief import *
from playerelfmagicuser import *
from playerelffightermagicuser import *
from playerelffighterthief import *
from playerelfmagicuserthief import *
from playerdrowthief import *
from playerdrowfightermagicuser import *
from playerdrowfighterthief import *
from playerdrowmagicuserthief import *
from playerhumanmonk import *
from playergnollmonk import *
from playerkattamonk import *
from playerelfmonk import *
from playerdrowmonk import *
from playerhumanassassin import *
from playergnollassassin import *
from playerkattaassassin import *
from playerelfassassin import *
from playerdrowassassin import *
from playerhumandruid import *
from playergnolldruid import *
from playerkattadruid import *
from playerelfdruid import *
from playerdrowdruid import *

import imagepluginmanager
import sys,os

class Game:
    "Main function"
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((300, 350))
        self.font = pygame.font.SysFont("Times", 8)
        gameover = 0
	
	self.charactersheet = None

        blankimage = pygame.image.load('./pics/blank.bmp').convert()
        ## There are several title screens in the ./pics/ directory
        titleimage = pygame.image.load('./pics/titlescreen0.3.bmp').convert()
        self.x = 0
        self.y = 0
       
        while gameover == 0:
            pygame.display.update()
            self.screen.blit(titleimage, (0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1

        self.room = Maproom1(0,0)
        self.heartmeter = HeartMeter()
        self.manameter = ManaMeter()
	self.player = None
        self.screen.blit(blankimage, (0,0))

	# display multiclass selection screen and wait for mouse click choice

        self.selectormc = MultiClassSelector(self.screen, self.font)

        self.selectormc.window_mainloop(0.3)



        self.selectormr = MultiRaceSelector(self.screen, self.font)

	# display character selection screen and wait for mouse click choice

        self.selectormr.window_mainloop(0.3)
       
	# get data from character selector screen 

	if self.selectormr.askrace() == "Human":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerHumanFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerHumanMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerHumanThief()
            elif self.selectormc.askclass() == "Monk":
                self.player = PlayerHumanMonk()
            elif self.selectormc.askclass() == "Assassin":
                self.player = PlayerHumanAssassin()
            elif self.selectormc.askclass() == "Druid":
                self.player = PlayerHumanDruid()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerHumanFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerHumanFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerHumanMagicuserThief()
        elif self.selectormr.askrace() == "Gnoll":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerGnollFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerGnollMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerGnollThief()
            elif self.selectormc.askclass() == "Monk":
                self.player = PlayerGnollMonk()
            elif self.selectormc.askclass() == "Assassin":
                self.player = PlayerGnollAssassin()
            elif self.selectormc.askclass() == "Druid":
                self.player = PlayerGnollDruid()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerGnollFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerGnollFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerGnollMagicuserThief()
        elif self.selectormr.askrace() == "Katta":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerKattaFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerKattaMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerKattaThief()
            elif self.selectormc.askclass() == "Monk":
                self.player = PlayerKattaMonk()
            elif self.selectormc.askclass() == "Assassin":
                self.player = PlayerKattaAssassin()
            elif self.selectormc.askclass() == "Druid":
                self.player = PlayerKattaDruid()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerKattaFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerKattaFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerKattaMagicuserThief()
        elif self.selectormr.askrace() == "Elf":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerElfFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerElfMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerElfThief()
            elif self.selectormc.askclass() == "Monk":
                self.player = PlayerElfMonk()
            elif self.selectormc.askclass() == "Assassin":
                self.player = PlayerElfAssassin()
            elif self.selectormc.askclass() == "Druid":
                self.player = PlayerElfDruid()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerElfFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerElfFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerElfMagicuserThief()
        elif self.selectormr.askrace() == "Drow":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerDrowFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerDrowMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerDrowThief()
            elif self.selectormc.askclass() == "Monk":
                self.player = PlayerDrowMonk()
            elif self.selectormc.askclass() == "Assassin":
                self.player = PlayerDrowAssassin()
            elif self.selectormc.askclass() == "Druid":
                self.player = PlayerDrowDruid()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerDrowFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerDrowFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerDrowMagicuserThief()

##        if self.selectormr.askrace() == "Abeille":
##            if self.selectormc.askclass() == "Fighter":
##                self.player = PlayerAbeilleFighter()

	# set race and class in player object

	self.player.setrace(self.selectormr.askrace())
	self.player.setclass(self.selectormc.askclass())

	self.player.setheartmeter(self.heartmeter)        
	self.player.setmanameter(self.manameter)        
        self.inventory = Inventory()
        self.inventoryitem = None 
        self.spellbook = Spellbook()
        self.spellitem = None 
	self.talker = None
	self.talktext = "" 
        self.taskbar = Taskbar(self.screen,self.font,self.player)
       
	self.imagepluginmanager = imagepluginmanager.ImagePluginManager("./plugins/")
	self.imagepluginmanager.start()

	sys.path.append(self.imagepluginmanager.plugindirectory)
	for f in self.imagepluginmanager.getpluginfilenames():
		execfile(self.imagepluginmanager.plugindirectory + f)	
			
        pygame.key.set_repeat(90,90)
        gameover = 0
        while gameover == 0:

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
            	   
		    if event.key == K_ESCAPE:
			gameover = 1

                    self.player.draw(self.screen)

                    ###if event.key == K_p:
	            ###		self.pythonshellwindow = PythonShellWindow(self.screen, self.font)
	            ###		self.pythonshellwindow.window_mainloop(0.3)
                    if event.key == K_j:
				self.charactersheet = CharacterSheetWindow(self.screen, self.font, self.player)
        			self.charactersheet.window_mainloop(0.3)

                    if event.key == K_s:
			if self.taskbar.inventoryitem != None:
                        	self.taskbar.inventoryitem.use(self)

                    if event.key == K_c:
			if self.taskbar.spellitem != None:
				if self.player.manapoints >= 0:
                        		self.taskbar.spellitem.cast(self)
					self.player.manapoints -= self.taskbar.spellitem.manapoints
                    if event.key == K_x:
                        o = self.player.pickup(self.room)
		        if o != None:
				self.inventory.setpickup(o)
				self.taskbar.setpickup(o)
				self.spellbook.setpickup(o)
				self.room.removegameobject(o)

                    if event.key == K_t:
                        o = self.player.talkto(self.room)
		        if o != None:
				self.talker = o	
				self.talktext = o.gettalktext(self)

	            elif event.key == K_z:
                        self.player.fight(self)  
                    elif event.key == K_UP:
                        self.room.movedown()    
                    elif event.key == K_DOWN:
                        self.room.moveup()    
                    elif event.key == K_LEFT:
                        self.room.moveright()    
                    elif event.key == K_RIGHT:
                        self.room.moveleft()    
   
			# enter inventory screen
 
                    elif event.key == K_i:
                        flag = 0
		
        		pygame.key.set_repeat(1000,1000)
			while flag == 0:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
		    		    if event.key == K_ESCAPE:
					flag = 1
                                    elif event.key == K_LEFT:
                                        self.inventory.moveleft()
                                    elif event.key == K_RIGHT:
                                        self.inventory.moveright()
                                    elif event.key == K_z or event.key == K_x:
                                        self.inventoryitem = self.inventory.getitem(self.inventoryitem)
					self.taskbar.inventoryitem = self.inventoryitem
                                        flag = 1
                    			pygame.key.set_repeat(90,90)


                                self.inventory.draw(self.screen)
                                pygame.display.update()

			# enter spellbook (spell inventory) screen
 
                    elif event.key == K_o:
                        flag = 0
		
        		pygame.key.set_repeat(1000,1000)
			while flag == 0:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
		    		    if event.key == K_ESCAPE:
					flag = 1
                                    elif event.key == K_LEFT:
                                        self.spellbook.moveleft()
                                    elif event.key == K_RIGHT:
                                        self.spellbook.moveright()
                                    elif event.key == K_z or event.key == K_x:
                                        self.spellitem = self.spellbook.getitem(self.spellitem)
					self.taskbar.spellitem = self.spellitem
                                        flag = 1
                    			pygame.key.set_repeat(90,90)


                                self.spellbook.draw(self.screen)
                                pygame.display.update()

		# NOTE ce a collision returns 2 
            if self.room.collide(self.player) == 1 or self.player.hitpoints <= 0:
        	endingimage = pygame.image.load('./pics/endingscreen.bmp').convert()
        	while gameover == 0:
	            	pygame.display.update()
        	    	self.screen.blit(endingimage, (0,0))
            		for event in pygame.event.get():
                		if event.type == QUIT:
                    			return
                		elif event.type == KEYDOWN:
                    			gameover = 1
					return
                		if event.type == pygame.MOUSEBUTTONDOWN:
                    			gameover = 1
					return
            
       	    self.screen.blit(self.room.background, (self.room.relativex, self.room.relativey))

	    # draw gameobjects 
            for go in self.room.gameobjects:
	        if go != None:
		    go.update(self)
		    self.screen.blit(go.image, (go.x+self.room.relativex,go.y+self.room.relativey))  
	    # draw walls 
	    for w in self.room.northwalls:
		    self.screen.blit(w.image, (w.x+self.room.relativex,w.y+self.room.relativey))  
	    for w in self.room.eastwalls:
		    self.screen.blit(w.image, (w.x+self.room.relativex,w.y+self.room.relativey))  
	    for w in self.room.southwalls:
		    self.screen.blit(w.image, (w.x+self.room.relativex,w.y+self.room.relativey))  
	    for w in self.room.westwalls:
		    self.screen.blit(w.image, (w.x+self.room.relativex,w.y+self.room.relativey))  
	    # draw tileboxes
            for t in self.room.northtileboxes:
		 for j in range(0, t.ny):
                        for i in range(0,t.nx):
		 		if t.image != None:
		 			self.screen.blit(t.image, (t.x+t.w*i+self.room.relativex,t.y+t.h*j+self.room.relativey))  
            for t in self.room.easttileboxes:
		 for j in range(0, t.ny):
                        for i in range(0,t.nx):
		 		if t.image != None:
		 			self.screen.blit(t.image, (t.x+t.w*i+self.room.relativex,t.y+t.h*j+self.room.relativey))  
            for t in self.room.southtileboxes:
		 for j in range(0, t.ny):
                        for i in range(0,t.nx):
		 		if t.image != None:
		 			self.screen.blit(t.image, (t.x+t.w*i+self.room.relativex,t.y+t.h*j+self.room.relativey))  
            for t in self.room.westtileboxes:
		 for j in range(0, t.ny):
                        for i in range(0,t.nx):
		 		if t.image != None:
		 			self.screen.blit(t.image, (t.x+t.w*i+self.room.relativex,t.y+t.h*j+self.room.relativey))  
            for t in self.room.tileboxes:
		 for j in range(0, t.ny):
                        for i in range(0,t.nx):
		 		if t.image != None:
		 			self.screen.blit(t.image, (t.x+t.w*i+self.room.relativex,t.y+t.h*j+self.room.relativey))  

	    for e in self.room.exits:
                if hasattr(e, 'draw'):
		 	self.screen.blit(e.image, (e.x+self.room.relativex,e.y+self.room.relativey))  

	    # draw player
	    self.player.update()
	    if self.player.image:
    	    	self.screen.blit(self.player.image, (self.player.x,self.player.y))  

	    # Set player hitpoints in life bar

	    self.heartmeter.index = self.player.hitpoints
	    self.manameter.index = self.player.manapoints

            # fight for enemies
            # remove dead game objects

            for o in self.room.gameobjects:
                if o:
                    o.fight(self.room,self.player)
                    if o.hitpoints <= 0:
                        self.room.removeobject(o)

            self.taskbar.draw()
            self.heartmeter.draw(self.screen)
            self.manameter.draw(self.screen)

	    if self.talktext != "":
            	self.screen.blit(self.font.render(self.talktext, 13, (255,255,255)), (self.talker.x,self.talker.y-14))
            else:
		self.talker = None
 
            pygame.display.update()

	    # sleep for speed down
		
	    sleep(0.09)

	    # start next event loop

            self.screen.blit(blankimage, (0,0))

	    # room exit code which changes rooms
	
            roomnumber = self.room.exit(self)
            self.chooseroom(roomnumber,self.font)


    def sethitf(self, hitf):
        for i in self.room.gameobjects:
            i.hitf = hitf

    def setxy(self,xx,yy):
        self.x = xx
        self.y = yy

    def chooseroom(self, roomnumber,font):
        if (roomnumber == 0):
            return
        elif (roomnumber == 1):
            self.room = Maproom1(self.x,self.y)
        elif (roomnumber == 2):
            self.room = Maproom2(self.x,self.y)
        elif (roomnumber == 3):
            self.room = Maproom3(self.x,self.y)
        elif (roomnumber == 4):
            print "room 4 not yet implemented"
	    sys.exit(0)
 
if __name__ == "__main__":
    foo = Game()



