#!/usr/bin/env python3
import sys
sys.path.append('modules')
from epublius import Epublius

def main():
    # Create instances
    epublius = Epublius()

    # Program execution

    ## DEBUG
    print(epublius.args)

if __name__ == '__main__':
    main()
