#Name Mangling -> __ (double underscore)
class Student:

    def __init__(self, roll, name, phone):
        self.roll = roll
        self._name = name
        self.__phone = phone

    def __show(self):
        print(self.roll,"belongs to",self._name,"and can be called at",self.__phone)


s1 = Student(101,"John","+91 99999 88888")
print(s1.roll)
print(s1._name)   #Protected, but not behaving as any access specification
#print(s1.__phone) #Behaving as Private,But isnt Private. Name Mangling Happens

print(s1.__dict__) # We will get __phone converted to _Student__phone
print(Student.__dict__)

print(s1._Student__phone)

s1._Student__show()