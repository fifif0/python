#4.3.1.8
def is_year_leap(year):
    if year < 1582:
        return False
    elif year %4 != 0:
        return False
    elif year %100 != 0:
        return True
    elif year %400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

def day_of_year(year, month, day):
    if year < 1582:
        return None
    if month > 12 or month<1:
        return None
    if day > days_in_month(year,month) or day < 1:
        return None

    total_days = day
    month -= 1
    while month > 0:
        total_days += days_in_month(year, month)
        month -= 1
    return total_days



def num_input(var):
    while True:
        if var==1:
            var=input("Enter the year:")
        elif var==2:
            var=input("Enter the month:")
        else:
            var=input("Enter the year:")
        if var.isnumeric():
            print(var)
            var=int(var)
            break
    return var
    

rok=num_input(1)
mies=num_input(2)
dzien=num_input(3)

#rok=int(input("Enter the :"))
#mies=int(input("Enter the :"))
#dzien=int(input("Enter the :"))

print(day_of_year(rok,mies,dzien))
