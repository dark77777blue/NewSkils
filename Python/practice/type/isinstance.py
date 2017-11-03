# encoding=utf-8
#########################################################################
#File Name: isinstance.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-25 20:16:54
#Last modified: 2017-10-26 11:27:39
#########################################################################
#!/usr/bin/env python






if __name__ == '__main__':
	print(type(b'abc'))

	print(isinstance([1, 2, 3], (list, tuple)))
	print(isinstance((1, 2, 3), (list, tuple)))

	#print(dir('ABC'))
	


	print('ABC'.__len__())
	print(len('ABC'))



