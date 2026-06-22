# =================================================================
# Basic Variable Swapping
# =================================================================


# ------------------------------------------------------------------
# 1. Switch values of two integers
# ------------------------------------------------------------------

# Input:
# n1 = 20,
# n2 = 30

n1 = 20
n2 = 30

print(f"Before Swaping integers: n1: {n1} and n2: {n2}")

temp = n1
n1 = n2
n2 = temp

print(f"After Swaping integers: n1: {n1} and n2: {n2}")

# ------------------------------------------------------------------
# 2. Switch values of two strings (characters)
# ------------------------------------------------------------------

# Input:
# char1 = "hello"
# char2 = "java"

char1 = "hello"
char2 = "java"

print(f"Before Swaping string: char1: {char1} and char2: {char2}")

char1, char2 = char2 , char1

print(f"After Swaping string: char1: {char1} and char2: {char2}")

# ------------------------------------------------------------------
# 3. Switch one string value with one integer value
# ------------------------------------------------------------------

# Input:
# n3 = 200,
# char3 = "java"

n3 = 200
char3 = "java"

print(f"Before Swaping string, integer: n3: {n3} and char3: {char3}")

arr = [n3 , char3]

char3 = arr[0]
n3 = arr[1]

print(f"After Swaping string, integer: n3: {n3} and char3: {char3}")


# =================================================================
# Banking and Transactions
# =================================================================

# ------------------------------------------------------------------
# 5. Update balance after deposit
# Initial balance: current_balance = 10000
# Deposit amount: deposit_balance = 5000
# ------------------------------------------------------------------

current_balance = 10000
deposit_balance = 5000

print("Before deposit: current_balance", current_balance)

current_balance = current_balance + deposit_balance 
print("After deposit: current_balance", current_balance)

# ------------------------------------------------------------------
# 6. Update balance after withdrawal
# Before: balance = 12000
# Withdrawal: 3000
# ------------------------------------------------------------------

balance = 12000
Withdrawal = 3000

print("Before Withdrawal balance", balance)

balance -= Withdrawal

print("After Withdrawal balance", balance)

# ------------------------------------------------------------------
# 7. Increase shopping cart items by 3
# Before: cart_items = 5
# ------------------------------------------------------------------

cart_items = 5
add_item = 3

print("Before Cart Item: {}".format(cart_items))
print("After Cart Item: {}".format(cart_items + add_item))

# ------------------------------------------------------------------
# 8. Apply a 20% discount to a price
# Before: price = 1000
# ------------------------------------------------------------------

price = 1000
discount = 20

print("Before discount Price: {p}" .format(p = price))

discount = price * discount / 100

print("After Discount Price : {}" .format(int(price - discount)))

# =================================================================
# Academic Calculations
# =================================================================

# ------------------------------------------------------------------
# 9. Calculate student percentage
# Input: obtain_marks = 430, out_of = 500
# ------------------------------------------------------------------

out_of = 500
obtain_marks = 430

percentage = ( obtain_marks / out_of ) * 100

print("Student Percentage: {p}" .format( p = percentage))

# ------------------------------------------------------------------
# 10.Calculate total and average of 4 subjects
# Input Example
# ● Subject 1: 80
# ● Subject 2: 75
# ● Subject 3: 90
# ● Subject 4: 85
# ------------------------------------------------------------------

s_1 = 80
s_2 = 75
s_3 = 90
s_4 = 85

total = s_1 + s_2 + s_3 + s_4

print("Total marks: {t} and average of marks: {a}" .format(t = total, a = total / 4))

# ------------------------------------------------------------------
# 11. Calculate average of 3 numbers
# Input: num1 = 25, num2 = 35, num3 = 45
# ------------------------------------------------------------------

num1 = 25
num2 = 35
num3 = 45

total_num = num1 + num2 + num3
avg = total / 3

print("average of 3 numbers is: ", avg)

# =================================================================
# Finance & Business Calculations
# =================================================================

# ------------------------------------------------------------------
# 12.Calculate profit or loss percentage
# Input: cost_price = 500, selling_price = 600
# ------------------------------------------------------------------

cost_price = 500
selling_price = 600

calculation = selling_price - cost_price 

per =  calculation / cost_price * 100

print("Profit percentage: ", per)

# ------------------------------------------------------------------
# 13. Calculate simple interest
# Input: principal = 10000, rate = 5, time = 2
# ------------------------------------------------------------------

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) /100

print("Simple Interest:", simple_interest)

# ------------------------------------------------------------------
# 14.Calculate compound interest
# Input: principal = 10000, rate = 5, time = 2
# ------------------------------------------------------------------

p = 10000
r = 5
t = 2

amount = p * ( 1 + r /100 ) ** t
compound_interest = amount - p

print("Compound Interest:", compound_interest)

# ------------------------------------------------------------------
# 15.Calculate tax on income
# Input: income = 500000, tax_rate = 10
# ------------------------------------------------------------------

income = 500000
tax_rate = 10

tax = income * tax_rate / 100

print("Tax: {t}" .format(t = tax))

# ------------------------------------------------------------------
# 16.Calculate percentage increase or decrease
# Input: initial_value = 200, final_value = 250
# ------------------------------------------------------------------

initial_value = 400
final_value = 250

percentage_change = ( ( final_value -  initial_value ) / initial_value ) * 100

if percentage_change > 0:
    print("increase percentage: {}" .format(percentage_change))
elif percentage_change < 0:
    print("decrease percentage: {}" .format(percentage_change))
else:
    print("no changes")

# =================================================================
# Conversions
# =================================================================

# ------------------------------------------------------------------
# 17. Convert boolean to integer
# Input: True
# ------------------------------------------------------------------

