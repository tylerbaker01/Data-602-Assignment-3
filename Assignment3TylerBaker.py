# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if
# statements and else statements print the user a message recommending a meal. For example,
# if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or
# dinner.
meal = input("breakfast, lunch, or dinner? ")
if meal == "breakfast":
    print("Doesn't oatmeal sound good?")
elif meal == "lunch":
    print("Why not sushi?")
elif meal == "dinner":
    print("Tacos!")
else:
    print("That's not a meal.")

# Q2: The mailroom has asked you to design a simple payroll program that calculates a student
# employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a
# week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20.
# You should take in the user’s input for the number of hours worked, and their rate of pay.

hours_worked = int(input("How many hours worked? "))
pay_rate = int(input("What is the pay rate? "))
overtime = 1.5

if hours_worked <= 20:
    gross_pay = hours_worked * pay_rate
    print(gross_pay)
else:
    ot_hours = hours_worked - 20
    gross_pay = ((hours_worked - ot_hours) * pay_rate) + (ot_hours * overtime * pay_rate)
    print(gross_pay)


# Q3: Write a function named times_ten. The function should accept an argument and display the
# product of its argument multiplied times 10.
def times_ten(arg):
    print(arg * 10)


# Q4: Find the errors, debug the program, and then execute to show the output.
# def main()
# Calories1 = input( "How many calories are in the first food?")
# Calories2 = input( "How many calories are in the first food?")
# showCalories(calories1, calories2)
# def showCalories()
# print(“The total calories you ate today”, format(calories1 + calories2,.2f))

def main():
    calories1 = int(input("How many calories are in the first food? "))
    calories2 = int(input("How many calories are in the second food? "))
    total_calories = calories1 + calories2
    print("The total calories you ate today are" + str(total_calories))


# Q5: Write a program that uses any loop (while or for) that calculates the total of the
# following series of numbers:
# 1/30 + 2/29 + 3/28 .............29/30 + 30/1

from fractions import Fraction
series = list(range(1, 31))
opposite = series[::-1]
b = list(range(30))
#for i in series:
        #fraction = Fraction(series[i]/opposite[i])
        #print(fraction)
# This is producing a bug.

for i in b:
    fraction = Fraction(series[i]/series[-i])
    print(fraction)
# still producing a bug

# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT
# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4) # should print 10

def triangle_area(base, height):
    base = float(input("What is the base? "))
    height = float(input("What is the height? "))
    area = 0.5 * base * height
    print(area)
