startday=int(input('enter the startding day (1-7)'))
numberofdays=int(input('enter the number of days in a month'))
print('Sun  Mon  Tue  Wed  Thur  Sat')
print('**************************')
for i in range(startday-1):
    print(end='    ')
    i=startday-1
    for j in range(1,numberofdays-1):
        if(i>6):
            print()
            i=1
        else:
            i=i+1
        print(str(j)+'   ',end=' ')