def convert(words):
    words = words.replace(":)", "😊")
    words = words.replace(":(", "😞")
    return words

def main():
    words = input("Enter your lines: ")
    words = convert(words)
    print(words)

main()
