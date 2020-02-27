import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def buildbridge():
    pos = mc.player.getTilePos()
    playerFoot = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if playerFoot == block.WATER_FLOWING or playerFoot == block.WATER_STATIONARY:
        mc.setBlock(pos.x , pos.y - 1,pos.z,block.GLASS.id)

while True:
    buildbridge()