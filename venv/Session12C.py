myProg = """
#include<iostream>
using namespace std;
int main(){
  cout<<"This is Awesome";
  return 0;
} 
"""

myProg = "** Be Exceptional **"


print(myProg)

# file = open("/Users/ishantkumar/Downloads/MyProg.cpp","w")

# w is write mode, which will overwrite the data
# with open("/Users/ishantkumar/Downloads/MyProg.cpp","w") as file:

# a is Append Mode
with open("/Users/ishantkumar/Downloads/MyProg.cpp","a") as file:

    print("Cursor is at: ",file.tell())

    # file.seek(10) # No Effect on appending

    file.write(myProg)
    print("==File Written==")

    print("Cursor is at: ", file.tell())
    file.close()

# Create Voice Based IDE to Code
# Use a Google Voice Recognition Library
# Generate .java and .cpp programs when user says: Create a Program to add 2 nos