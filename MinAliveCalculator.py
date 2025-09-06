#Age into Minutes

def calculate_minutes(age_years):
    DAYS_IN_YEARS = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = DAYS_IN_YEARS * age_years
    total_hours = HOURS_IN_DAY * total_days
    total_minutes = MINUTES_IN_HOUR * total_hours

    return round(total_days), round(total_hours), round(total_minutes)


while True:
    try:
        age = float(input("Enter your age in years: "))
        days, hours, minutes = calculate_minutes(age)

        print("\n you are aprrox: ")
        print(f"{days} days old")
        print(f"{hours} hours old")
        print(f"{minutes} minutes old\n")

        again = input("would you ike to try again? (y/n): ").lower()

        if again != "y":
            break
    except:3
        print("Please enter a valid number for age")

