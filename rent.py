import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

X1 = -152
Z1 = -17
X2 = -143
Z2 = -8
HOME_X = X2 + 2
HOME_Y = 0
HOME_Z = Z2 + 2
rent = 0
inField = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x > X1 and pos.x < X2 and pos.z > Z1 and pos.z < Z2:
        rent = rent + 1
        mc.postToChat("You owe rent:" + str(rent))
        inField = inField + 1
    else:
        inField = 0
    if inField > 2:
        mc.postToChat("Too slow!")
        mc.player.setPos(HOME_X, HOME_Y, HOME_Z)
        rent = 0
