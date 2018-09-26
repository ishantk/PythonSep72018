class Employee:

    def sayHello(self):
        return "Hello from Employee"

    def __repr__(self):
        print("Wow !!")



def executeCode():
    e = Employee()
    print(e.sayHello())


