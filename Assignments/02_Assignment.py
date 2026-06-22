import math

# -------------------------------------------------
# 1. Task: Calculate Profit Percentage
# Write a program that takes input for the cost price and selling price of an item.
# -------------------------------------------------

cost_price = float(input("enter your cost price :"))
selling_price = float(input("enter your selling price :"))

if cost_price <= 0:
    print("Cost price must be greater than 0")
elif selling_price > cost_price:
    profit = selling_price - cost_price
    percentage =  profit / cost_price * 100
    print("Profit Percentage: ", percentage, "And Profit of: ", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    percentage =  loss / cost_price * 100
    print("Loss Percentage: ", percentage, "And loss of: ", loss)
else:
    print("NO Profit Or Loss At Selling Item")
# -------------------------------------------------
# 2. Task: Cricket Stats Analyzer
# Objective: Write a script to analyze cricket stats for a team.
# -------------------------------------------------

one_p = int(input("Enter first Player score: "))
two_p = int(input("Enter second Player score: "))
three_p = int(input("Enter third Player score: "))
four_p = int(input("Enter fourth Player score: "))
fives_p = int(input("Enter fifth Player score: "))

total_runs = one_p + two_p + three_p + four_p + fives_p
average_runs = total_runs / 5

print(f"The total runs: {total_runs} and average runs: {average_runs}")

# -------------------------------------------------
# 3. Task: Retirement Age Calculator
# Objective: Write a program that prompts the user for their age and tells them how
# many years until they reach retirement age (65).
# -------------------------------------------------

user_age = float(input("Enter Your Age: "))

left_retirement = 65 - user_age

if user_age < 0:
    print("Enter your age above then 0")
elif user_age >= 65:
    print("You already reached retirement age.")
else:
    print("You have years left until retirement: ", left_retirement)

# -------------------------------------------------
# 4. Task: Calculate the Area of a Circle
# Objective: Write a program to calculate the area of a circle.
# -------------------------------------------------

radius_circle = float(input("Enter radius of circle: "))

circle_area = math.pi * (radius_circle ** 2)

print(f"Area of circle: {circle_area:2f}")

# -------------------------------------------------
# 5. Task: Salary Calculation
# Objective: You have to calculate an employee's salary by computing the gross
# salary tax and net salary based on the given parameters.
# -------------------------------------------------

base_salary = 50000
bonus = 5000
tax_rate = 10
other_charges = 2000

gross_salary = base_salary + bonus

salary_tax = gross_salary * tax_rate / 100

net_salary = gross_salary - salary_tax - other_charges

print("Gross Salary:", gross_salary)
print("Tax:", salary_tax)
print("Net Salary:", net_salary)

# -------------------------------------------------
# 6. Task: Bank Loan Approval System
# Objective: You have to create a javascript script that checks whether an user is
# eligible for a bank loan based on various criteria.
# -------------------------------------------------

user_age = 60
monthly_income = 25000
credit_score = 700
outstanding_debt = 10000

if (18 <= user_age <= 60 
    and monthly_income >= 25000
    and credit_score >= 700
    and outstanding_debt <= 10000):
    print("Loan Approved")
else: 
    print("Loan Rejected")

# -------------------------------------------------
# 7. Task: Students Interview Eligibility Checker
# Objective:you have to design a javascript script that checks whether a student is
# eligible for an interview based on their academic score attendance percentage
# and extracurricular participation.
# -------------------------------------------------

academic_score = float(input("Enter your Academic Score: "))
attendance_percentage = float(input("Enter your Attendance Percentage: "))
extracurricular = input("Have you done any Extracurricular activities? (yes/no): ").lower()

if extracurricular not in ["yes", "no"]:
    print("Input only Yes or No")

elif academic_score >= 75 and attendance_percentage >= 75 and extracurricular == "yes":
    print("You are selected for Interview")
else:
    print("You are not selected Interview")

# -------------------------------------------------
# 8. Task: Validating Email Domain
# Objective: You will implement a javascript program to validate the domain of a
# user's email address. The program will check if the email contains a specific
# domain (e.g. "gmail.com").
# -------------------------------------------------

user_input = input("Enter your Email: ")
check_email = "@gmail.com"


if user_input.endswith(check_email): 
    print("Yes eligible for registration")
else:
    print("Incorrect not Yes eligible for registration")

# -------------------------------------------------
# 10.Task : Student Grading System
# Create a javascript program to calculate a student's grade based on their marks.
# -------------------------------------------------

user_marks = int(input("Enter you marks: "))

if user_marks <= 100 and user_marks >= 90:
    print("Grade: A")
elif user_marks <= 89 and user_marks >= 80:
    print("Grade: B") 
elif user_marks <= 79 and user_marks >= 70:
    print("Grade: C")
elif user_marks <= 69 and user_marks >= 60:
    print("Grade: D")
elif user_marks <= 59 and user_marks >= 50:
    print("Grade: E")
elif user_marks <= 49 and user_marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks.")

# -------------------------------------------------
# 11.Task : Authentication System.
# Write a javascript program that authenticates a user by checking their username and
# password. The program should compare the entered credentials with predefined valid
# credentials.
# -------------------------------------------------

user_name = input("Enter your name: ")
user_passowrd = input("Enter your password: ")

username1 = "user1"
username1_password1 = "pass@123"

if user_name == username1 and user_passowrd == username1_password1:
    print("Authentication successful.")
else:
    print("Authentication failed.")

# -------------------------------------------------
# 12.Employee Salary Based on Experience.
# You are building a system for a Human Resources (HR) department that calculates an
# employee's salary based on their years of experience. The system assigns salary tiers
# based on the number of years an employee has been working. It also offers bonuses for
# employees who have more than 15 years of experience.
# -------------------------------------------------

employee_bonus = 5000
senior_salary = 80000
mid_level  = 50000
junior_salary = 30000

employees_experience = int(input("Enter your experience: "))

employee_bonus = 5000
senior_salary = 80000
mid_level_salary = 50000
junior_salary = 30000

employees_experience = int(input("Enter your experience: "))

if employees_experience > 15:
    print("Senior Employee")
    print("Salary:", senior_salary + employee_bonus)

elif employees_experience >= 10:
    print("Senior Employee")
    print("Salary:", senior_salary)

elif 5 <= employees_experience <= 9:
    print("Mid-Level Employee")
    print("Salary:", mid_level_salary)

else:
    print("Junior Employee")
    print("Salary:", junior_salary)

# -------------------------------------------------
# 13. Library Charge Calculation
# Problem Statement:
# Write a javascript program that calculates the library charge based on the number of days a book has been borrowed.
# -------------------------------------------------

borrowed_days = int(input("Enter the number of days a book has been borrowed: "))

if borrowed_days > 15:
    print("You Library Charges: ",borrowed_days * 5)
elif borrowed_days >= 11 and borrowed_days <= 15:
    print("You Library Charges: ", borrowed_days * 4)
elif borrowed_days >= 6 and borrowed_days <= 10:
    print("You Library Charges: ", borrowed_days * 3)
elif borrowed_days <= 5 and borrowed_days >= 1:
    print("You Library Charges: ", borrowed_days * 2)
else:
    print("No Library Charges")

# -------------------------------------------------
# 14. Arranging Three Numbers in Descending Order
# Write a javascript program to arrange three numbers in descending order.
# -------------------------------------------------

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 >= num2 >= num3:
    print(num1, num2, num3)
elif num1 >= num3 >= num2:
    print(num1, num3, num2)
elif num2 >= num1 >= num3:
    print(num2, num1, num3)
elif num2 >= num3 >= num1:
    print(num2, num3, num1)
elif num3 >= num1 >= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)

