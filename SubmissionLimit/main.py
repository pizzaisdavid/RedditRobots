import logging

import Credentials
import Settings
from RedditFacade import RedditFacade
from FrequencyTable import buildUserSubmissionFrequencyTable



logging.basicConfig(level=logging.DEBUG)

def main():
    logger = logging.getLogger(__name__)
    logger.info('Initializing.')
    r = RedditFacade.factory(Settings.user_agent)
    r.login(Credentials.username, Credentials.password)
    submissions = r.getSubredditSubmissionsWithin(Settings.subreddit_name, Settings.time_frame)
    table = buildUserSubmissionFrequencyTable(submissions)
    
    for s in submissions:
        print(s)

def buildSubmissionTable(submissions):
    return submissions
        
if __name__ == '__main__':
    main()