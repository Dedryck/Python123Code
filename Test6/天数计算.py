#闰年的条件：1.能被4整除，不能被100整除    
#           2. 能被400整除。
year, month = eval(input())
day_year = 365
month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    month_list[1] = 29
    day_year = 366

print(month_list[month - 1])