# -------------------------------------------------
# 15. Tax Calculation for Car Purchase
# Write a program to calculate the tax on a car purchase based on the car brand and its price.
# -------------------------------------------------

car_brand = input("Enter your car brand: ").lower()

car_price = float(input("Enter car price in lakh: "))

if car_brand == "mahindra" and 7 <= car_price <= 10:
    tax = car_price * 5 / 100
    print("If you purchase {} car on that tax was: {} and price of: {}" .format(car_brand, tax, car_price))
elif car_brand == "audi" and  10 <= car_price <= 15:
    tax = car_price * 10 / 100
    print("If you purchase {} car on that tax was: {} and price of: {}" .format(car_brand, tax, car_price))
elif car_brand == "jaguar" and 15 <=  car_price <= 20:
    tax = car_price * 25 / 100
    print("If you purchase {} car on that tax was: {} and price of: {}" .format(car_brand, tax, car_price))
elif car_brand == "mercedes" and 20 <= car_price <= 25:
    tax = car_price * 30 / 100
    print("If you purchase {} car on that tax was: {} and price of: {}" .format(car_brand, tax, car_price))
else: 
    print("No tax on the car you purchased")

# -------------------------------------------------
# 16.Finding the Middle Number
# ○ Task: Write a program to determine the middle number among three inputs.
# -------------------------------------------------

