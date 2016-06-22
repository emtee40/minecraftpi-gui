#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minecraft entry gui
#  
#  Copyright 2014 Paul Sutton <zleap@zleap.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,+


#  MA 02110-1301, USA.
#  
#  
# note: I have commented out the lines that call up api functions so that
# I could test on a desktop

import Tkinter # note use of caps
import sys
from mcpi import minecraft as minecraft # uncomment for program to work or comment to develop on a desktop
import mcpi.block as block
from Tkinter import *
import tkMessageBox as box
from time import sleep


window = Tk()
window.title("Minecraft Pi GUI")
window.geometry("640x300") #wxh
window.resizable(0,0)



mc = minecraft.Minecraft.create() # uncomment for program to work or comment to develop on a desktop
getPos = mc.player.getPos()
#mc.player.setPos(playerPos.x, playerPos.y + 50, playerPos.z)


def mcmessage():
	mcin = mctxtVar.get()
	#print mctxtVar.get()
	mc.postToChat(mctxtVar.get()) # uncomment for program to work or comment to develop on a desktop

def gotopos():
	mcx = int(mcxtext.get())
	mcy = int(mcytext.get())
	mcz = int(mcztext.get())
	print mcx,mcy,mcz
	mc.player.setPos(mcppos.mcx, mcppos.mcy, mcppos.mcz) # uncomment for program to work or comment to develop on a desktop

def play_position():
	x, y, z = mc.player.getPos()
	print(x,y,z)
	pos = x, y, z
	mcppos.delete(0, END)
	mcppos.insert(END, pos)
	#mcppos
	
#def testbutton():
#	print "test"
def flatworld():
	print("flat world")
	MINX = -5
	MAXX = 5
	MINZ = -5
	MAXZ = 5
	MINY = -5
	MAXY = 5

	mc.player.setPos(0,0,MAXZ+25)

	for y in range(MAXY, MINY, -1):
		mc.setBlocks(MINX, y, MINZ, MAXX, y, MAXZ, block.TNT.id,1)
		sleep(1)
		print y

	mc.setBlocks(MINX, MINY, MINZ, MAXX, MINY, MAXZ, block.GRASS.id)


#define buttons
btn1 = Button( window, text ='PostToChat', command=mcmessage)
btn2 = Button( window, text ='GoToPos', command=gotopos)
btn3 = Button( window, text ='Exit', command=exit )
btn4 = Button( window, text ='Player_Position', command=play_position )
btn5 = Button( window, text ='Make world flat', command=flatworld )

#Place buttons

btn1.grid(row = 1, column = 4, padx = 5, pady = 5)
btn2.grid(row = 4, column = 4, padx = 5, pady = 5)
btn3.grid(row = 7, column = 4, padx = 5, pady = 5) #exit
btn4.grid(row = 5, column = 4, padx = 5, pady = 5) # player position
btn5.grid(row = 6, column = 4, padx = 5, pady = 5)

#define and place labels

#define labels - cannot share same name as function
mcmesg = Label(window, text="MC_Message: ")
mcxpos = Label(window, text="x_pos ")
mcypos = Label(window, text="y_pos: ")
mczpos = Label(window, text="z_pos: ")
plypos = Label(window, text="player_position ")

#place labels
mcmesg.grid(row = 1, column = 1, padx = 5, pady = 5)

mcxpos.grid(row = 3, column = 1, padx = 5, pady = 5)
mcypos.grid(row = 3, column = 2, padx = 5, pady = 5)
mczpos.grid(row = 3, column = 3, padx = 5, pady = 5)
plypos.grid(row = 5, column = 1, padx = 5, pady = 5)


#create text entry file name boxes

#define entry box 1

mctxtVar = StringVar() #message text input box
mcmesgtext = Entry(window, textvariable=mctxtVar)

mcxtextVar = StringVar()
mcxtext = Entry(window, textvariable=mcxtextVar)

mcytextVar = StringVar()
mcytext = Entry(window, textvariable=mcytextVar)

mcztextVar = StringVar()
mcztext = Entry(window, textvariable=mcztextVar)

mcpposVar = StringVar()
mcppos = Entry(window, textvariable=mcpposVar)



#place entry boxes

mcmesgtext.grid(row = 1, column = 2,) # text for post to chat

mcxtext.grid(row = 4, column = 1, padx = 2, pady = 2) #xpos
mcytext.grid(row = 4, column = 2, padx = 2, pady = 2) #ypos
mcztext.grid(row = 4, column = 3, padx = 2, pady = 2) #zpos
mcppos.grid(row = 5, column = 2, padx = 2, pady = 2) #zpos

window.mainloop()
	

