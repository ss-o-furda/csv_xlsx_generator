import datetime
import sys
import argparser
import time

if __name__ == "__main__":
    parser = argparser.Parser()
    valid_data = parser.validation()

    print(valid_data)

#     headers = ['ID', 'Brand', 'Type', 'Color', 'Year',
#                'Engine capacity', 'Engine power', 'Mileage', 'Body type']

# python3 file_generator.py -t csv --cars -f 1 -r 10
# Namespace(cars=True, filename='1', people=False, processing=False, records=10, size=None, threading=False, type='csv')
