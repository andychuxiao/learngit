import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

X1 = 10
Z1 = 10
X2 = 10
Z2 = 10
HOME_X = X2 + 2
HOME_Y = 10
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
    if inField > 3:
        mc.postToChat("Too slow!")
        mc.player.setPos(HOME_X, HOME_Y, HOME_Z)
