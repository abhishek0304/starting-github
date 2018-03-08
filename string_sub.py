import re
string = "she sells sea shells on the shore sea."
pattern = "sea"
replace = 'ocean'
print("*** SUB COMMAND ***")

print("                   ")


new_string = re.sub(pattern , replace, string, 1)
print(new_string)

