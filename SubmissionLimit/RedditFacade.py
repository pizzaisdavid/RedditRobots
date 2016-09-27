from RedditWrapper import RedditWrapper
import logging

class RedditFacade(RedditWrapper):
    
    def __init__(self, user_agent, unix_timestamp):
        RedditWrapper.__init__(self, user_agent)
        self.logger = logging.getLogger(__name__)
        self.unix_timestamp = unix_timestamp
        self.logger.info('Initializing with {timestamp} Unix timestamp.'.format(timestamp=unix_timestamp))
        
    def getSubredditSubmissionsWithin(self, subreddit_name, time_limit_in_hours):
        self.logger.debug('Fetching submissions from {subreddit} made within the last {limit} hours.'
                         .format(subreddit=subreddit_name, limit=time_limit_in_hours))
        submission_limit = 100
        submissions_within_time_frame = []
        subreddit = self.reddit.get_subreddit(subreddit_name)
        submissions = subreddit.get_new(limit=submission_limit)
        for s in submissions:
            if self.isWithinTimeLimit(s, time_limit_in_hours):
                submissions_within_time_frame.append(s)
            else:
                break
        self.logger.info('Found {count} submissions made within the past {limit} hours'
                         .format(count=len(submissions_within_time_frame), limit=time_limit_in_hours))
        return submissions_within_time_frame
    
    def isWithinTimeLimit(self, submission, time_limit_in_hours):
        time_limit_in_seconds = time_limit_in_hours * 60 * 60
        deadline = self.unix_timestamp - time_limit_in_seconds;
        return deadline < submission.created_utc