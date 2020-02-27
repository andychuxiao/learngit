# 先保存代码，然后才能编译
import mcpi.minecraft as mc
# 给引入的mcpi.minecraft起个别名叫mc
link = mc.Minecraft.create()
# 建立python程序与MC的连接
link.postToChat("hello world")
# 在MC聊天窗口打印欢迎信息
