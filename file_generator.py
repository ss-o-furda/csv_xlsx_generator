import datetime
import sys
import argparser
import time

if __name__ == "__main__":
    parser = argparser.Parser()
    parser.validation()



# if __name__ == "__main__":
#     start_time = time.time()
#     records = 10000
#     headers = ['ID', 'Brand', 'Type', 'Color', 'Year',
#                'Engine capacity', 'Engine power', 'Mileage', 'Body type']
#
#     print(f'--------time----------\n{str(datetime.timedelta(seconds=time.time() - start_time))}')


# python3 file_generator.py -t csv -f main
# Namespace(cars=False, filename='main', people=False, records=None, size=None, type='csv')
