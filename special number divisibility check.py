a=[2,3,5,6,7,10]
count=0
for i in a:
        for j in a:
                if(i%j==0 and i!=j):
                        count +=1
                        print(i,j)
print("***",count,"***")
