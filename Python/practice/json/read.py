# encoding=utf-8
#########################################################################
#File Name: read.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 13:50:04
#Last modified: 2017-10-31 13:53:04
#########################################################################
#!/usr/bin/env python

import json



if __name__ == '__main__':
	with open('./dump.txt', 'r') as f:
		d = json.load(f)
		print(d)





