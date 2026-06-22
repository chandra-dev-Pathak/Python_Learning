#  19. Write a Python program to filter out duplicate characters from a string entered by the user.

duplicate = "a"
word_str = "raghaw"
count = 0

for i in word_str:
    if duplicate in i:
        count += 1
        if count >= 2:
            continue
    else:
        print(i)