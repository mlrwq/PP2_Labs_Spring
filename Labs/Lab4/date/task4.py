from datetime import datetime

date_format = "%Y-%m-%d %H:%M:%S"
date1 = input()
date2 = input()

datetime1 = datetime.strptime(date1, date_format)
datetime2 = datetime.strptime(date2, date_format)

difference = abs((datetime2 - datetime1).total_seconds())

print("Difference in seconds:", difference)
