# cook your dish here
t=int(input())
for i in range(t):
    class_id=str(input())
    if class_id=='B' or class_id=='b':
        print('BattleShip')
    elif class_id=='C' or class_id=='c':
        print('Cruiser')
    elif class_id=='D' or class_id=='d':
        print('Destroyer')
    else:
        print('Frigate')