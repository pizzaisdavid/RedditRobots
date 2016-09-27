import praw
import logging

class RedditFacade():
    
    def __init__(self, user_agent, unix_timestamp):
        self.logger = logging.getLogger(__name__)
        self.reddit = praw.Reddit(user_agent)
        self.unix_timestamp = unix_timestamp
        self.logger.info('Initializing with {timestamp} Unix timestamp.'.format(timestamp=unix_timestamp))
        
    def __init__(self, reddit, unix_timestamp):
        self.logger = logging.getLogger(__name__)
        self.reddit = reddit
        self.unix_timestamp = unix_timestamp
        self.logger.info('Initializing with {timestamp} Unix timestamp.'.format(timestamp=unix_timestamp))
        
    def login(self, username, password):
        self.logger.info('Logging into Reddit {username} account.'.format(username=username))
        self.reddit.login(username, password, disable_warning=True)
        self.logger.info('Logged into Reddit.')
        
    def getSubredditSubmissionsWithin(self, subreddit_name, time_limit_in_hours, submission_limit=100):
        self.logger.debug('Fetching submissions from {subreddit} made within the last {limit} hours.'.format(subreddit=subreddit_name, limit=time_limit_in_hours))
        submissions_within_time_frame = []
        subreddit = self.reddit.get_subreddit(subreddit_name)
        submissions = subreddit.get_new(limit=submission_limit)
        for s in submissions:
            if self.isWithinTimeLimit(s, time_limit_in_hours):
                submissions_within_time_frame.append(s)
            else:
                break
        self.logger.info('Found {count} submissions made within the past {limit} hours'.format(count=len(submissions_within_time_frame), limit=time_limit_in_hours))
        return submissions_within_time_frame
    
    def isWithinTimeLimit(self, submission, time_limit_in_hours):
        time_limit_in_seconds = time_limit_in_hours * 60 * 60
        deadline = self.unix_timestamp - time_limit_in_seconds;
        return deadline < submission.created_utc