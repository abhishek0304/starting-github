import re
pattern = r"[a-zA-Z]+ \d+"

print("*** FINDITER COMMAND ***")
matches = re.finditer(pattern, "LXI 2003, VXI 2012, VDI 2019, MARUSTI SUZUKI CARS AVAILBALE WITH US ")
for match in matches:
    print("                     ")
    print(match)
    print("Match found at starting index : ",match.start())
    print("Match found at ending index : ",match.end())
    print("Match found at starting and ending index : ",match.span())
    print("                     ")


print("*** FINDALL COMMAND ***")
matches = re.findall(pattern, "LXI 2003, VXI 2012, VDI 2019, MARUSTI SUZUKI CARS AVAILBALE WITH US ")
for match in matches:
    print("                     ")
    print(match, end = " ")
    print("                     ")
