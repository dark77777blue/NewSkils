# encoding=utf-8
#########################################################################
#File Name: test3.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 13:53:53
#Last modified: 2017-10-30 13:54:58
#########################################################################
#!/usr/bin/env python


def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	foo('0')




if __name__ == '__main__':
	main()




