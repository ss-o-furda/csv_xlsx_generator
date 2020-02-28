#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import sys


class Parser(argparse.ArgumentParser):
    def __init__(self):
        super(Parser, self).__init__()
        self.version = 1.1
        self.description = """A script that can generate a csv, xlsx, sqlite file 
        that contains a list of machines or people of a given size or length, with random values."""
        self.epilog = '(c) Orik 2020.'
        self.add_argument('--version', action='version', help='version number',
                          version='%(prog)s {}'.format(self.version))
        self.add_argument('-t', '--type', required=True, type=str, choices=['csv', 'xlsx', 'sqlite'],
                          help='the type of your file')
        self.add_argument('-f', '--filename', required=True, type=str,
                          help='the name of your file (without extension)')
        self.add_argument('-r', '--records', type=int,
                          help='the number of entries in the file. please, choose -r or -s, not both')
        self.add_argument('-s', '--size', type=float,
                          help='the size of your file. please, choose -r or -s, not both')
        self.add_argument('--cars', action='store_const', const=True, default=False,
                          help='a flag indicating that the file will contain vehicle information')
        self.add_argument('--people', action='store_const', const=True, default=False,
                          help='a flag indicating that the file will contain information about people')
        self.add_argument('--threading', action='store_const', const=True, default=False,
                          help='a flag indicating that the program will run in multithreading mode')
        self.add_argument('--processing', action='store_const', const=True, default=False,
                          help='a flag indicating that the program will work in multiprocessing mode')

    def validation(self):
        args = self.parse_args()

        if not args.records and not args.size:
            self._print_message('\nplease specify the size or number of rows\n\n')
            sys.exit(2)
        if not args.cars and not args.people:
            self._print_message('\nplease specify type of records\n--cars or --people\n\n')
            sys.exit(2)
        if args.cars and args.people:
            self._print_message('\nplease select one of the types, not both\n--cars or --people\n\n')
            sys.exit(2)
        if args.threading and args.processing:
            self._print_message('\nplease select one of the modes, not both\n--threading or --processing\n\n')
            sys.exit(2)