n1 = int(input("Enter number one: "))
n2 = int(input("Enter number second: "))
n3 = int(input("Enter number third: "))

# n1 > n2 , n2 > n3 || n1 > n3 , n3 > n2
# n2 > n1 , n1 > n3 || n2 > n3 , n3 > n1
# n3 > n1 , n1 > n2 || n3 > n2 , n2 > n1

# Take both step where same variable at the mid.

if (n3 >= n1 >= n2) or (n2 >= n1 >= n3):
    print(n1)
elif (n1 >= n2 >= n3) or (n3 >= n2 >= n1):
    print(n2)
else: 
    print(n3)


# -------------------------------------------------
# 17.Find the greatest number.
# ○ Task: Write a program to find greatest number from three number
# -------------------------------------------------

number1 = int(input("Enter number one: "))
number2 = int(input("Enter number second: "))
number3 = int(input("Enter number third: "))

if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3:
    print(number2)
else:
    print(number3)

# -------------------------------------------------
# 19.Calculate Class Attendance Percentage
# Task: Write a program to calculate the percentage of classes attended by a
# student and determine their eligibility to sit in the exam.
# -------------------------------------------------

attendance = 75

if  75 <= attendance <= 100:
    print(f"The attendance percentage {attendance} and eligibility status Eligible")
elif 0 <= attendance < 75:
    print(f"The attendance percentage {attendance} and eligibility status Not Eligible")
else:
    print("Enter percentage between 0 and 100")

# -------------------------------------------------
# 21.UPSC Selection Process
# Task: Simulate the UPSC selection process with the following steps:
# 1. Eligibility Check
# 2. Prelims Exam
# 3. Mains Exam
# 4. Interview
# -------------------------------------------------

eligibility_age = int(input("Enter your age: "))
graduation = input("You are Graduated: ").lower()
nationality = input("What is your nationality: ").lower()

if not (21 <= eligibility_age <= 32):
    print("Ineligible: Age must be between 21 and 32 years.")

elif graduation != "yes":
    print("Ineligible: Candidate must be a graduate.")

elif nationality != "indian":
    print("Ineligible: Nationality must be Indian.")

else:
    print("Proceed to Prelims")
    
    prelims_score = int(input("Enter Your Prelims Score: "))
    if prelims_score >= 80:
        print("Proceed to Mains")
        mains_score = int(input("Enter Your Mains Score: "))
        if mains_score >= 90:
            print("Proceed to Interview")
            interview_score = int(input("Enter Your Interview Score: "))
            if interview_score >= 70:
                print("Congratulations! You have cleared the UPSC.")
            else:
                print("You failed the Interview.")
        else:
            print("You failed the Mains")
    else:
        print("You failed the Prelims")

