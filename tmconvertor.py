from brointimezone import bro
import datetime
import pytz
import pandas as pd
import data
# https://www.youtube.com/watch?v=eirjjyP2qcQ
#process before taking inputs from all the users.
# step 0: enter a particular set of favourable 24 hours. Those 24 hours will be shown to all the users in native time zones. 
start_24_hours = datetime.datetime(2019, 12, 2, 00, 00)
end_24_hours = start_24_hours + datetime.timedelta(days=1)
# bro.start = start_24_hours

# inputs from various users
# step1 : number of freezones
# step2 : taking input for the freezones
User1 = bro([
                [datetime.datetime(2019, 12, 2, 16, 0), datetime.datetime(2019, 12, 2, 18, 0)],
                [datetime.datetime(2019, 12, 2, 23, 0), datetime.datetime(2019, 12, 3, 5, 0)],
                [datetime.datetime(2019, 12, 3, 7, 0), datetime.datetime(2019, 12, 3, 10, 0)],
                [datetime.datetime(2019, 12, 3, 11, 0), datetime.datetime(2019, 12, 3, 12, 0)]
            ], 
            'Antarctica/McMurdo')#+13:00
User2 = bro([
                [datetime.datetime(2019, 12, 2, 13, 0), datetime.datetime(2019, 12, 2, 16, 0)],
                [datetime.datetime(2019, 12, 2, 17, 0), datetime.datetime(2019, 12, 2, 19, 0)],
                [datetime.datetime(2019, 12, 2, 2, 0), datetime.datetime(2019, 12, 2, 5, 0)],
                [datetime.datetime(2019, 12, 2, 9, 0), datetime.datetime(2019, 12, 2, 11, 30)]
            ],
            'Israel')#+2:00 GMT : 
User3 = bro([
                [datetime.datetime(2019, 12, 2, 10, 30), datetime.datetime(2019, 12, 2, 13, 30)],
                [datetime.datetime(2019, 12, 2, 17, 30), datetime.datetime(2019, 12, 2, 20, 30)],
                [datetime.datetime(2019, 12, 2, 11, 30), datetime.datetime(2019, 12, 2, 15, 30)],
                [datetime.datetime(2019, 12, 2, 22, 30), datetime.datetime(2019, 12, 2, 23, 30)]
            ],
            'Asia/Kolkata')#+5:30  
User4 = bro([
                [datetime.datetime(2019, 12, 2, 4, 0), datetime.datetime(2019, 12, 2, 10, 0)],
                [datetime.datetime(2019, 12, 2, 11, 0), datetime.datetime(2019, 12, 2, 14, 0)],
                [datetime.datetime(2019, 12, 2, 15, 0), datetime.datetime(2019, 12, 2, 17, 30)],
                [datetime.datetime(2019, 12, 2, 19, 0), datetime.datetime(2019, 12, 2, 21, 0)]
            ],
            'Asia/Dubai')#+4:00 
# GMT common time for all the 3 users should be 14:00 to 15:00
itr = iter([User2,User3,User4])
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
        data.clashes.append([lower, upper])#saving the GMT
        User1.convert_from_GMT(lower, upper)
        User2.convert_from_GMT(lower, upper)
        User3.convert_from_GMT(lower, upper)
        User4.convert_from_GMT(lower, upper)
        print("IN")
        return
def wrapper_calculate_clashes():
    base_list = User1.gmt_timedelta
    # print(base_list)
    for rows, col in base_list.iterrows():
        calculate_clashes(col[0], col[1])
    return data.clashes

# display the common time periods for all the time zones respectively
# step6 : display the converted zones to respective users 
# if data.clashes == []:
#     print("No common timming.")
# else:
#     for each in data.clashes:
#         each[0] = start_24_hours + each[0]
#         each[1] = start_24_hours + each[1]
#     print(data.clashes)


# print("User 1 : " + str(User1.nativezonetime) + "\n")
# print("User 2 : " + str(User2.nativezonetime) + "\n")
# print("User 3 : " + str(User3.nativezonetime) + "\n")
# print("User 4 : " + str(User4.nativezonetime) + "\n")