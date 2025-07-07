def main():
    time = input("time: ")

    if convert(time) >= 7 and convert(time) <= 8:
        print("Breakfast Time")
        
    elif convert(time) >= 12 and convert(time) <= 13:
        print("Lunch Time")

    if convert(time) >= 18 and convert(time) <= 19:
        print("Dinner Time")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    decimal_time = hours + minutes / 60
    return decimal_time


if __name__ == "__main__":
    main()