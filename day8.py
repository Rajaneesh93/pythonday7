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



# 4. Number Comparison
# Write a function compare_numbers(a, b) that takes two integers and prints:

# "a is greater" if a > b
# "b is greater" if b > a
# "a and b are equal" if both numbers are equal.

def numberComparision(a,b):
    if a > b:
        print("a is greater")
    elif b > a:
        print("b is greater")
    elif a == b:
        print("a and b are equal")
    else:
        print("Enter integers only")

a = int(input("Please enter A: "))

b = int(input("Please enter B: "))

print(numberComparision(a,b))


# Find the Largest Number
# Write a function find_largest(a, b, c) that takes three integers and prints the largest number among the three.

def largestNumber(a,b,c):
    if a > b and a > c:
        print("a is graterthan b and c")
    elif b > a and b > c:
        print("b is graterthan a and c")
    # elif c > b and c > a:
    #     print("c is graterthan a and b")
    else:
        print("c is graterthan a and b")

largestNumber(100,200,300)


# . Even or Odd
# Write a function even_or_odd(num) that checks if a number is even or odd:

# Print "Even" if the number is divisible by 2.
# Print "Odd" if the number is not divisible by 2.

def evenOdd(number):
    if number % 2 ==0:
        print("This number is even")
    else:
        print("This number is odd")

number = int(input("Please enter your number: "))

evenOdd(number)



# Write a function age_group(age) that categorizes a person into the following groups based on their age:

# "Child" for ages 0-12
# "Teenager" for ages 13-19
# "Adult" for ages 20-64
# "Senior" for ages 65 and above

def ageGroup(age):
    if age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 64:
        print("Adult")
    elif age > 65:
        print("old")
    else:
        print("Please enter valid age")
        
age =input("Please enter your age: ")

ageGroup(age)

 8. Discount Calculator
# Write a function calculate_discount(price) that calculates the discount based on the price:

# If the price is greater than or equal to 500, apply a 20% discount.
# If the price is between 200 and 499 (inclusive), apply a 10% discount.
# If the price is less than 200, apply no discount.
# Print the final price after the discount.

def disCalc(price):
    if price >= 500:
        Bill = price - (price *0.20)
        print(Bill)
    elif price > 200 and price <=499:
        Bill = price - (price *0.10)
        print(Bill)
    elif price <= 200:
        Bill = price
        print(Bill)
    else:
        print("Please enter a valid price")

disCalc(100)


        
