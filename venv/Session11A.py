# Run Time Polymorphism

class Cab:
    def bookCab(self):
        print("Cab is Booked !! Arriving Soon !!")

class UberGo(Cab):
    def bookCab(self):
        print("UberGo is Booked !! Arriving Soon !!")

class UberX(Cab):
    def bookCab(self):
        print("UberX is Booked !! Arriving Soon !!")

class UberMoto(Cab):
    def bookCab(self):
        print("UberMoto is Booked !! Arriving Soon !!")

c = Cab()
c.bookCab()
print("------------")
c = UberGo()
c.bookCab()

print("------------")
c = UberX()
c.bookCab()
print("------------")
c = UberMoto()
c.bookCab()

class Person:
    pass

class Employee:
    pass

ref = Person()
ref = Employee()