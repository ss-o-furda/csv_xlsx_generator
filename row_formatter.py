import random as rd

from faker import Faker

import cars_lists

FAKE = Faker()


def cars_formatter(id_):
    rows_dict = {
        'ID': id_ + 1,
        'Brand': rd.choice(cars_lists.cars_names_list),
        'Type': rd.choice(cars_lists.cars_types_list),
        'Color': rd.choice(cars_lists.cars_color_list),
        'Year': rd.choice(cars_lists.cars_years_list),
        'Engine capacity': rd.choice(cars_lists.cars_engine_capacity_list),
        'Engine power': rd.choice(cars_lists.cars_engine_power_list),
        'Mileage': rd.choice(cars_lists.cars_mileage_list),
        'Body type': rd.choice(cars_lists.cars_body_type_list)
    }
    return rows_dict


def people_formatter(id_):
    rows_dict = {
        'ID': id_ + 1,
        'Name': FAKE.first_name(),
        'Surname': FAKE.last_name(),
        'Username': FAKE.user_name(),
        'Phone': FAKE.phone_number(),
        'Address': FAKE.address(),
        'Job': FAKE.job(),
        'Personal Email': FAKE.ascii_free_email(),
        'Company Email': FAKE.company_email()
    }
    return rows_dict
