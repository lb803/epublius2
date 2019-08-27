#!/usr/bin/env python3
import sys
sys.path.append('modules')
from epublius import Epublius
from config import Config
from metadata import Metadata
from pandoc import Pandoc

def main():
    # Create instances
    config = Config()
    epublius = Epublius(config.get_config('epublius'))
    metadata = Metadata(config.get_config('metadata'),
                        epublius.args)
    pandoc = Pandoc(config.get_config('pandoc'))
    
    # Program execution
    epublius.unzip_epub()

    ## Get ebook contents
    contents = epublius.get_contents()

    for index, content in enumerate(contents):
        ## Gather metadata and convert files to HTML5
        metadata_path = metadata.get_metadata(contents, index)
        pandoc.convert_files(content, metadata_path)
        metadata.cleanup(metadata_path)

        ## Fix links in content (as the file extension is now .html)
        epublius.manipulate_links(content)
        
    epublius.cleanup()
    
if __name__ == '__main__':
    main()
