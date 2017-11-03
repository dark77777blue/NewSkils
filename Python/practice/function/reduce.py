# encoding=utf-8
#########################################################################
#File Name: reduce.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-21 18:37:05
#Last modified: 2017-10-21 18:45:42
#########################################################################
#!/usr/bin/env python


from functools import reduce

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))






if __name__ == '__main__':
	print(str2int('12345'))





