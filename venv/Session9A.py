class Product:
    def __init__(self, pid, name, brand, price):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price

    def showProductDetails(self):
        print("{} belongs to {} and is priced at {}".format(self.pid,self.name,self.price))


class LEDTV(Product): # IS-A Relation
    pass


class Mobile(Product):
    def __init__(self, pid, name, brand, price, os, ram):
        super().__init__(pid,name,brand,price) #Parent's Constructor Execution
        self.os = os
        self.ram = ram

    def showProductDetails(self):
        print("{} belongs to {} and is priced at {}".format(self.pid, self.name, self.price))
        print("{} runs on {} with memory {} GB".format(self.name,self.os,self.ram))


    # def showMobileDetails(self):
    #     print(self.pid)
    #     print("Mobile Phone runs on {}  with memory of {} GB".format(self.os, self.ram))


# p1 = Product(101,"Learning Python","Wiley",300)
# p1.showProductDetails()

# print(Product.__dict__)
# print(LEDTV.__dict__)
#
# led = LEDTV(101,"Learning Python","Wiley",300)
# print(led.__dict__)
# led.showProductDetails()
#
# LEDTV.showProductDetails(led)

mob = Mobile(1001,"iPhone XS","Apple",80000,"iOS",4)
print(mob.__dict__)

mob.showProductDetails()
# mob.showMobileDetails()

