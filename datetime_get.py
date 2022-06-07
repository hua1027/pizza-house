import datetime

# setup dates
previous_date = datetime.datetime.strptime("05-21-2022", '%m-%d-%Y')
today = datetime.datetime.today()

# compute difference
nowadays = (today - previous_date).days
