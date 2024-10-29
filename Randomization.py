import string
import random
import time


letters = string.ascii_letters
result = ""
target = "roHAN" 

for letter in target:
    while True:
        l = random.choice(letters)
        print(result + l)
        if l == letter:
            result += l
            break
        time.sleep(0.1)

print("Final result:", result)

