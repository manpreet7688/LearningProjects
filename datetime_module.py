'''Python has the datetime module to help deal with timestamps in your code.
Time values are represented with the time class. Times have attributes for hour, minute, second, and microsecond.
 They can also include time zone information. The arguments to initialize a time instance are optional,
 but the default of 0 is unlikely to be what you want.'''

'''
Time:
Let's take a look at how we can extract time information from the datetime module. We can create a 
timestamp by specifying datetime.time(hour,minute,second,microsecond)'''

import datetime
t = datetime.time(5,25,1)

# Let's show the different components
print(t)
print("hour: ", + t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

'''Note: A time instance only holds values of time, and not a date associated with the time.

We can also check the min and max values a time of day can have in the module:'''

print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)

'''
Date:
datetime also allows us to work with date timestamps. Calender date values are represented with
the date class. Instances have attributes for year, month, and day.
it is easy to create a date representinng today's date using the today() method.
'''

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)

print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)

'''Another way to create new date instances uses the replace() method of an existing date. 
For example, you can change the year, leaving the day and month alone.'''

d1 = datetime.date(2015,3,11)
print("date value of d1 is ", d1)

d2 = d1.replace(year=1990)
print d2

# Arithematic

'''We can perform arithmetic on date objects to check for time differences.'''

print(d1-d2)

'''This gives us the difference in days between the two dates. You can use the timedelta method to specify various units of times (days, minutes, hours, etc.)

'''