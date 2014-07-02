# playerPos.py by George Tuli.
# This program will find a player's position and post it to the in-game chat.

# Import a couple of external libraries so the program can interface with Minecraft.
import mcpi.minecraft as minecraft 
import time
from mcpi.block import *

# Setup the API.
mc = minecraft.Minecraft.create("localhost")

# The main loop, which will run indefinitely.
while True:
	# Get the player's position (x,y,z) and set it to the variable 'pos'.
	pos = mc.player.getPos()
	
	# Check if the block in front of the player is not air.
	if pos.x+1 not AIR:
		mc.setBlocks(pos.x+1, pos.y, pos.z, pos.x+1, pos.y+1, pos.z, AIR)
	time.sleep(0.1)
