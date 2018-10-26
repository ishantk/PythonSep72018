import re

quote = "Search the candle rather than cursing the darkness"

# String Matching
# result = re.match(r"the",quote)
result = re.match(r"Search",quote)
print(result)
print(type(result))
print(result.start())
print(result.end())

print("*********************")
# String Searching
result = re.search(r"the",quote)
print(result)
print(result.group(0))

print("*********************")
# String Finding
result = re.findall(r"the",quote)
print(result)

print("*********************")
# String Splitting
# result = re.split(r" ",quote)
result = re.split(r"the",quote)
print(result)
print(type(result))

print("*********************")
# String Substitution
result = re.sub(r"the","a",quote)
print(result)

# Regular Expressions with Patterns
print("*********************")
pattern = re.compile("the")
print(pattern)
print(type(pattern))
result = pattern.findall(quote)
print(result)