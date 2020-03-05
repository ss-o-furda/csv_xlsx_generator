"""Auxiliary module for generating csv files"""
import csv
import os
import random as rd
import sys

from faker import Faker

import cars_lists

FAKE = Faker()


def csv_cars_filler(writer, id_):
    """
    A function that writes machine parameters to a row
    :param writer: csv.DictWriter obj
    :param id_: row id
    """
    writer.writerow({
        'ID': id_ + 1,
        'Brand': rd.choice(cars_lists.cars_names_list),
        'Type': rd.choice(cars_lists.cars_types_list),
        'Color': rd.choice(cars_lists.cars_color_list),
        'Year': rd.choice(cars_lists.cars_years_list),
        'Engine capacity': rd.choice(cars_lists.cars_engine_capacity_list),
        'Engine power': rd.choice(cars_lists.cars_engine_power_list),
        'Mileage': rd.choice(cars_lists.cars_mileage_list),
        'Body type': rd.choice(cars_lists.cars_body_type_list)
    })


def csv_people_filler(writer, id_):
    """
    A function that writes people information to a row
    :param writer: csv.DictWriter obj
    :param id_: row id
    """
    writer.writerow({
        'ID': id_ + 1,
        'Name': FAKE.first_name(),
        'Surname': FAKE.last_name(),
        'Username': FAKE.user_name(),
        'Phone': FAKE.phone_number(),
        'Address': FAKE.address(),
        'Job': FAKE.job(),
        'Personal Email': FAKE.ascii_free_email(),
        'Company Email': FAKE.company_email()
    })


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
                    csv_cars_filler(writer, id_)
            elif people:
                for id_ in range(records):
                    csv_people_filler(writer, id_)
            else:
                print('Smth went wrong...')
                sys.exit(2)
        elif size:
            temp_size = 0
            id_ = 0
            if cars:
                while temp_size < size:
                    csv_cars_filler(writer, id_)
                    id_ = id_ + 1
                    temp_size = os.stat(filename).st_size
            elif people:
                while temp_size < size:
                    csv_people_filler(writer, id_)
                    id_ = id_ + 1
                    temp_size = os.stat(filename).st_size
            else:
                print('Smth went wrong...')
                sys.exit(2)
        else:
            print('Smth went wrong...')
            sys.exit(2)

    print('CSV generation complete')
