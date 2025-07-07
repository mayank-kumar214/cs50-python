text = input("Enter your words: ").split()
for i in range(len(text)):
    if i != len(text) - 1: 
        print(f"{text[i]}...", end='')
    else:
        print(text[i], end='')
