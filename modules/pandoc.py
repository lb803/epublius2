#!/usr/bin/env python3
import os
import subprocess

class Pandoc():
    def __init__(self, config):
        self.config = config
        
    def convert_files(self, content, metadata):
            
        cmd = ['pandoc', '-s',
               '--template', os.path.abspath(self.config['template']),
               '--metadata-file={}'.format(metadata),
               content['input_path'],
               '-o', content['output_path'],
               '--to=html5']

        try:
            p = subprocess.Popen(cmd,
                                 stdout = subprocess.PIPE,
                                 stderr = subprocess.PIPE)
            stdout, stderr = p.communicate()

            assert p.returncode == 0
            
        except AssertionError:
            print('[ERROR] Standard error of subprocess: {}' \
                  .format(stderr))
            raise

