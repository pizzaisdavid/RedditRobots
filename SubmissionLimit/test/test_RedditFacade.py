import pytest
from unittest.mock import Mock
import datetime
import time
import logging

from .MockRedditHelper import *
from ..RedditFacade import RedditFacade

logging.basicConfig(level=logging.DEBUG)

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