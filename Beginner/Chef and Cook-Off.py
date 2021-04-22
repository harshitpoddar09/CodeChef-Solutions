# cook your dish here
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    level=["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"]
    print(level[a.count(1)])