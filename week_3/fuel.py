while True:
    try:
        value = input("Enter your value: ")
        numerator, denominator = value.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        
        if denominator == 0:
            raise ZeroDivisionError
        
        if numerator < 0 or denominator < 0:
            continue
            
        fraction = numerator / denominator
        
        if fraction > 1:
            continue
            
        percentage = round(fraction * 100)
        
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break
        
    except (ValueError, ZeroDivisionError):
        pass

