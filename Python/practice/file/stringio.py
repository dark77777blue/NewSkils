# encoding=utf-8
#########################################################################
#File Name: stringio.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-30 16:12:43
#Last modified: 2017-10-30 16:14:28
#########################################################################
#!/usr/bin/env python

from io import StringIO

if __name__ == '__main__':
	f = StringIO()
	f.write('hello')
	f.write(' ')
	f.write('world!') 

	print(f.getvalue())
