
import datetime
def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_date)

def calculate_future_date():
         from datetime import datetime, timedelta
         adid = int(input("Enter the number of days to add to the current date: "))
         print("Future date: ", current_date + timedelta(days=adid))


display_current_datetime()
calculate_future_date()




