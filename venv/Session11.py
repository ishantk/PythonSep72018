"""
    Single Level
    P
    |
    C

    Multi Level
    P
    |
    C
    |
    GC

    Hierarchy
    P
    |
 C1   C2

    Multiple
    P1    P2
       |
       C

    Hybrid
        Fusion of all above



"""

class User:
    def __init__(self, name, phone, email, occupation):
        self.name = name
        self.phone = phone
        self.email = email
        self.occupation = occupation

class Person:
    def __init__(self, age, gender, address):
        self.age = age
        self.gender = gender
        self.address = address

class Driver(User,Person):
    def __init__(self, licenseNum):
        super().__init__("John","+91 99999 88888","john@example.com","Software Engr")
        # super().__init__(30, "Male", "Redwood Shores")
        # Person.__init__() :)
        self.licenseNum = licenseNum

d1 = Driver(1001)
print(d1.__dict__)
print(Driver.__dict__)