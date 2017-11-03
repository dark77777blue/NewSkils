# encoding=utf-8
#########################################################################
#File Name: test1.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 13:28:17
#Last modified: 2017-10-30 13:29:26
#########################################################################
#!/usr/bin/env python


def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')


if __name__ == '__main__':
	main()
	

