print("\nProblem6\n")
# a 
def is_leap(year):
    if year >= 0:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                return "Not leap year"
            elif year % 100 == 0 and year % 400 == 0: 
                return "Leap year"
            else:  
                return "Leap year"
        else:  
            return "Not leap year"
    else:
        return "Invalid Year!!!"
    
# b
def days_in_month(month, year):
    if 0 < month <= 12:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return "31"
        elif month in [4, 6, 9, 11]:
            return "30"
        elif month == 2:
            result = is_leap(year)
            if result == "Leap year":
                return "29"
            else:
                return "28"
    else:
        return "Invalid Month!!!"

# c
y = [-1900, 1900, 2000, 1987, 1800, 1200, 2024]
for year in y:
    print(year, "->", is_leap(year))

print("")
m= [2, 4, 7, 13, -2]
for year in y:
    for month in m:
        print(month, "m", year, "y", "->", days_in_month(month, year))
    print("")
print("")

# d
count = 0
for year in range(2000, 2100):
    result = is_leap(year)
    if result == "Leap year":
        count += 1
print("The total leap year from 2000-2100 is:", count)
print("")