import pytest
from unittest.mock import Mock
import datetime
import time

#import MockRedditHelper 
from .RedditFacade import RedditFacade

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

def test_getSubredditSubmissionsWithin():
    YEAR = 2014
    MONTH = 11
    DAY = 22
    HOUR = 14
    MINUTE = 59
    mock_reddit = makeMockReddit(
        makeMockSubreddit([
            makeMockSubmission('username', makeUnixTimestamp(YEAR, MONTH, DAY, HOUR, MINUTE)),
            makeMockSubmission('username', makeUnixTimestamp(YEAR, MONTH, DAY, HOUR, MINUTE - 9)),
            makeMockSubmission('username', makeUnixTimestamp(YEAR, MONTH, DAY - 2, HOUR, MINUTE))
        ])
    )
    
    reddit_facade = RedditFacade(mock_reddit, makeUnixTimestamp(YEAR, MONTH, DAY, HOUR, MINUTE))
    new_submissions = reddit_facade.getSubredditSubmissionsWithin('subreddit', 24)
    
    assert len(new_submissions) == 2