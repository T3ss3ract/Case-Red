import time
import io
from datetime import datetime as dt

from datetime import timedelta

print("testing!")

#today = timedelta(5);

#print(today)

def days_between(d1, d2):
    d1 = dt.strptime(d1, "%Y-%m-%d")
    d2 = dt.strptime(d2, "%Y-%m-%d")
    return abs((d2-d1).days)



date1 = "2019-8-15"
date2 = "2019-10-3"
print(days_between(date1, date2))
    
