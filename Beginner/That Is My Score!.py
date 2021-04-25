# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    scores=[0]*11
    for j in range(n):
        p,s=map(int,input().split())
        if s>scores[p-1]:
            scores[p-1]=s
    print(sum(scores[:8]))