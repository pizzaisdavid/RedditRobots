from RedditFacade import RedditFacade
from FrequencyTable import buildUserSubmissionFrequencyTable
import logging
import datetime
import calendar
import time

import Credentials
import Settings


logging.basicConfig(level=logging.DEBUG)

def main():
    logger = logging.getLogger(__name__)
    logger.info('Initializing.')
    unix_timestamp = getCurrentTime()
    r = RedditFacade(Settings.user_agent, unix_timestamp)
    r.login(Credentials.username, Credentials.password)
    
    submissions = r.getSubredditSubmissionsWithin(Settings.subreddit_name, Settings.time_frame)
    
    table = buildUserSubmissionFrequencyTable(submssions)
    
    for s in submissions:
        print(s)

def getCurrentTime():
    return calendar.timegm(time.gmtime())

def buildSubmissionTable(submissions):
    return submissions
        
if __name__ == '__main__':
    main()