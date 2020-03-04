import mcpi.minecraft as minecraft

import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

for i in range(0,20,2):
    mc.setBlock(pos.x+1,pos.y+i,pos.z+1,block.REDSTONE_BLOCK)