"""
Python Printing Methods - Learning Notes
Order: Most Recommended -> Less Common

1. print() with commas            Beginner friendly
2. f-strings                      Most recommended (Python 3.6+)
3. str.format()                   Older but still useful
4. String concatenation (+)       Requires str() for numbers
5. Percent formatting (%)         Legacy style

Extra:
- sep parameter
- end parameter
"""

# =====================================================
# 1. print() with commas (Easy for beginners)
# =====================================================

name = "Aman"
age = 22

print("1. Comma Style")
print("My name is", name, "and age is", age)

# When to use:
# - Quick debugging
# - Beginner practice
# - Simple output


# =====================================================
# 2. f-Strings (RECOMMENDED)
# =====================================================

print("\n2. f-String Style")
print(f"My name is {name} and age is {age}")

# When to use:
# - Real projects
# - Clean and readable code
# - Most common modern Python style

# Example:
a = 10
b = 20

print(f"Sum of {a} and {b} = {a + b}")


# =====================================================
# 3. str.format()
# =====================================================

print("\n3. format() Style")
print("My name is {} and age is {}".format(name, age))

# Named placeholders
print("My name is {n} and age is {a}".format(n=name, a=age))

# When to use:
# - Older codebases
# - Older codebases
# - Before f-strings existed


# =====================================================
# 4. String Concatenation (+)
# =====================================================

print("\n4. Concatenation Style")
print("My name is " + name)

# Numbers must be converted to string
print("Age is " + str(age))

# When to use:
# - Small string joins
# - Not preferred for complex output


# =====================================================
# 5. Percent Formatting (Legacy)
# =====================================================

print("\n5. Percent Formatting Style")
print("My name is %s and age is %d" % (name, age))

# When to use:
# - Reading old Python code
# - Legacy systems


# =====================================================
# EXTRA: sep Parameter
# =====================================================

print("\n6. sep Parameter")
print("Python", "Java", "C++", sep=" | ")

# Output:
# Python | Java | C++


# =====================================================
# EXTRA: end Parameter
# =====================================================

print("\n7. end Parameter")

print("Hello", end=" ")
print("World")

# Output:
# Hello World


# =====================================================
# RECOMMENDED ORDER TO LEARN
# =====================================================

"""
1. print() with commas
2. f-strings
3. sep and end
4. str.format()
5. String concatenation
6. Percent formatting

For interviews and real projects:
- Mostly use f-strings
- Sometimes use comma style for debugging
- Understand format() and % formatting when reading old code
"""
