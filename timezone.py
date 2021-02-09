import datetime as dt 
from dateutil import tz 


tz_string = dt.datetime.now(dt.timezone.utc).astimezone().tzname() 

print("datetime.now() :", tz_string) 

NYC = tz.gettz('America / Portland, OR') 
dt1 = dt.datetime(2015, 5, 21, 12, 0) 
dt2 = dt.datetime(2015, 12, 21, 12, 0, tzinfo = NYC) 

print("Naive Object :", dt1.tzname()) 
print("Aware Object :", dt2.tzname()) 