# -------------------------------------------------
# 22. Menu-Driven Login System
# Login with Phone
# Login with Email
# Exit the system
# -------------------------------------------------

print("1 Login with Phone selected")
print("2 Login with Email selected")
print("3 Exiting...")
choice = int(input("Enter your choice: "))

phone_v = 7566300872
opt_v = 5588
email_v = "raghaw@gmail.com"
password_v = "raghaw@123"

if choice == 1:
    phone = int(input("Enter your number: "))
    opt = int(input("Enter your otp: "))
    if phone == phone_v and opt == opt_v:
        print("Login successful with phone!")
    else:
        print("Incorrect phone and opt")
elif choice == 2:
    email = input("Enter your eamil: ")
    password = input("Enter your password: ")
    if email == email_v and password_v == password:
        print("Login successful with email!")
    else:
        print("Incorrect email and password")
elif choice == 3:
    print("Exiting the program. Have a nice day!")
else:
    print("Invalid choice")

# -------------------------------------------------
# 23. Create Your Own KBC Game
# Design and implement a quiz game inspired by the popular Kaun Banega Crorepati (KBC)
# Game show. The aim of this assignment is to test the user's knowledge through a series of multiple-choice questions, track their score, and display statistics at the end of the game. 
# -------------------------------------------------

start_game = input("Do you want to start the game? (yes/no): ").lower()

if start_game == "yes":

    kbc_score = 0
    correct_answers = 0
    wrong_answers = 0
    skipped_questions = 0

    print("\nQuestion 1: What is the capital of India?")
    print("A. Mumbai")
    print("B. Delhi")
    print("C. Kolkata")
    print("D. Chennai")

    answer = input("Enter your answer (A/B/C/D) or skip: ").lower()

    if answer == "skip":
        skipped_questions += 1
    elif answer == "b":
        kbc_score += 1000
        correct_answers += 1
    else:
        wrong_answers += 1

    print("\nQuestion 2: Which language is used for Python programming?")
    print("A. Python")
    print("B. Java")
    print("C. HTML")
    print("D. CSS")

    answer = input("Enter your answer (A/B/C/D) or skip: ").lower()

    if answer == "skip":
        skipped_questions += 1
    elif answer == "a":
        kbc_score += 2000
        correct_answers += 1
    else:
        wrong_answers += 1

    print("\nQuestion 3: How many days are there in a week?")
    print("A. 5")
    print("B. 6")
    print("C. 7")
    print("D. 8")

    answer = input("Enter your answer (A/B/C/D) or skip: ").lower()

    if answer == "skip":
        skipped_questions += 1
    elif answer == "c":
        kbc_score += 3000
        correct_answers += 1
    else:
        wrong_answers += 1

    print("\nQuestion 4: Which planet is known as the Red Planet?")
    print("A. Earth")
    print("B. Mars")
    print("C. Venus")
    print("D. Jupiter")

    answer = input("Enter your answer (A/B/C/D) or skip: ").lower()

    if answer == "skip":
        skipped_questions += 1
    elif answer == "b":
        kbc_score += 5000
        correct_answers += 1
    else:
        wrong_answers += 1

    print("\nQuestion 5: What is 10 × 10?")
    print("A. 50")
    print("B. 100")
    print("C. 200")
    print("D. 150")

    answer = input("Enter your answer (A/B/C/D) or skip: ").lower()

    if answer == "skip":
        skipped_questions += 1
    elif answer == "b":
        kbc_score += 10000
        correct_answers += 1
    else:
        wrong_answers += 1

    print("\n===== GAME OVER =====")
    print("Total Score:", kbc_score)
    print("Correct Answers:", correct_answers)
    print("Wrong Answers:", wrong_answers)
    print("Skipped Questions:", skipped_questions)

else:
    print("Game Ended")
