from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():
    print(f"Current date and time: {current_date}")

number_of_days = int(input("Enter the number of days to add to the current date: "))   
def calculate_future_date():
    future_date = current_date + timedelta(days = number_of_days )
    print(f"Future date: {future_date.strftime('%Y-%M-%D')}")
    