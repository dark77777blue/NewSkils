# encoding=utf-8
#########################################################################
#File Name: isinstance.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-21 16:43:17
#Last modified: 2017-10-21 17:17:03
#########################################################################
#!/usr/bin/env python

from collections import Iterable
from collections import Iterator








if __name__ == '__main__':

	b = isinstance([], Iterable)
	print(b)
	b = isinstance([], Iterator)
	print(b)





