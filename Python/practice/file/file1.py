# encoding=utf-8
#########################################################################
#File Name: file1.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 15:40:32
#Last modified: 2017-10-30 16:10:40
#########################################################################
#!/usr/bin/env python




if __name__ == '__main__':
	with open('./abc.txt', 'rb') as f:
		#print(f.read())
		'''
		for line in f.readlines():
			print(line.strip())
		'''

		'''
		for buf in f:
			print(buf.strip())
		'''

		data = f.read(10)
		while 1:
			print(data)
			print(type(data))
			data = f.read(10)
			if not data:
				break









