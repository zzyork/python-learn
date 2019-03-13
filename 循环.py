
#while循环输出列表中的各个元素
L = ['Bart','Lisa','Adam']
n = 0		
while n < 3:		#设置循环条件
	print("Hello! " + L[n] + " !")	#利用n值输出句子和数组中的元素
	n = n + 1

#for循环输出各元素
L = ['Bart','Lisa','Adam']
for x in range(3):      #让x从0-2开始递增，直到x>2停止
	print("Hello! " + L[x] + " !")
