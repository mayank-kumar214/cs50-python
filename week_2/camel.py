camelCase = input("Enter a camel case string:")
snake_Case= ""
for i in camelCase:
    if i.islower():
       snake_Case = snake_Case+i
    else:
        snake_Case = snake_Case+"_"+i.lower()
print("Snake_Case:",snake_Case)