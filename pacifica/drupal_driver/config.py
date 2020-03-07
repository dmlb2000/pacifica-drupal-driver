#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Configuration reading and validation module."""
from os import getenv, getcwd
from configparser import ConfigParser as SafeConfigParser
from .globals import CONFIG_FILE


def get_config(config_file=CONFIG_FILE):
    """Return the ConfigParser object with defaults set."""
    configparser = SafeConfigParser()
    configparser.add_section('drupal')
    configparser.set('drupal', 'url', getenv(
        'DRUPAL_DRIVER_URL', 'http://localhost'))
    configparser.set('drupal', 'admin_user', getenv(
        'DRUPAL_DRIVER_USER', 'admin'))
    configparser.set('drupal', 'admin_password', getenv(
        'DRUPAL_DRIVER_USER_PASSWORD', ''))
    configparser.set('drupal', 'project_directory', getenv(
        'DRUPAL_DRIVER_PROJECT_DIRECTORY', getcwd()))    
    configparser.add_section('drush')
    configparser.set('drush', 'alias', getenv(
        'DRUPAL_DRIVER_DRUSH_ALIAS', '@self'))
    configparser.set('drush', 'admin_theme', 'seven')
    configparser.add_section('bin_paths')
    configparser.set('bin_paths', 'drush', 'drush')
    configparser.set('bin_paths', 'drupal', 'drupal')
    configparser.add_section('url_paths')
    configparser.set('url_paths', 'add_content_types', '/admin/structure/types/add')
    configparser.set('url_paths', 'content_types', '/admin/structure/types')
    configparser.add_section('page_queries')
    configparser.set('page_queries', 'admin_toolbar_header', '#toolbar-bar > h2')
    configparser.set('page_queries', 'add_content_type_form', '#node-type-add-form')
    configparser.set('page_queries', 'content_type_save', '#edit-save-continue')
    configparser.set('page_queries', 'content_type_name_input', '#edit-name')
    configparser.set('page_queries', 'content_type_edit_type', '#edit-name-machine-name-suffix > span.admin-link > button')
    configparser.set('page_queries', 'content_type_type_input', '#edit-type')
    configparser.set('page_queries', 'block_content', '#block-seven-content')
    configparser.set('page_queries', 'config_type_xpath', '//a[text()="Manage fields"]')
    configparser.read(config_file)
    return configparser
