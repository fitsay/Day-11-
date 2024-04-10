def leap_year(year):
  if year % 4 == 0:
    if year % 100 != 0:
      if year % 400 == 0:
        return True
        print(year, == "Is leap year")
      else:
        print("Not leap year")
    else:
      ("Not leap year")
  else:
    ("Not leap year")
def days_in_month(years,month):
  days(31,28,31,30,31,30,31,31,30,31,30,31)
  if month == 2 and is_leap(year):
    return 29
  else:
    return days_in_month[month - 1]

year = int(input("What is the year? "))
month = int(input())
day = input("what is the day? ")
