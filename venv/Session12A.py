with open("Session12.py","r") as file:

    print("cursor is at:",file.tell())

    """
    data = file.read(50)
    print(data)

    print("cursor is at:", file.tell())

    data = file.read(100)
    print(data)
    print("cursor is at:", file.tell())
    """

    file.seek(100)
    print("cursor is at:", file.tell())

    data = file.read(100)
    print(data)
    print("cursor is at:", file.tell())


print("Game Over")



