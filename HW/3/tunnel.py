# tunnel.py by George Tuli.
# This program will allow the player to easily mine through hills and mountains (and snow) without the use of tools.

# Import a couple of external libraries so the program can interface with Minecraft.
import mcpi.minecraft as minecraft 
import time
from mcpi.block import *

# Setup the API.
mc = minecraft.Minecraft.create("localhost")

# Set a diamond block for a point of reference.
pos = mc.player.getPos()
mc.setBlock(pos.x+1, pos.y+1, pos.z, WOOD_PLANKS)

# Give the player instrutions.
mc.postToChat("Face the wooden planks, then walk forward.")

time.sleep(2)

# The main loop, which will run indefinitely.
while True:
	# Get the player's position (x,y,z) and set it to the variable 'pos'.
	pos = mc.player.getPos()
	
	# Check if the block in front of the player is not air.
	block = mc.getBlock(pos.x+1, pos.y, pos.z)
	if block != AIR or block != WATER:
		mc.setBlocks(pos.x+1, pos.y, pos.z, pos.x+1, pos.y+1, pos.z, AIR)
