0#!/usr/bin/env python
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
	gotox = gotoxtextVar.get()
	gotoy = gotoytextVar.get()
	gotoz = gotoztextVar.get()
	print gotox,gotoy,gotoz
	mc.player.setPos(gotox, gotoy, gotoz) 
	#clean up and delete old data in boxes
	mcxtext.delete(0, END)
	mcytext.delete(0, END)
	mcztext.delete(0, END)
		
	#insert new player position
	
	x, y, z = mc.player.getPos()
	pos = x, y, z
	
	mcxtext.insert(END, x)
	mcytext.insert(END, y)
	mcztext.insert(END, z)
	
def play_position():
	#clean up
	mcxtext.delete(0, END)
	mcytext.delete(0, END)
	mcztext.delete(0, END)
	
	#insert new player position data
	x, y, z = mc.player.getPos()
	pos = x, y, z
	
	mcppos.delete(0, END)
	mcxtext.insert(END, x)
	mcytext.insert(END, y)
	mcztext.insert(END, z)
	

	
#def testbutton():
#	print "test"
def flatworld():
	print("flat world")
	MINX = -100
	MAXX = 100
	MINZ = -100
	MAXZ = 100
	MINY = -60
	MAXY = 64

	mc.player.setPos(0,0,0)

	for y in range(MAXY, MINY, -1):
		mc.setBlocks(MINX, y, MINZ, MAXX, y, MAXZ, block.AIR.id)
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
btn2.grid(row = 6, column = 4, padx = 5, pady = 5) #goto

btn4.grid(row = 4, column = 4, padx = 5, pady = 5) # player position
btn5.grid(row = 8, column = 4, padx = 5, pady = 5) #flat world
btn3.grid(row = 9, column = 4, padx = 5, pady = 5) #exit
#define and place labels

#define labels - cannot share same name as function
mcmesg = Label(window, text="MC_Message: ")
mcxpos = Label(window, text="x_pos ")
mcypos = Label(window, text="y_pos: ")
mczpos = Label(window, text="z_pos: ")
plypos = Label(window, text="player_position ")
gotox = Label(window, text="goto x_pos ")
gotoy = Label(window, text="goto y_pos: ")
gotoz = Label(window, text="goto z_pos: ")

#place labels
mcmesg.grid(row = 1, column = 1, padx = 5, pady = 5)
#place lables for player pos
mcxpos.grid(row = 3, column = 1, padx = 5, pady = 5)
mcypos.grid(row = 3, column = 2, padx = 5, pady = 5)
mczpos.grid(row = 3, column = 3, padx = 5, pady = 5)
#place labels for goto pos
gotox.grid(row = 5, column = 1, padx = 5, pady = 5)
gotoy.grid(row = 5, column = 2, padx = 5, pady = 5)
gotoz.grid(row = 5, column = 3, padx = 5, pady = 5)

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

#define entry boxes for goto position

gotoxtextVar = StringVar()
gotoxtext = Entry(window, textvariable=gotoxtextVar)

gotoytextVar = StringVar()
gotoytext = Entry(window, textvariable=gotoytextVar)

gotoztextVar = StringVar()
gotoztext = Entry(window, textvariable=gotoztextVar)


#place entry boxes

mcmesgtext.grid(row = 1, column = 2,) # text for post to chat

mcxtext.grid(row = 4, column = 1, padx = 2, pady = 2) #xpos
mcytext.grid(row = 4, column = 2, padx = 2, pady = 2) #ypos
mcztext.grid(row = 4, column = 3, padx = 2, pady = 2) #zpos
#mcppos.grid(row = 5, column = 2, padx = 2, pady = 2) #zpos

#place entry boxes for goto position

gotoxtext.grid(row = 6, column = 1, padx = 2, pady = 2) #xpos
gotoytext.grid(row = 6, column = 2, padx = 2, pady = 2) #ypos
gotoztext.grid(row = 6, column = 3, padx = 2, pady = 2) #zpos


window.mainloop()
	

