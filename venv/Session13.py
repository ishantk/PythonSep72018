import mysql.connector

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def __str__(self):
        str = "{} belongs to {} and is priced for Rs {}".format(self.pid,self.name,self.price)
        return str


p1 = Product(1,"Apple iPhoneX",80000)
p2 = Product(201,"One Plus",30000)

# They must show hashCodes, but we have overrided __str__ so it will return the string as we have made
print(p1)
print(p2)

# Data in Objects is temporary. Lets Save it !!
# 1. Create SQL Query
# sql = "insert into Product values(null,'{}',{})".format(p2.name,p2.price)

# sql = "update product set name = '{}', price = {} where pid = {}".format(p1.name,p1.price,p1.pid)
# sql = "delete from Product where pid = {}".format(p1.pid)
sql = "select * from Product"
print(sql)

#2. Create Connection with the database
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="GW2018AI")

#3. Execute SQL Statement over the connection
cursor = con.cursor()
cursor.execute(sql)
# con.commit() # Transaction

"""
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
"""

for row in cursor:
    # print(row)
    print(row[0],row[1],row[2])


# print(p1.name,"Updated in DB")