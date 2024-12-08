def grade_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


#Leap Year Checker
#Write a function check_leap_year(year) that takes an integer year and checks:

#If the year is divisible by 4 but not divisible by 100, it's a leap year.
#If the year is divisible by 400, it's a leap year.
#Otherwise, it’s not a leap year.

def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        print("its a Leap year")
    else:
        print("its not a leap year")

year = int(input("Please enter year:"))

print(leapyear(year))


