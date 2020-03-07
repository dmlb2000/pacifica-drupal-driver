#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Used to load in all the Drupal driver environment variables.

Wrapped all in if statements so that they can be used in
unit test environment
"""
from os.path import expanduser, join
from os import getenv


CONFIG_FILE = getenv('DRUPAL_DRIVER_CONFIG', join(
    expanduser('~'), '.pacifica-drupal-driver', 'config.ini'))
