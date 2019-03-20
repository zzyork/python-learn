dec = int(input("请输入一个十进制数："))  #输入一个十进制数并将其转化成int类型
hex = hex(dec)                          #将这个额十进制数转换成十六进制
print("转换为十六进制为：" + hex)


def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
x = (-9)
print(my_abs(x))

import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print (x,y)
