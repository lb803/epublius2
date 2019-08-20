#!/usr/bin/env python3
import os
import argparse

class Epublius:
    def __init__(self):
        argv = self.parse_args()
        self.args = self.process_args(argv)

    def parse_args(self, argv=None):
        parser = argparse.ArgumentParser()

        parser.add_argument('epub',
			    help = 'Path to the ePub file to process')

        parser.add_argument('-o', '--output',
			    help = 'Output directory',
			    required = True)

        parser.add_argument('-t', '--title',
			    help = 'Title of the book',
			    required = True)

        parser.add_argument('-i', '--isbn',
			    help = 'ISBN number of the book',
			    required = True)
        
        parser.add_argument('-u', '--url',
			    help = 'URL of book\'s page',
			    required = True)

        return parser.parse_args(argv)

    def process_args(self, parsed_args):
        args = {'epub' : os.path.abspath(parsed_args.epub),
                'output' : os.path.abspath(parsed_args.output),
                'title': parsed_args.title,
                'isbn': parsed_args.isbn,
                'url' : parsed_args.url
        }
        
        return args