from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
