# -*- coding: utf-8 -*-
# from: http://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library

import calendar

from datetime import date

def add_months(sourcedate,months):
     month = sourcedate.month - 1 + months
     year = int(sourcedate.year + month / 12 )
     month = month % 12 + 1
     day = min(sourcedate.day,calendar.monthrange(year,month)[1])
     return date(year,month,day)
