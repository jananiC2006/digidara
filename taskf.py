def year():
    year=int(input("enter a year:"))
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print("year is leap")
    else:
        print("year is not leap")
year()