import threading
import time

class MyThread(threading.Thread):

    def run(self):
        for i  in range(1,11):
            time.sleep(1)
            print("MyThread",i)


mRef = MyThread()
mRef.start()

# Logic : To Create a timer !!
# Input on GUI
# Output also on GUI
