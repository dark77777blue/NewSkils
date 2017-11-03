# encoding=utf-8
#########################################################################
#File Name: test1.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 13:33:54
#Last modified: 2017-10-31 13:35:01
#########################################################################
#!/usr/bin/env python

import pickle




if __name__ == '__main__':
	with open('./dump.txt', 'rb') as f:
		d = pickle.load(f)
		print(d)




