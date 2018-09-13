# -*- coding: utf-8 -*-
import csv

with open("2018-09-13_at_pincodes.csv", 'r', encoding='utf-8') as csvfile:
    raw_pincodes = csv.reader(csvfile, delimiter=',', quotechar='"')
    output = open("at_pincodes.csv", "w")
    output.write('"pincode","city","canton","canton_code","country","country_code"\n')
    for row in raw_pincodes:
        pincode = row[0]
        city_codes = row[1].split(', ')
        city_names = row[2].split(', ')
        for i in range(0, len(city_codes)):
            print("{0}/{1}/{2}".format(pincode, city_codes[i], city_names[i]))
            output.write('{0},"{1}","","","Österreich","AT"\n'.format(pincode, city_names[i])) 

