import os
import random as rd
import sqlite3

import cars_lists


def generate_sqlite(records, headers):
    conn = sqlite3.connect('large.db')

    curr = conn.cursor()

    # curr.execute(f"CREATE TABLE cars {tuple(headers)}")

    size = 0
    i = 0

    while size < 10000000000:
        i = i + 1
        size = os.stat('large.db').st_size
        curr.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                     [i,
                      rd.choice(cars_lists.cars_names_list),
                      rd.choice(cars_lists.cars_types_list),
                      rd.choice(cars_lists.cars_color_list),
                      rd.choice(cars_lists.cars_years_list),
                      rd.choice(cars_lists.cars_engine_capacity_list),
                      rd.choice(cars_lists.cars_engine_power_list),
                      rd.choice(cars_lists.cars_mileage_list),
                      rd.choice(cars_lists.cars_body_type_list)])
    conn.commit()
    print(f'-------size--------\n{os.stat("large.db").st_size}')
    conn.close()
