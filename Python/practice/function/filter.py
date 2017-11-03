# encoding=utf-8
#########################################################################
#File Name: filter.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-23 07:58:44
#Last modified: 2017-10-23 08:02:06
#########################################################################
#!/usr/bin/env python


def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

