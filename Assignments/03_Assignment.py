# ----------------------------------------------------------------------------------
# 1. Write a Python program to print all odd and even numbers from 1 to 20.
# ----------------------------------------------------------------------------------

for i in range(1,21):
    if i % 2 == 0:
        print(f"Even {i}")
    else:
        print(f"Odd {i}")

# ----------------------------------------------------------------------------------
# 2. Write a Python program to generate all multiples of 12. 
# ----------------------------------------------------------------------------------

for i in range(1, 11):
    print(i*12)

# ----------------------------------------------------------------------------------
# 3. Write a Python program to generate a table of a number provided by the user.
# ----------------------------------------------------------------------------------

user_number = int(input("Enter number that table Want you: "))

for i in range(1, 11):
    print(f"{user_number} * {i} = {i*user_number}")

# ----------------------------------------------------------------------------------
# 4. Given a number, print all numbers that divide it exactly (without remainder).
# ----------------------------------------------------------------------------------

num = int(input("Give a number: "))

for i in range(1, num+1):
    if num % i == 0:
        print(i)

# ----------------------------------------------------------------------------------
# 5. Write a Python program to check if a number provided by the user is prime or not.
# ----------------------------------------------------------------------------------

number = int(input("Enter number: "))

# if number <= 1:
#     print("not prime")
# else: 
#     is_prime = True

#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print("Prime Numbers")
else:
    print("Not Prime")

# ----------------------------------------------------------------------------------
# 6. Write a Python program to calculate the sum of numbers between a starting and ending point provided by the user. 
# ----------------------------------------------------------------------------------

start = int(input("Enter start: "))
end = int(input("Enter end: "))

total = 0

for i in range(start, end + 1):
    total += i

print(total)

# ----------------------------------------------------------------------------------
# 7. Write a Python program to calculate the product of numbers between a starting and ending point provided by the user
# ----------------------------------------------------------------------------------

start_num = int(input("Enter start: "))
end_num = int(input("Enter end: "))

product = 1

for i in range(start_num, end_num + 1):
   product = product * i

print(product)

# ----------------------------------------------------------------------------------
# 8. Write a Python program to generate the Fibonacci sequence up to a specified number of terms
# ----------------------------------------------------------------------------------

n = int(input("Enter a number: "))

a = 0
b = 1

print(a, b , end=" ")

for i in range(n - 2):
    c = a + b
    print(c, end=" ")

    a = b
    b = c
    b = c

# ----------------------------------------------------------------------------------
# 9. Write a Python program to generate and display the first N terms of the Fibonacci sequence, where N is entered by the user.
# ----------------------------------------------------------------------------------

def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n_fibonacci = int(input("Enter number of terms: "))

for i in range(n_fibonacci):
    print(fibonacci(i), end=" ")

# ----------------------------------------------------------------------------------
# 10. Write a Python program to calculate the factorial of a number provided by the 
# user. 
# ----------------------------------------------------------------------------------

f_n = int(input("Enter number: "))

factorial = 1

for i in range(1, f_n +1):
    factorial *= i
    print(factorial)

# ----------------------------------------------------------------------------------
# 11. Write a Python program to find the greatest character from the string "python". 
# ----------------------------------------------------------------------------------

name = "python"
greatest = name[0]

for ch in name:
    if ch > greatest :
        greatest = ch

print(greatest)

# ----------------------------------------------------------------------------------
# 12. Write a Python program to display all letters except 'm' and 'i' from the string "Dreamer infotech". 
# ----------------------------------------------------------------------------------

letters = "Dreamer infotech"

for word in letters:
    if word not in "mi":
        print(word, end="") 

# ----------------------------------------------------------------------------------
# 13. Write a Python program to print alternate characters from a given string.
# ----------------------------------------------------------------------------------

alter = "abcdefghij"

for i in range(0, len(alter), 2):
    print(alter[i])

