# playerPos.py by George Tuli.
# This program will find a player's position and post it to the in-game chat.

# Import a couple of external libraries so the program can interface with Minecraft.
import mcpi.minecraft as minecraft 
import time

# Setup the API.
mc = minecraft.Minecraft.create("localhost")

# The main loop, which will run indefinitely.
while True:
	# Wait for 1 second before each position reading.
	time.sleep(1.0)
	# Get the player's position (x,y,z) and set it to the variable 'pos'.
	pos = mc.player.getPos()
	# Output the player's position to the terminal.
	print pos.x, pos.y, pos.z															
	# Output the player's position to the in-game chat.
	mc.postToChat(pos)
