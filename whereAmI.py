import mcpi.minecraft as minecraft
import time
#导入时间模块

mc = minecraft.Minecraft.create() 
#与MC建立连接

while True:
    time.sleep(1)
    #延时1s
    pos = mc.player.getTilePos()
    #获取玩家位置，y向上，z正南，x正东
    mc.postToChat(str(pos.x)+" "+str(pos.y)+" "+str(pos.z))
    #str（）字符串，字符串之间的连接用“+”;pos.x位置的x坐标