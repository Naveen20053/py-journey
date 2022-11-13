year = int(input("Which year do you want to check? "))


leap_year = year % 4

if leap_year == 0:
    not_leap_year = leap_year%100
    if not_leap_year == 0:
        is_leap_year = not_leap_year%400
        if is_leap_year == 0:
            print("Leap year")
        else:
            print("Not leap year")
else:
    print("Not leap year")
