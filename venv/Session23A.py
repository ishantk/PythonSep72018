import re

quote = "Work hard Get Luckier"
result = re.findall(r".",quote)
print(result)
# . -> represents a character

print("===============")
result = re.findall(r"\w",quote)
print(result)
# w -> represents all characters other than spaces

print("===============")
result = re.findall(r"\w*",quote)
print(result)

print("===============")
result = re.findall(r"\w+",quote)
print(result)

# Validate the below email, password and phone !!
email = "john@example.com"
password = "john123"
phone = "+91 99999 88888"

# Split a CSV File after reading, using regular expressions
# Using Regular Expression check if csv file is correct or not