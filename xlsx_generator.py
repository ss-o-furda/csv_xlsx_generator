import random as rd

import xlsxwriter

import cars_lists


def generate_xlsx(headers, filename, records=None, size=None):
    columns = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
    things = ()
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet("Cars")

    for i in range(len(columns)):
        worksheet.write(columns[i], headers[i])

    for i in range(records):
        things = things + (
            [i + 1,
             rd.choice(cars_lists.cars_names_list),
             rd.choice(cars_lists.cars_types_list),
             rd.choice(cars_lists.cars_color_list),
             rd.choice(cars_lists.cars_years_list),
             rd.choice(cars_lists.cars_engine_capacity_list),
             rd.choice(cars_lists.cars_engine_power_list),
             rd.choice(cars_lists.cars_mileage_list),
             rd.choice(cars_lists.cars_body_type_list)],
        )

    row = 1
    col = 0

    for id_, brand, type_, color, year, engine_capacity, engine_power, mileage, body_type in things:
        worksheet.write(row, col, id_)
        worksheet.write(row, col + 1, brand)
        worksheet.write(row, col + 2, type_)
        worksheet.write(row, col + 3, color)
        worksheet.write(row, col + 4, year)
        worksheet.write(row, col + 5, engine_capacity)
        worksheet.write(row, col + 6, engine_power)
        worksheet.write(row, col + 7, mileage)
        worksheet.write(row, col + 8, body_type)
        row += 1

    workbook.close()
    print('XLSX generation complete')
