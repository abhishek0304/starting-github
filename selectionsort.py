print('''                 ''')
A = [1, 99, 12, 87, 23, 74, 35, 65, 41, 58]
print('Unsorted Array : ', A) 
print('''                 ''')

for i in range(len(A)):
     
    
    min = i
    for j in range(i+1, len(A)):
        if A[min] > A[j]:
            min = j
             
            
    A[i], A[min] = A[min], A[i]
    print("pass - ",i,A)
 
print('''                 ''')
print ("Sorted array : ", A)
