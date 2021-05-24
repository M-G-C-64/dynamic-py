#https://www.geeksforgeeks.org/k-centers-problem-set-1-greedy-approximate-algorithm/
difficulty - 0.5

weights = [[0,4,8,5],[4,0,10,7],[8,10,0,9],[5,7,9,0]]
k = 2
temp = {}
for i in range(len(weights)):
	lst = weights[i]
	lst = sorted(lst, reverse = True)
	temp[i] = lst[k-1]
miny = min(temp, key = temp.get)
arr = weights[miny]
res = [miny]
while k>1:
	z = arr.index(max(arr))
	res.append(z)
	arr[z] = 0
	k = k-1
print(res)
