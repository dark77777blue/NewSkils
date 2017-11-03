# encoding=utf-8
#########################################################################
#File Name: queue_t.py
#Author: Don Hu
#Mail: hudeng@didichuxing.com
#Create Time: 2017-11-02 15:53:23
#Last modified: 2017-11-02 16:43:28
#########################################################################
#!/usr/bin/env python

from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))

	pw.start()
	pr.start()

	pw.join()

	pr.terminate()
	