# ----------------------------------------------------------------------------------
# 14. Write a Python program to reverse a string entered by the user.
# ----------------------------------------------------------------------------------

reverse = "abcd"
store = ""

for i in reverse:
   store =  i + store
print(store)

# ----------------------------------------------------------------------------------
# 15. Write a Python program to count the total number of characters in a string entered by the user. 
# ----------------------------------------------------------------------------------

cou = "qwertyuiopasdfghjklzxcvbnm"
total_number = 0


for i in cou:
    total_number += 1
print(total_number)

# ----------------------------------------------------------------------------------
# 16. Write a Python program to check whether a string entered by the user is a palindrome. 
# ----------------------------------------------------------------------------------

input_Str =  "helleh"
store_Str = "" 
for ch in input_Str:
    store_Str = ch + store_Str


if input_Str == store_Str:
    print("Its a palindrome string")
else:
    print("Its not palindrome string")

# ----------------------------------------------------------------------------------
# 17. Write a Python program that allows the user to search for a character within a given string. 
# ----------------------------------------------------------------------------------

char = "a"
word = "raghaw"

for i in word:
    if i in word:
        print("character found")
    else:
        print("character Not found")

# ----------------------------------------------------------------------------------
# 18. Write a Python program to filter out all vowels and consonants from a string entered by the user. 
# ----------------------------------------------------------------------------------

char = "a"
word = "raghaw"
is_found = False

for i in word:

    if i == char:
        is_found = True
        break
    else:
        is_found = False

if is_found == True:
    print("character found")
else:
    print("character not found")

# ----------------------------------------------------------------------------------
# 19. Write a Python program to filter out duplicate characters from a string entered by the user. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 20. Write a Python program to display all possible pairs of 3. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 21. Write a Python program to generate the pattern of the letter H. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 22. Write a Python program to find duplicate letters between two strings. Example: In "virat" and "rohit", the duplicate letter is "r". 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 23. Write a Python program to display the squares of numbers from 1 to 10. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 24. Given a string text = "python", calculate the sum of the indices of its characters without using the range() or len() functions. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 25. Given: text = "python programming" 
# Goal: Count how many vowels are in the string. 
# Constraint: Do not use indexing (text[i]) or slicing (text[:]). 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 26. Given: text = "programming" 
# Goal: Print all characters that repeat in the string. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 27. Given : 01275623 
# Write a Python program to find and print the greatest character in the string. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 28. Given : "rahul" 
# Write a Python program to find and print the greatest character in the string. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 29. Given: text = "knowyourself" 
# Goal: Find and print the first character that repeats. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 30. Give : text=”if you think you can not do, you can not show think wisely”  
# Goal: Print the alternate words  
# Constraint: Do not use space between words more than once . 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 31. Given: text = "knowyourself" 
# Goal: Find and print the alternate characters. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 32. Take two numbers from the user: start and end. Print a string labeling each 
# number in that range as Odd or Even. 
# Output_format : 3:Odd 4:Even 5:Odd 6:Even 7:Odd 8:Even 9:Odd 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 33.Find the sum of string “198765456412”. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 34.Count how many digits in the string are greater than 5 from text = "1234567890".
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 35.Task: Replace Character in String 
# Write a program that takes a string input from the user, then asks for a character 
# to replace and the character to replace it with. The program should output the 
# modified string where all occurrences of the specified character are replaced by 
# the replacement character. 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 36.Replace Spaces with Underscores Replace all spaces in a string with underscores (_) 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 37.Remove Duplicate characters from the string given by the user then print the final output.
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 38.Take string from user and Replace every vowel in the string with an asterisk *.
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 39.Count only words not spaces. 
# Entered a string: Hello coders from Success24 
# Number of words: 4 
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 40.Task: Count how many uppercase and lowercase letters are in a string.
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------
# 41.Task: Print all characters from the string that are at odd indices. 
# ----------------------------------------------------------------------------------

