original = input("Input: ")
new=""
for i in original:
    if i.lower() not in "aeiou":
        new += i
print("Output: ",new) 