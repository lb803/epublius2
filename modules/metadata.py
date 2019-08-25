#!/usr/bin/env python3
import os
import tempfile
import datetime
import json

class Metadata:
    def __init__(self, config, args):
        self.config = config
        self.args = args

    def get_metadata(self, contents, index):

        metadata = {# Page specific
                    'lang': 'en',
                    'date': datetime.datetime.now().isoformat(),

                    # Links
                    'css': contents[index]['css'],

                    # Menu
                    'bookpage': self.args['url'],
                    'contents': self.config['contents'],
                    'copyright': self.config['copyright'],
                    'current_page_url': self.get_page_url(contents, index),
            
                    # Bootstrap breadcrumb
                    'booktitle': self.args['title'],
                    'pagetitle': contents[index]['content_name'],                    
                    # Footer
                    'prev': contents[index-1]['output_file'],
                    'next': self.get_next(contents, index)
        }
        metadata_file = self.write_metadata(metadata)

        return metadata_file
        
    def write_metadata(self, metadata):
        with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8',
                                         suffix='.json', delete=False) as tf:
            json.dump(metadata, tf)

        return tf.name

    def get_page_url(self, contents, index):
        url_items = [self.config['reader_url'],
                     self.args['isbn'],
                     contents[index]['output_file']
        ]

        return '/'.join(url_items)

    def get_next(self, contents, index):
        # metadata['next'] takes the value of the following book section.
        # In the special case of the last chapter, takes the first section.
        try:
            next = contents[index+1]['output_file']
        except IndexError:
            next = contents[0]['output_file']

        return next
    
    def cleanup(self, metadata):
        os.remove(metadata)
