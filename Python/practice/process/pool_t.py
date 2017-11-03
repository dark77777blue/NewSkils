# encoding=utf-8
#########################################################################
#File Name: pool.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-10-31 14:40:44
#Last modified: 2017-11-02 15:19:41
#########################################################################
#!/usr/bin/env python


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')





