#  19. Write a Python program to filter out duplicate characters from a string entered by the user.

word_str = "raghaw"
result = ""

for i in word_str:
    if i not in result:
        result = result + i

print(result)