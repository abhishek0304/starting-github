theSeq=[11,99,22,88,33,77,44,66,55]
left=0
right=5
end=9
tmpArray=[1,2,3,4,5,6,7,8,9]
a = left
b = right
m = 0
while a < right and b < end :
    if theSeq[a] < theSeq[b] :
        tmpArray[m] = theSeq[a]
        a += 1
    else :
        tmpArray[m] = theSeq[b]
        b += 1
    m += 1
while a < right :
    tmpArray[m] = theSeq[a]
    a += 1
    m += 1
while b < end :
    tmpArray[m] = theSeq[b]
    b += 1
    m += 1
for i in range( end - left ) :
    theSeq[i+left] = tmpArray[i]
print(theSeq)
