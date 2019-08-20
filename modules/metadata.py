#!/usr/bin/env python3
import os
import tempfile
import datetime

class Metadata:
    def __init__(self, config, args):
        self.config = config
        self.args = args

    def get_metadata(self, contents, index):

        data = {'lang': 'en',
                'date': datetime.datetime.now().isoformat(),
                'booktitle': self.args['title'],
                'bookpage': self.args['url'],
                'contents': self.config['contents'],
                'copyright': self.config['copyright'],
                'current_page_url': self.get_page_url(contents, index), 
                'prev': contents[index-1]['output_file'],
                'pagetitle': contents[index]['content_name']
        }
        try:
            data['next'] = contents[index+1]['output_file']
        except IndexError:
            data['next'] = contents[0]['output_file']

        metadata_file_path = os.path.abspath(self.config['metadata'])
        with open(metadata_file_path, 'r') as f:
            metadata = f.read().format(**data)

        #if contents[index]['doi']:
            # TODO Work on this

        metadata_file = self.write_metadata(metadata)

        return metadata_file
        
    def write_metadata(self, metadata):
        with tempfile.NamedTemporaryFile(mode='w+',
                                         encoding='utf-8',
                                         suffix='.yaml',
                                         delete=False) as tf:
            tf.write(metadata)
            tf.seek(0)

        return tf.name

    def get_page_url(self, contents, index):
        url_items = [self.config['reader_url'],
                     self.args['isbn'],
                     contents[index]['output_file']
        ]

        return '/'.join(url_items)

    def cleanup(self, metadata):
        os.remove(metadata)
