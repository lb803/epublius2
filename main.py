#!/usr/bin/env python3
import sys
sys.path.append('modules')
from epublius import Epublius
from config import Config

def main():
    # Create instances
    config = Config()
    epublius = Epublius(config.get_config('epublius'))

    # Program execution
    epublius.unzip_epub()

    contents = epublius.get_contents()

    ## DEBUG
    for c in contents:
        print('---')
        print(c)
        
    epublius.cleanup()
    
if __name__ == '__main__':
    main()
