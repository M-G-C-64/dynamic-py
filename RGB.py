'''No of ways of arranging the balls such that same ball should come side by side'''
def sol(lst,ind,cnt):
    if ind is None:
        return 1
    if ind == 0:
        tlst = [lst[1],lst[2]]
    elif ind == 1:
        tlst = [lst[0],lst[2]]
    else:
        tlst = [lst[0],lst[1]]
    
    if (sum(x>0 for x in lst)) <= 1:
        return 1
    ind = next((i for i,v in enumerate(lst) if i and i != ind), None)
    lst[ind] -= 1
    #print('sfafd', sum(x>0 for x in tlst), tlst)
    cnt = sum(x>0 for x in tlst)*sol(lst,ind,cnt)
    
    return cnt

#inputs
r = 2
g = 2
b = 2


lst = [r,g,b]
cnt = 0
cnt += sum(x>0 for x in lst)
ind = next((i for i,x in enumerate(lst) if x),None)
if cnt > 0:
    lst[ind] -= 1
    print(cnt*sol(lst,ind,cnt))
else:
    print(cnt)
