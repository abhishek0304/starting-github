string = "sun rises in the east east"
str = 'east'
print(string.capitalize())

print(string.center(30, '*'))

print(string.count(str,0,len(string)))
print(string.endswith("ast",0, len(string)))
print(string.startswith("su",0, len(string)))
print(string.find("in",0, len(string)))

print(string.rfind("rises",0, len(string)))
print(string.rindex("in",0, len(string)))