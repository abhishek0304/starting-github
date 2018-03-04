print('''                 ''')
A = [1, 99, 12, 87, 23, 74, 35, 65, 41, 58]
print('Unsorted Array : ', A) 
print('''                 ''')

for i in range(len(A)):
     
    
    
    for j in range(0, len(A)-i-1):
        if A[j] > A[j+1]:
            min = A[j]
            A[j]=A[j+1]
            A[j+1]=min
            
    
    print("pass - ",i,A)
 
print('''                 ''')
print ("Sorted array : ", A)
