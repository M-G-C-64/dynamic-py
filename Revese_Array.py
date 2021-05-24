#https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/

lst = list(map(int, input().split()))
k = int(input())

lst2 = []
temp = []
for i in range(len(lst)):
	temp.append(str(lst[i]))
	if (i+1)%k == 0:
		lst2.append(temp[::-1])
		temp = []
lst2.append(temp[::-1])
#print(lst2)
for i in lst2: print((' ').join(i),end = ' ')
