#https://www.geeksforgeeks.org/coin-change-dp-7/
#difficulty -- 0.7

def coin(z,temp = 0,l = 0):
	global n,olst,minc
	cnt = 0
	if z == 0:
		minc.append(temp)
		temp = 0
		return 1
	if z < 0:
		return 0
		temp = 0
	for i in range(len(olst)):
		if l <= olst[i]:
			l = olst[i]
			coin(z-olst[i],temp+1,l)

n = int(input())

minc = []
olst = list(map(int, input().split()))
olst = sorted(olst)
coin(n)
print('ways = ',len(minc),', minimum = ',min(minc))
