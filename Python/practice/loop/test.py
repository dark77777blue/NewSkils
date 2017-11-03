# encoding=utf-8
#########################################################################
#File Name: test.py
#Author: Don Hu
#Mail: hudeng@staff.sina.com.cn
#Create Time: 2017-10-18 16:42:42
#Last modified: 2017-10-18 16:49:34
#########################################################################
#!/usr/bin/env python




if __name__ == '__main__':
	print('begin...')

	names = ['Michael', 'Bob', 'Tracy']
	for name in names:
		print(name)

	print(list(range(5)))
	print(tuple(range(5)))

	print('#########################################################')

	sum = 0
	for x in range(101):
		sum = sum + x
	print(sum)

	for x in 'Hello, world':
		print(x)