value = True
convert = int(value)

print(convert)

# ------------------------------------------------------------------
# 18.Convert float to string
# Input: 45.67
# ------------------------------------------------------------------

val = 45.6
con = str(val)

print(con)

# ------------------------------------------------------------------
# 19.Convert 20°C to Fahrenheit
# Input: 20°C
# ------------------------------------------------------------------

celsius = 20
fahrenheit = ( celsius * 1.8 ) + 32

print(fahrenheit)

# ------------------------------------------------------------------
# 20. Convert 50°F to Celsius
# Input: 50°F
# ------------------------------------------------------------------

fahr = 50
cel = ( fahr - 32 ) * 5 / 9

print(cel)

# ------------------------------------------------------------------
# 21.Convert integer to binary
# Input: 25
# ------------------------------------------------------------------

number = 25
binary = bin(25)[2:]

print(binary)

# =================================================================
# Geometry
# =================================================================

# ------------------------------------------------------------------
# 21. Calculate area of a triangle
# Input: base = 10, height = 6
# ------------------------------------------------------------------

base = 10
height = 6

area = 0.5 * base * height

print("The area of the triangle is:", area)

# ------------------------------------------------------------------
# 22.Calculate perimeter of a square
# Input: side = 9
# ------------------------------------------------------------------

side = 9
perimeter = 4 * side

print("perimeter of a square: {}" .format(perimeter))

# ------------------------------------------------------------------
# 23.Calculate diameter of a circle
# Input: radius = 14
# ------------------------------------------------------------------

radius = 14
diameter = 2 * radius

print(diameter)

# ------------------------------------------------------------------
# 24.Calculate volume of a cube
# Input: side = 5
# ------------------------------------------------------------------

cube_side = 5
volume_cube = cube_side * cube_side * cube_side

print("volume of a cube" , volume_cube)

# ------------------------------------------------------------------
# 25.Calculate surface area of a cuboid
# Input: l = 4, b = 3, h = 2
# ------------------------------------------------------------------

l = 4
b = 3
h = 2

surface_Area = 2 * (l * b + b * h + l * h)

print("surface area of a cuboid: ", surface_Area)

# =================================================================
# Mathematical Expressions
# =================================================================

# ------------------------------------------------------------------
# 26.Square of sum: (x + y)²
# Input: x1 = 5, y1 = 7
# ------------------------------------------------------------------

x1 = 5
y1 = 7

sum_square = (x1 + y1) ** 2

print("Square of sum: ", sum_square)

# ------------------------------------------------------------------
# 27.Simplify expression: x² - 4x + 4
# Input: x = 3
# ------------------------------------------------------------------

x2 = 3

result = x2 ** 2 - 4 * x2 + 4
print("result: ", result)

# ------------------------------------------------------------------
# 25.Evaluate: (a1 + b2)(a1 - b2)
# Input: a = 6, b = 2
# ------------------------------------------------------------------

a1 = 6
b2 = 2

evaluate = (a1 + b2) * (a1 - b2)

print("Evaluate: " ,evaluate)

# ------------------------------------------------------------------
# 29.Sum of cubes: a³ + b³
# Input: a3 = 1, b3 = 2
# ------------------------------------------------------------------

a3 = 1
b3 = 2

cubes_sum = a3**3 + b3 **3

print("sum of cubes: ",cubes_sum)

# ------------------------------------------------------------------
# 30.Simplify: (x - y)²
# Input: x = 10, y = 6
# ------------------------------------------------------------------

x4 = 10
y4 = 6

simplify = (x4 - y4) ** 2

print(simplify)

# ------------------------------------------------------------------
# 31.Difference of cubes: x³ - y³
# Input: x5 = 4, y5 = 1
# ------------------------------------------------------------------

x5 = 4
y5 = 1

result2 = x5**3 - y5**3

print(result2)

# =================================================================
# String Operations
# =================================================================

# ------------------------------------------------------------------
# 32.If user input is:
# Name: Dev
# Age: 25
# City: Jaipur
# Hobby: Cooking

# Then Output is :
# Meet Dev, a 25-year-old enthusiast from Jaipur.
# When not busy with daily tasks, Dev loves spending time cooking.
# Life in Jaipur keeps Dev energetic and curious every single day.
# With coding as a passion, the future looks creative and inspiring for
# Dev in the Jaipur City.
# ------------------------------------------------------------------

Name = "Dev"
Age = 25
City = "Jaipur"
Hobby = "Cooking"

string = """
Meet Dev, a 25-year-old enthusiast from Jaipur.
When not busy with daily tasks, Dev loves spending time cooking.
Life in Jaipur keeps Dev energetic and curious every single day.
With coding as a passion, the future looks creative and inspiring for
Dev in the Jaipur City."""

print(string)

# ------------------------------------------------------------------
# 33.Create a Python program that asks the user for the following:
# ● Full Name
# ● Profession
# ● Favorite Quote
# ● Years of Experience
# ------------------------------------------------------------------

full_name  ="raghaw Pathak"
profession = "computer Scince"
favorite_quote = "pratice make men perfect"
experience = 4

print("Full Name: ", full_name)
print("Profession: ", profession)
print("Favorite Quote: ", favorite_quote)
print("Years of Experience: ", experience)

# ------------------------------------------------------------------
# 34.Ask the user:
# ● Movie Name
# ● Viewer Name
# ● Seat Number
# ● Show Time
# ------------------------------------------------------------------

movie_name = "Animal"
viewer_name = "chandra dev pathak"
seat_name = 88
show_name = "12:30"

print("Movie Name :", movie_name)
print("Viewer Name :", viewer_name)
print("Seat Number :", seat_name)
print("Show Time :", show_name)