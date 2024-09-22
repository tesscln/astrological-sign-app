from datetime import datetime

# Function to determine astrological sign based on date of birth
def get_astrological_sign(month, day):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Unknown"

# Main program
def main():
    name = input("What's your name? ")
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")

    # Parse date and hour
    try:
        date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
        sign = get_astrological_sign(date_obj.month, date_obj.day)

        print(f"\nHello, {name}! You were born on {date_obj.strftime('%B %d, %Y')}")
        print(f"Your astrological sign is {sign}.")
    except ValueError:
        print("Invalid date or time format. Please try again.")

if __name__ == "__main__":
    main()
