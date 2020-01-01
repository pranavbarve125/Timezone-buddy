from brointimezone import bro
import datetime
import pytz
import pandas as pd
# https://www.youtube.com/watch?v=eirjjyP2qcQ
#process before taking inputs from all the users.
# step 0: enter a particular set of favourable 24 hours. Those 24 hours will be shown to all the users in native time zones. 
start_24_hours = datetime.datetime(2019, 12, 2, 13, 00)
end_24_hours = start_24_hours + datetime.timedelta(days=1)
# bro.start = start_24_hours
clashes = []

# inputs from various users
# step1 : number of freezones
# step2 : taking input for the freezones
User1 = bro([
                [datetime.datetime(2019, 12, 3, 2, 0), datetime.datetime(2019, 12, 3, 5, 0)]
                #,[datetime.datetime(2019, 12, 2, 16, 0), datetime.datetime(2019, 12, 2, 19, 0)]
            ], 
            'Antarctica/McMurdo')#+13:00  GMT : 13:00 to 16:00
User2 = bro([
                [datetime.datetime(2019, 12, 2, 16, 0), datetime.datetime(2019, 12, 2, 19, 0)]
            ],
            'Israel')#+2:00 GMT : 14:00 to 17:00
User3 = bro([
                [datetime.datetime(2019, 12, 2, 17, 30), datetime.datetime(2019, 12, 2, 20, 30)]
            ],
            'Asia/Kolkata')#+5:30 GMT : 12:00 to 15:00 
# GMT common time for all the 3 users should be 14:00 to 15:00

# trying to find common time timethrough GMT + 0
# step3 : converting all the data to GMT
# step4 : measure all the timedeltas and look for clashes with user1 
# step5 : convert all the clashes back to native timezones
def calculate_clashes(lower, upper):
    try: 
        deltas = next(itr).gmt_timedelta
        for rows, col in deltas.iterrows():
            lower_to_compare = col[0]
            upper_to_compare = col[1]
            if upper_to_compare <= lower:
                continue
            elif lower_to_compare >= upper:
                break
            else:
                if lower_to_compare <= lower:
                    if upper_to_compare <= upper:#1-5
                        calculate_clashes(lower,upper_to_compare)
                    else:#1-6
                        calculate_clashes(lower,upper)
                else:
                    if upper_to_compare <= upper:#2-5
                        calculate_clashes(lower_to_compare,upper_to_compare)
                    else:#2-6
                        calculate_clashes(lower_to_compare, upper)
        return
    except StopIteration:
        clashes.append([lower, upper])
        return
itr = iter([User2,User3])
base_list = User1.gmt_timedelta
# print(base_list)
for rows, col in base_list.iterrows():
    calculate_clashes(col[0], col[1])

# display the common time periods for all the time zones respectively
# step6 : display the converted zones to respective users 
for each in clashes:
    each[0] = start_24_hours + each[0]
    each[1] = start_24_hours + each[1]

print(clashes)