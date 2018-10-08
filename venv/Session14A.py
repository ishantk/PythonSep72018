class Student:
    def __init__(self, roll, name, email, gender, address):
        self.roll = roll
        self.name = name
        self.email = email
        self.gender = gender
        self.address = address


def saveStudentInDB(student):
    pass


def showAddStudentGUI():
    pass

s1 = Student(0,"NA","NA","NA","NA")

# A GUI will pop up, asking details of student roll, name, email, gender and address
# On Click of AddButton on your GUI, saveStudentInDB should be executed
# Use mysql.connector to save data in DB

showAddStudentGUI()

# Execute this file and make sure Student Object will be saved in DB
