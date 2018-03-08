import re
string = "she sells sea shells on the shore."
pattern1 = "sells"

print("*** MATCH COMMAND ***")
if re.match(pattern1 , string):
    print('pattern found')
else:
    print('pattern not found')

print("*** SEARCH COMMAND ***")

if re.search(pattern1 , string):
    print('pattern found')
else:
    print('pattern not found')