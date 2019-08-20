#!/usr/bin/env python3
import sys
sys.path.append('modules')
from epublius import Epublius
from config import Config
from metadata import Metadata

def main():
    # Create instances
    config = Config()
    epublius = Epublius(config.get_config('epublius'))
    metadata = Metadata(config.get_config('metadata'),
                        epublius.args)

    # Program execution
    epublius.unzip_epub()

    contents = epublius.get_contents()

    for index, content in enumerate(contents):
        metadata_path = metadata.get_metadata(contents, index)

        ## Debug
        print(metadata_path)
        
        metadata.cleanup(metadata_path)
        
    epublius.cleanup()
    
if __name__ == '__main__':
    main()
