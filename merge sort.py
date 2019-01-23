def mergeSort(a):

    if len(a)>1:
        mid=len(a)//2
        lefthalf=a[:mid]
        righthalf=a[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)


        i=j=k=0
        
        while (i<len(lefthalf)) and (j<len(righthalf)):

            if(lefthalf[i]<righthalf[j]):
                a[k]=lefthalf[i]
                i +=1
            else:
                a[k]=righthalf[j]
                j +=1
            k +=1
            
        while (i<len(lefthalf)):
                a[k]=lefthalf[i]
                i +=1
                k +=1
        while (j<len(righthalf)):
                a[k]=righthalf[j]
                j +=1
                k +=1

a=[11,99,22,88,33,77,44,66,55,1,9,43,12,98,65,34,56,32,27]
mergeSort(a)
print(a)
                

        

    
