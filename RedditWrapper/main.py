from RedditFacade import RedditFacade
import logging

import Settings

logging.basicConfig(level=logging.DEBUG)

def main():
    logger = logging.getLogger(__name__)
    logger.info('Initializing.')
    r = RedditFacade(Settings.user_agent)
    #r.login(Settings.username, Settings.password)
    
    
    
    
    
    

if __name__ == '__main__':
    main()
