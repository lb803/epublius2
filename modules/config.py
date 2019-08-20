#!/usr/bin/env python3
import os
import configparser

class Config:
    def __init__(self):
        CONFIG_PATH = os.path.abspath('config.ini')
        self.config = configparser.ConfigParser()
        
        try:
            with open(CONFIG_PATH, 'r') as config_file:
                self.config.read_file(config_file)
        except IOError as e:
            print('IOError: Is your config file missing? {}'.format(e))

    def get_config(self, section):
        return self.config[section]
