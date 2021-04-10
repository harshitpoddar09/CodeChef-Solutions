# cook your dish here
t=int(input())
for i in range(t):
    [n,x]=list(map(int,input().split()))
    movie=[]
    for j in range(n):
        movie.append(list(map(int,input().split())))
    movie.sort(reverse=True, key=lambda x:x[1])
    for k in movie:
        if k[0]<=x:
            print(k[1])
            break