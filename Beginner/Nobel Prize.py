# cook your dish here
t=int(input())
for i in range(t):
    [n,m]=list(map(int,input().split()))
    topic=list(map(int,input().split()))
    a=[i for i in range(1,m+1)]
    if a==list(set(topic)):
        print('No')
    else:
        print('Yes')