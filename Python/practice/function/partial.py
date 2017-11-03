# encoding=utf-8
#########################################################################
#File Name: partial.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 14:39:31
#Last modified: 2017-10-23 15:33:10
#########################################################################
#!/usr/bin/env python

import functools

int2 = functools.partial(int, base=2)





if __name__ == '__main__':
	pass
	print(int2('1100'))

