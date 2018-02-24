score=float(input("Enter the score"))
try:
    score<0.0
    score>1.0
except ValueError:
    print("its not a valid input")

if(score>=0.9):
    print("A")
elif(score>=0.8):
    print("B")
elif(score>=0.7):
    print("C")
elif(score>=0.6):
    print("D")
if(score<0.6):
    print("F")
    