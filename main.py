import csv
import xlsxwriter
import random as rd
import time

cars_names_list = ['Audi', 'BMW', 'Chevrolet', 'Daewoo',
                   'Ford', 'Honda', 'Hyundai', 'Kia', 'Mazda', 'Mercedes-Benz',
                   'Mitsubishi', 'Nissan', 'Opel', 'Renault', 'Skoda', 'Toyota',
                   'Volkswagen', 'Alfa Romeo', 'Aston Martin', 'Bentley', 'Cadillac',
                   'Chrysler', 'Citroen', 'Ferrari', 'Fiat', 'Jeep', 'Lamborghini',
                   'Land Rover', 'Lexus', 'Lotus', 'Peugeot', 'Porsche', 'Smart', 'Tesla',
                   'Dodge', 'Hummer', 'Infiniti', 'Pontiac', 'Chery', 'Lada', 'Marusia']
cars_types_list = ['Passenger', 'Motorcycle', 'Truck',
                   'Trailer', 'Bus', 'Water transport', 'Special machinery']
cars_color_list = ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black',
                   'Brown', 'Azure', 'Silver', 'Purple', 'Gray', 'Orange',
                   'Maroon', 'Charcoal', 'Aquamarine', 'Coral', 'Lime', 'Magenta',
                   'Olden', 'Olive', 'Cyan']
cars_years_list = ['1850', '1920', '1938', '1975', '1982', '1985', '1987', '1989', '1991',
                   '1995', '2000', '2001', '2002', '2004', '2005', '2006', '2007', '2008',
                   '2009', '2010', '2012', '2013', '2015', '2016', '2017', '2018', '2019']
cars_engine_capacity_list = ['0.5', '0.75', '0.9', '1.0',
                             '1.2', '1.5', '1.8', '2.0', '2.3', '2.5', '2.8', '3.0',
                             '3.2', '3.5', '3.8', '4.0']
cars_engine_power_list = ['75', '80', '85', '90', '110', '120', '150',
                          '180', '195', '200', '210', '220', '235', '250', '280',
                          '290', '300', '305', '315', '325', '340', '350', '380', '400']
cars_mileage_list = ['0', '5 000', '20 000', '25 000', '30 000', '35 000', '40 000', '50 000',
                     '60 000', '75 000', '95 000', '100 000', '110 000', '125 000', '130 000',
                     '150 000', '180 000', '200 000', '250 000', '300 000']
cars_body_type_list = ['Station wagon', 'Hatchback',
                       'Coupe', 'Sedan', 'SUV', 'Cabriolet']


def generate_csv(records, headers):
    with open('Test_dataset_filterMe.csv', 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                'ID': i + 1,
                'Brand': rd.choice(cars_names_list),
                'Type': rd.choice(cars_types_list),
                'Color': rd.choice(cars_color_list),
                'Year': rd.choice(cars_years_list),
                'Engine capacity': rd.choice(cars_engine_capacity_list),
                'Engine power': rd.choice(cars_engine_power_list),
                'Mileage': rd.choice(cars_mileage_list),
                'Body type': rd.choice(cars_body_type_list)
            })
    print('CSV generation complete')


def generate_xlsx(records, headers):
    columns = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
    things = ()
    workbook = xlsxwriter.Workbook('Test_dataset_filterMe.xlsx')
    worksheet = workbook.add_worksheet("Cars")

    for i in range(len(columns)):
        worksheet.write(columns[i], headers[i])

    for i in range(records):
        things = things + (
            [i+1,
            rd.choice(cars_names_list),
            rd.choice(cars_types_list),
            rd.choice(cars_color_list),
            rd.choice(cars_years_list),
            rd.choice(cars_engine_capacity_list),
            rd.choice(cars_engine_power_list),
            rd.choice(cars_mileage_list),
            rd.choice(cars_body_type_list)],
        )

    row = 1
    col = 0

    for id_, brand, type_, color, year, engine_capacity, engine_power, mileage, body_type in things:
        worksheet.write(row, col, id_)
        worksheet.write(row, col+1, brand)
        worksheet.write(row, col+2, type_)
        worksheet.write(row, col+3, color)
        worksheet.write(row, col+4, year)
        worksheet.write(row, col+5, engine_capacity)
        worksheet.write(row, col+6, engine_power)
        worksheet.write(row, col+7, mileage)
        worksheet.write(row, col+8, body_type)
        row += 1

    workbook.close()
    print('XLSX generation complete')

if __name__ == "__main__":
    start_time = time.time()
    records = 10000
    headers = ['ID', 'Brand', 'Type', 'Color', 'Year',
               'Engine capacity', 'Engine power', 'Mileage', 'Body type']

    generate_csv(records, headers)
    generate_xlsx(records, headers)
    
    print(f'--- seconds ---\n{time.time() - start_time}')
