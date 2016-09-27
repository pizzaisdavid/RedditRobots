from unittest.mock import Mock
import datetime
import time

def makeMockReddit(subreddit):
    reddit = Mock()
    reddit.get_subreddit.return_value=subreddit
    return reddit

def makeMockSubreddit(submissions):
    subreddit = Mock()
    subreddit.get_new.return_value = submissions
    return subreddit

def makeMockSubmission(username, timestamp):
    submission = Mock()
    submission.author.name = username
    submission.created_utc = timestamp
    return submission

def makeUnixTimestamp(year, month, day, hour, minute):
    timestamp = datetime.datetime(year, month, day, hour, minute, tzinfo=datetime.timezone.utc)
    return time.mktime(timestamp.timetuple())