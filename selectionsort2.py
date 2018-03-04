print('''                 ''')
A = [1, 99, 12, 87, 23, 74, 35, 65, 41, 58]
print('Unsorted Array : ', A) 
print('''                 ''')

for i in range(len(A)):
     
    
    
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            min = A[i]
            A[i]=A[j]
            A[j]=min
            
    
    print("pass - ",i,A)
 
print('''                 ''')
print ("Sorted array : ", A)