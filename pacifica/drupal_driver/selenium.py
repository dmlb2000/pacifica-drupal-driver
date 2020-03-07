#!/usr/bin/python
"""Drupal driver selenium module."""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .drush import get_drush_uli, set_drush_admin_theme
from .config import get_config

def _wait_on_selector(driver, config_key):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, get_config().get('page_queries', config_key))
        )
    )

def _wait_on_title(driver, title_str):
    WebDriverWait(driver, 30).until(
        EC.title_contains(title_str)
    )

def _get_content_types(driver, config):
    driver.get('{}/{}'.format(
        config.get('drupal', 'url'),
        config.get('url_paths', 'content_types')
    ))
    links = driver.find_elements(By.XPATH, config.get('page_queries', 'config_type_xpath'))
    return [
        link.get_attribute('href').replace(
            '{}{}/manage/'.format(config.get('drupal', 'url'), config.get('url_paths', 'content_types')),
            ''
        ).replace('/fields', '')
        for link in links
    ]

def _create_content_type(driver, config, prefix, content_type):
    driver.get('{}/{}'.format(
        config.get('drupal', 'url'),
        config.get('url_paths', 'add_content_types')
    ))
    _wait_on_title(driver, 'Add content type')
    elem = driver.find_element(By.CSS_SELECTOR, config.get('page_queries', 'content_type_name_input'))
    elem.clear()
    elem.send_keys('{} {}'.format(prefix.capitalize(), content_type.capitalize()))
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,  config.get('page_queries', 'content_type_edit_type')))
    )
    elem = driver.find_element(By.CSS_SELECTOR, config.get('page_queries', 'content_type_edit_type'))
    elem.click()

    elem = driver.find_element(By.CSS_SELECTOR, config.get('page_queries', 'content_type_type_input'))
    elem.clear()
    elem.send_keys('{}_{}'.format(prefix, content_type))
    elem = driver.find_element(By.CSS_SELECTOR, config.get('page_queries', 'add_content_type_form'))
    elem.submit()
    _wait_on_title(driver, 'Manage fields')

def create_content_types(args):
    """Main entrypoint to run selenium."""
    config = get_config(args.config)
    set_drush_admin_theme(config)
    admin_uli = get_drush_uli(config)
    driver = webdriver.Firefox()
    driver.get(admin_uli)
    try:
        _wait_on_title(driver, 'admin')
        links = _get_content_types(driver, config)
        for content_type in args.content_types:
            machine_name = '{}_{}'.format(args.prefix, content_type)
            if machine_name not in links:
                _create_content_type(driver, config, args.prefix, content_type)
    finally:
        driver.close()
    return 0