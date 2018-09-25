class Parent:

    def purchaseBike(self):
        print("Lets buy Bajaj Pulsar")


class Child(Parent):

    # Overriding
    def purchaseBike(self):
        print("Lets buy Royal Enfield")


    pass


print(Parent.__dict__)
print(Child.__dict__)

ch = Child()
ch.purchaseBike()