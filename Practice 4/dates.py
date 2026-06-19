# Practice 4 - Dates and Time

from datetime import datetime, date, timedelta, timezone

# 1. Current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# 2. Creating date objects
birthday = date(2006, 5, 15)
print("Birthday:", birthday)

# 3. Date formatting
formatted_date = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date:", formatted_date)

# 4. Calculating time differences
today = date.today()
exam_date = date(2026, 6, 30)
difference = exam_date - today
print("Days until exam:", difference.days)

# 5. Adding days to a date
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)

# 6. Working with timezone
utc_time = datetime.now(timezone.utc)
print("UTC time:", utc_time)
