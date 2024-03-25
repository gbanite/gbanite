def calculate_total_time(swimming_time, cycling_time, running_time):
    return swimming_time + cycling_time + running_time

def determine_award(total_time):
    if total_time <= 100:
        return "Provincial colours"
    else:
        return "Provincial colours"

def main():
    swimming_time = float(input("Enter swimming time (in minutes): "))
    cycling_time = float(input("Enter cycling time (in minutes): "))
    running_time = float(input("Enter running time (in minutes): "))

    total_time = calculate_total_time(swimming_time, cycling_time, running_time)
    print("Total time taken to complete the triathlon:", total_time, "minutes")

    award = determine_award(total_time)
    print("Award:", award)

if __name__ == "__main__":
    main()


def calculate_total_time(swimming_time, cycling_time, running_time):
    return swimming_time + cycling_time + running_time

def determine_award(total_time):
    if total_time <= 100:
        return "Provincial colours"
    elif 101 <= total_time <= 105:
        return "Provincial half colours"
    else:
        return "Provincial half colours"

def main():
    swimming_time = float(input("Enter swimming time (in minutes): "))
    cycling_time = float(input("Enter cycling time (in minutes): "))
    running_time = float(input("Enter running time (in minutes): "))

    total_time = calculate_total_time(swimming_time, cycling_time, running_time)
    print("Total time taken to complete the triathlon:", total_time, "minutes")

    award = determine_award(total_time)
    print("Award:", award)

if __name__ == "__main__":
    main()

def calculate_total_time(swimming_time, cycling_time, running_time):
    return swimming_time + cycling_time + running_time

def determine_award(total_time):
    if total_time <= 100:
        return "Provincial colours"
    elif 101 <= total_time <= 105:
        return "Provincial half colours"
    elif 106 <= total_time <= 110:
        return "Provincial scroll"
    else:
        return "Provincial scroll"

def main():
    swimming_time = float(input("Enter swimming time (in minutes): "))
    cycling_time = float(input("Enter cycling time (in minutes): "))
    running_time = float(input("Enter running time (in minutes): "))

    total_time = calculate_total_time(swimming_time, cycling_time, running_time)
    print("Total time taken to complete the triathlon:", total_time, "minutes")

    award = determine_award(total_time)
    print("Award:", award)

if __name__ == "__main__":
    main()

def calculate_total_time(swimming_time, cycling_time, running_time):
    return swimming_time + cycling_time + running_time

def determine_award(total_time):
    if total_time >= 111:
        return "No award"
    else:
        return "No award"

def main():
    swimming_time = float(input("Enter swimming time (in minutes): "))
    cycling_time = float(input("Enter cycling time (in minutes): "))
    running_time = float(input("Enter running time (in minutes): "))

    total_time = calculate_total_time(swimming_time, cycling_time, running_time)
    print("Total time taken to complete the triathlon:", total_time, "minutes")

    award = determine_award(total_time)
    print("Award:", award)

if __name__ == "__main__":
    main()
