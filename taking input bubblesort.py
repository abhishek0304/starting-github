print('''                 ''')

A = []
n = int(input('Enter how many elements you want: '))
for i in range(0, n):
    x = input('Enter the numbers into the array: ')
    A.append(x)
print(A)

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
