# cook your dish here
t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    solve=list(map(int,input().split()))
    cakewalk=0
    hard=0
    for i in solve:
        if i>=p//2:
            cakewalk+=1
        elif i<=p//10:
            hard+=1
    if cakewalk==1 and hard==2:
        print('yes')
    else:
        print('no')