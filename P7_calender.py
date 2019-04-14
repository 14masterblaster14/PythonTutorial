#############################
#  17 # Datetime
#############################

import datetime

import pytz

x = datetime.datetime.now()
print(x)  # O/P : 2019-03-23 15:27:57.110657

print(x.year)  # O/P : 2019
print(x.month)  # O/P : 3
print(x.date())  # O/P : 2019-03-23
print(x.day)  # O/P : 23
print(x.hour)  # O/P : 15
print(x.minute)  # O/P : 27
print(x.second)  # O/P : 57
print(x.microsecond)  # O/P : 110657
print(x.tzinfo)  # O/P : None

###
#    strftime() Method
#
#        Directive	        Description	                                                    Example
#
#        %a	                Weekday, short version	                                        Wed
#        %A	                Weekday, full version	                                        Wednesday
#        %w	                Weekday as a number 0-6, 0 is Sunday	                        3
#        %d	                Day of month 01-31	                                            31
#        %b             	Month name, short version	                                    Dec
#        %B	                Month name, full version	                                    December
#        %m	                Month as a number 01-12	                                        12
#        %y	                Year, short version, without century	                        18
#        %Y	                Year, full version	                                            2018
#        %H	                Hour 00-23	                                                    17
#        %I	                Hour 00-12	                                                    05
#        %p	                AM/PM	                                                        PM
#        %M	                Minute 00-59	                                                41
#        %S	                Second 00-59	                                                08
#        %f	                Microsecond 000000-999999	                                    548513
#        %z	                UTC offset	                                                    +0100
#        %Z	                Timezone	                                                    CST
#        %j	                Day number of year 001-366	                                    365
#        %U             	Week number of year, Sunday as the first day of week, 00-53	    52
#        %W	                Week number of year, Monday as the first day of week, 00-53	    52
#        %c	                Local version of date and time	                                Mon Dec 31
#                                                                                           17:41:00 2018
#        %x	                Local version of date	                                        12/31/18
#        %X	                Local version of time	                                        17:41:00
#        %%	                A % character	                                                %
#
###

print(x.strftime("%A"))  # O/P :    Saturday
print(x.strftime("%a"))  # O/P :    Sat

print(x.strftime("%B"))  # O/P :    March
print(x.strftime("%b"))  # O/P :    Mar

print(x.strftime("%C"))  # O/P :    20
print(x.strftime("%c"))  # O/P :    Sat Mar 23 16:05:15 2019

print(x.strftime("%D"))  # O/P :    03/23/19
print(x.strftime("%d"))  # O/P :    23

###
#   Creating Date Objects and timezones
###

y = datetime.datetime(2020, 7, 14)
print(y)  # O/P : 2020-07-14 00:00:00
print(y.tzinfo)  # O/P : None

z = datetime.datetime(2021, 7, 14, 10, 9, 8, 7)
print(z)  # O/P : 2021-07-14 10:09:08.000007

# Default timezone is none and need not to be passed
# But if necessary, we can pass thrugh pytz library

d = datetime.datetime.now()
# timezone = pytz.timezone("America/Los_Angeles")
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(d)
d_aware.tzinfo
print("---")
print(d_aware)  # O/P : 2019-03-24 12:15:59.638161-07:00
print(d_aware.tzinfo)  # O/P : America/Los_Angeles

#  Let's create a datetime object with a UTC timezone, and convert it to Pacific Standard.

utc_now = pytz.utc.localize(datetime.datetime.now())
print(utc_now)  # O/P : 2019-03-24 12:23:22.673501+00:00
print(utc_now.isoformat())  # O/P : 2019-03-24T12:23:22.673501+00:00

pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
print(pst_now)  # O/P : 2019-03-24 05:23:22.673501-07:00
print(pst_now.isoformat())  # O/P : 2019-03-24T05:23:22.673501-07:00

print(utc_now == pst_now)  # O/P : True

###
#   Measuring duration with timedelta
###

my_birthdate = datetime.datetime(1985, 10, 20, 17, 55)
brothers_birthdate = datetime.datetime(1992, 6, 25, 18, 30)

# Since we like to work with offset aware objects, we'll add timezone information.
ind = pytz.timezone("Asia/Kolkata")
my_birthdate = ind.localize(my_birthdate)
brothers_birthdate = ind.localize(brothers_birthdate)

# calculate difference :
# datetime - datetime = timedelta
# datetime - timedelta = datetime

diff = brothers_birthdate - my_birthdate  # timedelta object
print(diff)  # O/P : 2440 days, 0:35:00


# e.g. "what day of the week is 90 days from today?".

today = datetime.datetime.now()
ninety_days = datetime.timedelta(days=90)
target_date = today + ninety_days
print(target_date)  # O/P : 2019-06-22 12:49:53.878513
print(target_date.strftime("%A"))  # O/P : Saturday
