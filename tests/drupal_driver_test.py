#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test the example module."""
from os import path
from unittest import TestCase
from pacifica.drupal_driver.__main__ import main


class TestCommand(TestCase):
    """Test the example class."""

    def test_main(self):
        """Test the add method in example class."""
        self.assertEqual(main('--config', path.join(path.dirname(__file__), 'drupal.ini'), 'content_types', '--prefix', 'office', 'chairs', 'tables'), 0, 'main should return 0')
