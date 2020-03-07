#!/usr/bin/python
"""Run the drush command on drupal for things."""
from subprocess import check_output

def get_drush_uli(config):
    """Call drush uli on the project root."""
    url = check_output([
        config.get('bin_paths', 'drush'),
        '--root={}'.format(config.get('drupal', 'project_directory')),
        config.get('drush', 'alias'),
        'uli',
        '--no-browser'
    ]).decode('utf8')
    if 'http://default' in url:
        url = url.replace('http://default', config.get('drupal', 'url'))
    return url

def set_drush_admin_theme(config):
    """Call drush to set the admin theme."""
    return check_output([
        config.get('bin_paths', 'drush'),
        '--yes',
        '--root={}'.format(config.get('drupal', 'project_directory')),
        config.get('drush', 'alias'),
        'cset',
        'system.theme',
        'admin',
        config.get('drush', 'admin_theme')
    ]).decode('utf8')