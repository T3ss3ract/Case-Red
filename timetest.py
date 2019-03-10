import time
import io
from datetime import datetime as dt

from datetime import timedelta
import yaml

print("testing!")

#today = timedelta(5);

#print(today)

def days_between(d1, d2):
    d1 = dt.strptime(d1, "%Y-%m-%d")
    d2 = dt.strptime(d2, "%Y-%m-%d")
    return abs((d2-d1).days)


with open("config.yaml", 'r') as stream:
    config = yaml.load(stream)



for key,val in config.items():
    start_date =  val["start_time"]
    end_date = val["end_time"]
    print(start_date)
    print(end_date)
    print("calculating time between...")
    print(days_between(start_date, end_date))




#date1 = "2019-8-15"
#date2 = "2019-10-3"
#print(days_between(date1, date2))
    
