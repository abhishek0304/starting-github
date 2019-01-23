a=[1,2,3,4,6,7,8,9,11,12,13,14,15]
target=9
k=0
low=0
high=len(a)-1
while(low<=high):
    mid=(high+low)//2
    if(a[mid]==target):
        print("element found:",a[mid])
        k=1

        break
    elif(target<a[mid]):
        high=mid-1
    else:
        low=mid+1
if(k==0):
    print("element not found")
