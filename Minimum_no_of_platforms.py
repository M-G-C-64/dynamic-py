#https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/


#VSCode
#ctrl+F2 -> edit all same keywords
#ctrl+shift+alt+arrow up/down -> multiple cursors
def plat(a,l):
    global ariv,lev,p
    if a >= len(ariv):
        return 0
    #print(a,l,'p:',p)
    temp = 0
    for i in l:
        #print('i',i)
        if ariv[a]>lev[i]:
            l.append(l[-1]+1)
            l.remove(i)
            break
        else:
            temp += 1

    if temp>0:
        p+=1
        l.append(l[-1]+1)
    plat(a+1,l)

def conv(arrv):
	for i in range(len(arrv)):
		ar1,ar2 = map(str, arrv[i].split(':'))
		arrv[i] = int(ar1+ar2)
	return arrv

ariv = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00', '18:01']
lev  = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00', '24:00']

ariv = conv(ariv)
lev = conv(lev)
p = 1

plat(1,[0])
print(p)
