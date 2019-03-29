import random
start = input('請輸入起始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0 #猜的次數一開始為0
while True:
	num = input('請輸入一個數字: ')
	num = int(num)
	count = count + 1 #每猜一次就加一
	if num == r :
		print('恭喜!你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r :
		print('比答案大')
	elif num < r :
		print('比答案小')
	print('這是你猜的第', count, '次')