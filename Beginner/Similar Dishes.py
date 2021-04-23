# cook your dish here
t=int(input())
for i in range(t):
    dish1=list(map(str,input().split()))
    dish2=list(map(str,input().split()))
    count=0
    for i in dish1:
        if i in dish2:
            count+=1
    if count>1:
        print('similar')
    else:
        print('dissimilar')