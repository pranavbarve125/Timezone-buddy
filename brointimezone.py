import pytz, datetime
import pandas as pd
class bro:
    def __init__(self, timeslots, timezone):
        self.timeslots = timeslots
        self.timezone = pytz.timezone(timezone)
        self.gmt_timedelta = self.convert_to_GMT()
        #self.nativezonetime = nativezonetime

    def set(self, timeslots, timezone):
        self.timeslots = timeslots
        self.timezone = pytz.timezone(timezone)
        self.gmt_timedelta = self.convert_to_GMT()
        #self.nativezonetime = nativezonetime

    def convert_to_GMT(self):
        gmt_list = []
        for timeslot in self.timeslots:
            #print(timeslot)
            list_of_datetime = []
            for n in timeslot:
                list_of_datetime.append(
                    (n - self.timezone.utcoffset(n)) - datetime.datetime(2019, 12, 2, 13, 00)
                    )
            gmt_list.append(list_of_datetime)
        return pd.DataFrame(gmt_list, columns=['Lowerlimit', 'Upperlimit']).sort_values(["Lowerlimit"], ascending=True) 

    def convert_from_GMT(self):
        pass

