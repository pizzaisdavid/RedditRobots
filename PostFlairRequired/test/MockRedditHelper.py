from unittest.mock import Mock
import datetime
import time
from _overlapped import NULL

def makeMockReddit(subreddit):
    reddit = Mock()
    reddit.get_subreddit.return_value=subreddit
    return reddit

def makeMockSubreddit(submissions=[]):
    subreddit = Mock()
    subreddit.get_new.return_value = submissions
    return subreddit

def makeMockSubmission(author="username", timestamp=None):
    submission = Mock()
    submission.author.name = author
    submission.created_utc = timestamp
    return submission

def makeUnixTimestamp(year, month, day, hour, minute):
    timestamp = datetime.datetime(year, month, day, hour, minute, tzinfo=datetime.timezone.utc)
    return time.mktime(timestamp.timetuple())

def toSeconds(days=0, hours=0, minutes=0, seconds=0):
    secondsInDays = days * 86400
    secondsInHours = hours * 3600
    secondsInMinutes = minutes * 60
    return secondsInDays + secondsInHours + secondsInMinutes + seconds;
    