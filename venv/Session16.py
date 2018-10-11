import threading
import time

lock = threading.Lock()

class Printer:
    def printNotes(self, fromPage, toPage):
        lock.acquire()
        for i in range(fromPage, toPage):
            print("Printing Page#",i)
            time.sleep(.5)
        lock.release()


class User(threading.Thread):

    def __init__(self, name, printer, fromPage, toPage):
        # If we create constructor in child class and parent class is Thread, we must call Parents' constructor
        threading.Thread.__init__(self)
        self.name = name
        self.printer = printer
        self.fromPage = fromPage
        self.toPage = toPage

    def run(self):
        print("Printing Notes for",self.name)
        self.printer.printNotes(self.fromPage,self.toPage)

printer = Printer()

user1 = User("John",printer, 5, 18)
user2 = User("Fionna",printer, 70, 90)
user3 = User("Harry",printer, 101, 130)

user1.start()
user2.start()
user3.start()


