# By Default each and Every Class is inherited from object class
class Student:
    def __init__(self, roll, name, address):
        self.roll = roll
        self.name = name
        self.address = address

    def getDetails(self):
        details = "{} belongs to {} and lives in {}".format(self.roll,self.name,self.address)
        return details

    # ReDefining the Parent(object) Method in the Child(Student)
    #Overriding
    def __str__(self):
        # print(super().__str__())
        details = "{} belongs to {} and lives in {}".format(self.roll, self.name, self.address)
        return details


def executeCode():
    s1 = Student(101,"John","Redwood Shores")
    print(s1)
    print(s1.__str__())
    print(s1.getDetails())

    print(type(s1))


    names = ["John","Jennie","Jim","Jack","Joe"]
    print(names)

    print(type(names))

    a = 10
    print(type(a))
    print(a)
    print(a.__str__())

# executeCode()