user = input ("What is the Answer to the Ultimate Question of Life, the Universe, and Everything? ").strip().lower()

match user:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print ("No")

        