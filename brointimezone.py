import pytz, datetime
import pandas as pd
import data

class bro:
    def __init__(self, timeslots, timezone):
        self.timeslots = timeslots
        self.timezone = pytz.timezone(timezone)
        self.gmt_offset = self.timezone.utcoffset(self.timeslots[0][0])
        self.gmt_timedelta = self.convert_to_GMT()
        self.nativezonetime = []
        print("User Created successful.")

    def set(self, timeslots, timezone):
        self.timeslots = timeslots
        self.timezone = pytz.timezone(timezone)
        self.gmt_offset = self.timezone.utcoffset(self.timeslots[0][0])
        self.gmt_timedelta = self.convert_to_GMT()
        self.nativezonetime = []

    def convert_to_GMT(self):
        gmt_list = []
        for timeslot in self.timeslots:
            #print(timeslot)
            list_of_datetime = []
            for n in timeslot:
                list_of_datetime.append(
                    (n - self.gmt_offset) - datetime.datetime(2019, 12, 2, 13, 00)
                    )
            gmt_list.append(list_of_datetime)
        return pd.DataFrame(gmt_list, columns=['Lowerlimit', 'Upperlimit']).sort_values(["Lowerlimit"], ascending=True) 

    def convert_from_GMT(self, lower, upper):
            self.nativezonetime.append(
                [ 
                    (datetime.datetime(2019, 12, 2, 13, 00) + lower + self.gmt_offset ),
                    (datetime.datetime(2019, 12, 2, 13, 00) + upper + self.gmt_offset )
                ]
            )
            print("In GMT Convert")


