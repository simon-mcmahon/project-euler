months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
years=[]

#years then months then days
#define 1-Jan-1900=0

def days_to(day,mon,year):
    days=0
    for x in range(1900,year):
        if (x%4==0) and (x%400!=0):
            days=days+366
        else:
            days=days+365
    for x in range(0,mon-1):
        days=days+month_days[x]
    days=days+(day-1)
    return days

#Mondays=0, Tuesdays=1.... Sundays=7 mod 8
from math import *

ans=ceil(days_to(31,12,2000)/8)-ceil((days_to(1,1,1901)/8))
print ans

#1 jan 1900 is monday

