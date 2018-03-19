a = []
for i in range(100):
    n=int(input("enter input array"))
    if(n==-1): break
    a.append(n)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            [a[i],a[j]]=[a[j],a[i]]
    print("soretd array:",a)