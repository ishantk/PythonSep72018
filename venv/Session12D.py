import os
import glob

# path = "/Users/ishantkumar/Downloads/MyProg.cpp"
path = "/Users/ishantkumar/Downloads"
flag = os.path.exists(path)
print("Is Path Existing? ",flag)

print("Is it a File? ",os.path.isfile(path))
print("Is it a Directory? ",os.path.isdir(path))

if os.path.isdir(path):
    data = os.listdir(path)
    print(type(data))

    for file in data:
        if file.endswith(".csv"):
            print(file)

print(os.path.getsize(path))

print("==========")

files = glob.glob("*.py")
# print(files)
for file in files:
    print(file)

# Create a File Manager