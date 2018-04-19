import queue
import threading
import time

def put_thread(q):
    while True:
        print('Starting thread...')
        time.sleep(10) # threat will wait for 10 seconds before putting value
        q.put(3)
        print('Put something')

myqueue = queue.Queue()
mythread = threading.Thread(target = put_thread, args = (myqueue,), daemon = True )
mythread.start()

myqueue.put(3)
print(myqueue.get())
print('Retrieved first element')

'''the execution will be blocked here and the program will wait for the thread to put something
in the queue. That something will be fetched by the following get statement.
'''
print(queue.get())
print('Finished')
