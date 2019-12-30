from brointimezone import bro
import datetime
import pytz
# https://www.youtube.com/watch?v=eirjjyP2qcQ
#process before taking inputs from all the users.
# step 0: enter a particular set of favourable 24 hours. Those 24 hours will be shown to all the users in native time zones. 
start_24_hours = datetime.datetime(2019, 12, 31, 21, 35)
end_24_hours = start_24_hours + datetime.timedelta(hours=4)

# inputs from various users
# step1 : number of freezones
# step2 : taking input for the freezones
User1 = bro({
                [datetime.datetime(), datetime.datetime()]
            },
            'Antarctica/McMurdo')#+13:00
User2 = bro(,'Israel')#+2:00
User3 = bro(,'Asia/Kolkata')#+5:30

# trying to find common time timethrough GMT + 0
# step3 : converting all the data to GMT
# step4 : scale all the time between 0.0 to 24.0 and look for clashes
# step5 : convert all the clashes back to native timezones

# display the common time periods for all the time zones respectively
# step6 : display the converted zones to respective users 