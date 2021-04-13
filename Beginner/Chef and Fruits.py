# cook your dish here
def fruits(n,m,k):
    if k<=abs(n-m):
        return abs(n-m)-k
    return 0
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    print(fruits(n,m,k))