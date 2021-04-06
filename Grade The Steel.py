# cook your dish here
t=int(input())
for i in range(t):
    [hard,carbon,tensile]=list(map(float,input().split()))
    grade=5
    if hard>50 and carbon<0.7 and tensile>5600:
        grade=10
    elif hard>50 and carbon<0.7:
        grade=9
    elif carbon<0.7 and tensile>5600:
        grade=8
    elif hard>50 and tensile>5600:
        grade=7
    elif hard>50 or carbon<0.7 or tensile>5600:
        grade=6
    print(grade)