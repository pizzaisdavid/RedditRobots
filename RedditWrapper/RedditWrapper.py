import praw
import logging

class RedditWrapper():
    
    def __init__(self, user_agent):
        self.logger = logging.getLogger(__name__)
        self.logger.info('Registering user agent with Reddit.')
        self.reddit = praw.Reddit(user_agent)
        
    def login(self, username, password):
        self.logger.info('Logging into Reddit account: {username}'.format(username=username))
        self.reddit.login(username, password, disable_warning=True)
        self.logger.info('Logged into Reddit.')

