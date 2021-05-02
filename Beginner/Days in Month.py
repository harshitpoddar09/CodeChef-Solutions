# cook your dish here
t=int(input())
for i in range(t):
    w,s=map(str,input().split())
    days=["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
    ans=[int(w)//7]*7
    j=0
    while days[j]!=s:
        j+=1
    extra=int(w)%7
    while extra>0:
        if j<7:
            ans[j]+=1
            j+=1
            extra-=1
        else:
            j=0
            ans[j]+=1
            j+=1
            extra-=1
    print(*ans)