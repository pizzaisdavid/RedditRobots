from RedditFacade import RedditFacade
import logging

import Credentials
import Settings


logging.basicConfig(level=logging.DEBUG)

def main():
    logger = logging.getLogger(__name__)
    logger.info('Initializing.')
    r = RedditFacade(Settings.user_agent)
    r.login(Credentials.username, Credentails.password)
    
    
    
    
    
    

if __name__ == '__main__':
    main()
