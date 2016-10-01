import pytest
from unittest.mock import Mock
import datetime
import time
import logging

from .MockRedditHelper import *
from ..src.RedditFacade import RedditFacade

logging.basicConfig(level=logging.DEBUG)

def test_getSubredditSubmissionsWithin():
    YEAR = 2014
    MONTH = 11
    DAY = 22
    HOUR = 14
    MINUTE = 59
    UNIX_TIMESTAMP = makeUnixTimestamp(YEAR, MONTH, DAY, HOUR, MINUTE)
    mock_reddit = makeMockReddit(
        makeMockSubreddit(submissions=[
            makeMockSubmission(timestamp=UNIX_TIMESTAMP),
            makeMockSubmission(timestamp=UNIX_TIMESTAMP - toSeconds(minutes=9)),
            makeMockSubmission(timestamp=UNIX_TIMESTAMP - toSeconds(days=3))
        ])
    )
    
    reddit_facade = RedditFacade(mock_reddit, UNIX_TIMESTAMP)
    new_submissions = reddit_facade.getSubredditSubmissionsWithin('subreddit', time_limit_in_hours=24)
    
    assert len(new_submissions) == 2