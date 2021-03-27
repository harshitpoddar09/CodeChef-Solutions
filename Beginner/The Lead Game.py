# cook your dish here
n=int(input())
lead_list=[]
x=0
y=0
for i in range(n):
    [a,b]=list(map(int,input().split()))
    x=x+a
    y=y+b
    lead=x-y
    lead_list.append(lead)
big=max(lead_list)
small=min(lead_list)
if abs(big)>abs(small):
    ans=['1',str(big)]
else:
    ans=['2',str(abs(small))]
print(' '.join(ans))