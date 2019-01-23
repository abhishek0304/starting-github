x=int(input("ENter 5 ruppees coins available"))
y=int(input("ENter 1 ruppees coins available"))
z=int(input("ENter amount to be paid"))

a=z//5
b=z-(5*a)
if(x<a or y<b):
        print("-1")
else:
        print(min(x,a))
        print(min(y,b))







