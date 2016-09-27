from RedditFacade import RedditFacade
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
    
    submissions = r.getSubredditSubmissionsWithin(Settings.subreddit_name,
                                                  Settings.time_frame)
    
    for s in submissions:
        print(s)
        
def get_date(submission):
    time = submission.created_utc
    return datetime.datetime.fromtimestamp(time)

def getCurrentTime():
    return calendar.timegm(time.gmtime())
        
if __name__ == '__main__':
    main()