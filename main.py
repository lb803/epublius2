#!/usr/bin/env python3
import sys
sys.path.append('modules')
from epublius import Epublius
from config import Config

def main():
    # Create instances
    config = Config()
    epublius = Epublius()

    # Program execution
    epublius.unzip_epub()

    ## DEBUG
    import os
    print(os.listdir(epublius.tmp_dir))

    epublius.cleanup()
    
if __name__ == '__main__':
    main()
