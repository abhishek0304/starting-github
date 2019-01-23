def countSort(arr): 

	output = [0 for i in range(64)] 
 
	count = [0 for i in range(64)] 

	ans = ["" for _ in arr] 

	for i in arr: 
		count[ord(i)] += 1
 
	for i in range(64): 
		count[i] += count[i-1] 

	for i in range(len(arr)): 
		output[count[ord(arr[i])]-1] = arr[i] 
		count[ord(arr[i])] -= 1

	for i in range(len(arr)): 
		ans[i] = output[i] 
	return ans 


arr = '12987264728124387382'
ans = countSort(arr) 
print (ans)
