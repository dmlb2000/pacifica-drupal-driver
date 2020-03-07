#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Main Drupal Driver command line module."""
from sys import argv as sys_argv
from argparse import ArgumentParser
from .globals import CONFIG_FILE
from .selenium import create_content_types


def _create_content_type_parser(subparsers):
    parser = subparsers.add_parser(
        'content_types',
        description='Update or Create the Content Types.'
    )
    parser.add_argument(
        '--prefix', required=True, type=str,
        help='The content type prefix'
    )
    parser.add_argument(
        'content_types', type=str, metavar='content_type',
        help='The content type names', nargs='+'
    )
    parser.set_defaults(func=create_content_types)

def _create_field_config_parser(subparsers):
    parser = subparsers.add_parser(
        'content_types',
        description='Update or Create the Content Types.'
    )
    parser.add_argument(
        '--prefix', required=True, type=str,
        help='The content type prefix'
    )
    parser.add_argument(
        'content_types', type=str, metavar='content_type',
        help='The content type names', nargs='+'
    )
    parser.set_defaults(func=create_content_types)

def main(*argv):
    """Main command method."""
    parser = ArgumentParser(description='Run the Drupal driver.')
    parser.add_argument('-c', '--config', metavar='CONFIG', type=str,
                        default=CONFIG_FILE, dest='config',
                        help='drupal driver config file')
    parser.set_defaults(func=lambda _args: parser.print_help())
    subparsers = parser.add_subparsers(help='sub-command help')
    _create_content_type_parser(subparsers)
    if not argv:  # pragma: no cover
        argv = sys_argv[1:]
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == '__main__':
    main()
