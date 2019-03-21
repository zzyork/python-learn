import math 
def quadratic(a,b,c):
	if a == 0:
		raise TypeError('a不能为0')
	if not isinstance(a,(int,float)) or  not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
		raise TypeError('Bad operand type')
	delta = math.pow(b,2) - 4*a*c
	if delta < 0:
		return '无实根'
	x1= (math.sqrt(delta)-b)/(2*a)
	x2=-(math.sqrt(delta)+b)/(2*a)
	return x1,x2
	
a = int(input("请输入a的值：\n"))
b = int(input("请输入b的值：\n"))
c = int(input("请输入c的值：\n"))

print(quadratic(a,b,c))
