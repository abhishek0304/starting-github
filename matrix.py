list1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
list2 = [[9,8,7],[6,5,4],[3,2,1]]
print(list1)
print(list2)
print("*** MATRIX ADDITION ***")
some = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list1)):
    for j in range(len(list2)):
        some[i][j] = list1[i][j] + list2[i][j]
print(some)
print("*** MATRIX SUBSTRACTION ***")
some = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list1)):
    for j in range(len(list2)):
        some[i][j] = list1[i][j] - list2[i][j]

        
print(some)
print("*** MATRIX MULTIPLICATION ***")
some = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(list1)):
    for j in range(len(list2)):
        for k in range(len(list2)):
            some[i][j] = some[i][j] + (list1[i][k] * list2[k][j])
        
print(some)