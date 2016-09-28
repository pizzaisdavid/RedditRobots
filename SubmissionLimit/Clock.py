import calendar
import time


def getCurrentUnixTime():
    return calendar.timegm(time.gmtime())