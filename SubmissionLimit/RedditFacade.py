import RedditWrapper
import logging

class RedditFacade(RedditWrapper):
    
    def __init__(self, user_agent):
        RedditWrapper.__init__(self, user_agent)
        self.logger = logging.getLogger(__name__)
        self.logger.info('Initializing.')
        
    def test_(self):
        pass