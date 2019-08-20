#!/usr/bin/env python3
import os
import argparse
import tempfile
import zipfile
import shutil
from bs4 import BeautifulSoup

class Epublius:
    def __init__(self, config):
        self.config = config

        argv = self.parse_args()
        self.args = self.process_args(argv)

        self.tmp_dir = tempfile.mkdtemp()

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

    def unzip_epub(self):
        with zipfile.ZipFile(self.args['epub'], 'r') as file:
            file.extractall(self.tmp_dir)

    def cleanup(self):
        shutil.rmtree(self.tmp_dir)

    def get_contents(self):
        contents = self.parse_toc()

        for index, content in enumerate(contents):
            input_path = os.path.join(self.tmp_dir,
                                      self.config['ch_dir'],
                                      content['input_file']
            )

            output_file = content['input_file'].replace('.xhtml', '.html')
            
            content_data = {'index': index,
                            'output_file': output_file,
                            'doi': self.get_doi(input_path),
                            'input_path': input_path,
                            'output_path': os.path.join(self.args['output'],
                                                        output_file),
                            'css': self.get_css(input_path)
            }
            
            contents[index].update(content_data)

        return contents
        
    def parse_toc(self):
        toc_path = os.path.join(self.tmp_dir,
                                self.config['toc_dir'],
                                self.config['toc_file']) 

        with open(toc_path, 'r') as toc:
            soup = BeautifulSoup(toc, 'html.parser')
            listing = soup.find(id='toc').find_all('a')

        contents = []
        
        for content in listing:
            content_data = {'input_file': content['href'],
                            'content_name': content.string
            }
            contents.append(content_data)

        return contents

    def get_doi(self, chapter):
        with open(chapter, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')

            doi = soup.find('span', self.config['doi_class'])
            if doi:
                return doi.string
            else:
                return False

    def get_css(self, chapter):
        with open(chapter, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')

            entries = soup.findAll('link', rel='stylesheet')
            css_paths = [css['href'] for css in entries]

            return css_paths
