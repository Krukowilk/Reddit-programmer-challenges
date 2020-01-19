#Description
#Given two positive year numbers (with the second one greater than or equal to
#the first), find out how many leap days (Feb 29ths) appear between Jan 1 of
#the first year, and Jan 1 of the second year in the Revised Julian Calendar.
#This is equivalent to asking how many leap years there are in the interval
#between the two years, including the first but excluding the second.


import re

leaps=0
print('Input start year, end year (positive number only)')
Years = re.match(r'^(\d+)(?:[ ,-]+)(\d+)$',input())
Y1=int(Years.group(1))
Y2=int(Years.group(2))

#leaps+=leap(Y1)
diff=Y2-Y1
Y2=Y1+(diff)%900

leaps=((diff//900)*218)
for yr in range(Y1, Y2):
    if (yr%4==0 and yr%100!=0) or (yr%900==200 or yr%900==600):
        leaps+=1

print(leaps)
