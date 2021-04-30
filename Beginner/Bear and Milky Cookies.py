# cook your dish here
def limak(n,s):
    if s[-1]=='cookie':
        return 'NO'
    for j in range(n):
        if s[j]=='cookie' and s[j+1]!='milk':
            return 'NO'
    return 'YES'
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(str,input().split()))
    print(limak(n,s))