# cook your dish here
n=int(input())
budget=[]
for i in range(n):
    budget.append(int(input()))
budget.sort()
ans=[]
for i in range(n):
    ans.append(budget[i]*(n-i))
print(max(ans))