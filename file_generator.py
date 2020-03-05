import sys

import argparser
import csv_generator

CARS_HEADERS = ['ID', 'Brand', 'Type', 'Color', 'Year',
                'Engine capacity', 'Engine power', 'Mileage', 'Body type']
PEOPLE_HEADERS = ['ID', 'Name', 'Surname', 'Username', 'Phone', 'Address',
                  'Job', 'Personal Email', 'Company Email']


def parse_arg():
    parser = argparser.Parser()
    valid_data = parser.validation()

    filename = valid_data.filename
    file_type = valid_data.type
    records = valid_data.records
    size_in_gb = valid_data.size  #
    if size_in_gb:
        size = size_in_gb * 1000000000
    else:
        size = 0
    cars = valid_data.cars
    people = valid_data.people
    thread = valid_data.threading
    process = valid_data.processing

    return filename, file_type, records, size, cars, people, thread, process


def main():
    filename, file_type, records, size, cars, people, thread, process = parse_arg()
    if file_type == 'csv':
        filename += '.csv'
        if cars:
            csv_generator.generate_csv(CARS_HEADERS,
                                       filename,
                                       records=records,
                                       size=size,
                                       cars=cars,
                                       people=people,
                                       thread=thread,
                                       process=process)
        elif people:
            csv_generator.generate_csv(PEOPLE_HEADERS,
                                       filename,
                                       records=records,
                                       size=size,
                                       cars=cars,
                                       people=people,
                                       thread=thread,
                                       process=process)
    else:
        print('in future')
        sys.exit(2)


if __name__ == "__main__":
    main()
