# house.py by George Tuli.
# This program builds a simple house automatically.

# Import a couple of external libraries to interface with Minecraft.
import mcpi.minecraft as minecraft 
from mcpi.block import * 

# Setup the API locally.
mc = minecraft.Minecraft.create("localhost") 

# Get the player's position.
pos = mc.player.getTilePos()

# Clear enough space to build the house.
mc.setBlocks(pos.x-2, pos.y, pos.z-2, pos.x+2, pos.y+8, pos.z+8, AIR)

# Reposition the player, so they can watch the house being built.
mc.player.setTilePos(pos.x+1, pos.y, pos.z-2)

# Build the first walls.
mc.setBlocks(pos.x-1, pos.y, pos.z, pos.x-1, pos.y+4, pos.z+6, BRICK_BLOCK)
mc.setBlocks(pos.x-1, pos.y, pos.z+6, pos.x+3, pos.y+4, pos.z+6, BRICK_BLOCK)
mc.setBlocks(pos.x+3, pos.y, pos.z+6, pos.x+3, pos.y+4, pos.z, BRICK_BLOCK)
mc.setBlocks(pos.x-1, pos.y, pos.z, pos.x+3, pos.y+4, pos.z, BRICK_BLOCK)

# Build the floor and ceiling.
mc.setBlocks(pos.x-1, pos.y-1, pos.z, pos.x+3, pos.y-1, pos.z+6, WOOL)
mc.setBlocks(pos.x-1, pos.y+5, pos.z, pos.x+3, pos.y+5, pos.z+6, WOOL)

# Build the roof.
mc.setBlocks(pos.x+3, pos.y+5, pos.z, pos.x+3, pos.y+5, pos.z+6, WOOD_PLANKS)
mc.setBlocks(pos.x+2, pos.y+6, pos.z, pos.x+2, pos.y+6, pos.z+6, WOOD_PLANKS)
mc.setBlocks(pos.x+1, pos.y+7, pos.z, pos.x+1, pos.y+7, pos.z+6, WOOD_PLANKS)
mc.setBlocks(pos.x, pos.y+6, pos.z, pos.x, pos.y+6, pos.z+6, WOOD_PLANKS)
mc.setBlocks(pos.x-1, pos.y+5, pos.z, pos.x-1, pos.y+5, pos.z+6, WOOD_PLANKS)
mc.setBlocks(pos.x, pos.y+5, pos.z, pos.x+2, pos.y+5, pos.z, COBBLESTONE)
mc.setBlock(pos.x+1, pos.y+6, pos.z, COBBLESTONE)
mc.setBlocks(pos.x, pos.y+5, pos.z+6, pos.x+2, pos.y+5, pos.z+6, COBBLESTONE)
mc.setBlock(pos.x+1, pos.y+6, pos.z+6, COBBLESTONE)

# Make a door and window.
mc.setBlocks(pos.x+1, pos.y, pos.z, pos.x+1, pos.y+1, pos.z, DOOR_WOOD)
mc.setBlocks(pos.x+1, pos.y+1, pos.z+6, pos.x+1, pos.y+3, pos.z+6, GLASS_PANE)

# Add some furniture.
mc.setBlocks(pos.x+2, pos.y, pos.z+4, pos.x+2, pos.y, pos.z+5, BED)
mc.setBlock(pos.x, pos.y, pos.z+5, CHEST)
mc.setBlock(pos.x+1, pos.y+3, pos.z+1, TORCH)
