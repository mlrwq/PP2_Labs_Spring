from datetime import *

current_date = datetime.now()
drop_microsec = current_date.replace(microsecond = 0)

print(drop_microsec)