import csv
import random as rd

import cars_lists


def generate_cars_csv(headers, filename, records=None, size=None):
    with open(filename, 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                'ID': i + 1,
                'Brand': rd.choice(cars_lists.cars_names_list),
                'Type': rd.choice(cars_lists.cars_types_list),
                'Color': rd.choice(cars_lists.cars_color_list),
                'Year': rd.choice(cars_lists.cars_years_list),
                'Engine capacity': rd.choice(cars_lists.cars_engine_capacity_list),
                'Engine power': rd.choice(cars_lists.cars_engine_power_list),
                'Mileage': rd.choice(cars_lists.cars_mileage_list),
                'Body type': rd.choice(cars_lists.cars_body_type_list)
            })
    print('CSV generation complete')


def generate_people_csv():
    pass
