import datetime

# input
birthday = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)

# goal
# get to 5/1/2012

print parsed_date.strftime("%x") # 01/11/17