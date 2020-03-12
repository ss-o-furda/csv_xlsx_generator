"""Auxiliary module for generating csv files"""
import csv
import os
import sys

import row_formatter


def generate_csv(headers, filename, **kwargs):
    """
    A function that takes the following options and generates a csv file based on them
    :param headers: headers of csv file
    :param filename: name of csv file
    :param kwargs:
        :records: the number of rows that must be in the file
        :size: the size of the final file
        :cars: a flag indicating that the file must contain machine data
        :people: a flag indicating that the file must contain information about people
    """
    records = kwargs.get('records', 0)
    size = kwargs.get('size', 0)
    cars = kwargs.get('cars', False)
    people = kwargs.get('people', False)

    with open(filename, 'wt') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        if records:
            if cars:
                for id_ in range(records):
                    writer.writerow(row_formatter.cars_formatter(id_))
            elif people:
                for id_ in range(records):
                    writer.writerow(row_formatter.people_formatter(id_))
            else:
                print('Smth went wrong...')
                sys.exit(2)
        elif size:
            temp_size = 0
            id_ = 0
            if cars:
                while temp_size < size:
                    writer.writerow(row_formatter.cars_formatter(id_))
                    id_ = id_ + 1
                    temp_size = os.stat(filename).st_size
            elif people:
                while temp_size < size:
                    writer.writerow(row_formatter.people_formatter(id_))
                    id_ = id_ + 1
                    temp_size = os.stat(filename).st_size
            else:
                print('Smth went wrong...')
                sys.exit(2)
        else:
            print('Smth went wrong...')
            sys.exit(2)

    print('CSV generation complete')
