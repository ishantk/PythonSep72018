# Decorators in Python - OOPS

class Student:

    def __init__(self, roll, name, email):
        self.roll = roll
        self.name = name
        self.email = email

    @property
    def showStudent(self):
        return "{} belongs to {}".format(self.roll,self.name)

    @property
    def stuEmail(self):
        return "{} can be emailed at {}".format(self.name,self.email)

    @stuEmail.setter
    def stuEmail(self, email):
        if str(email).endswith(".com"):
            self.email = email
            print(">> email set")
        else:
            self.email = None
            print(">> email not set")

    @stuEmail.deleter
    def stuEmail(self):
        print(">> email deleted")
        self.email = None



s1 = Student(101,"John Watson","john.w@example.com")
print(s1.name)
print(s1.showStudent)
print(s1.email)

print("==========")
# s1.setEmail("john.watson@example")
s1.stuEmail = "john@example.com"
print(s1.stuEmail)

del s1.stuEmail
print(s1.stuEmail)
