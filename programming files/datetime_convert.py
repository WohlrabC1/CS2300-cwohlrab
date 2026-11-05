from datetime import datetime

# takes a date string and changes dashes to slashes (JL)
date_str = "2022-03-17 10:45:30"
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# prints out the formatted date (JL)
print(formatted_date)
