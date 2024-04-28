import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data1 = ['Afghanistan', 652090 , 'AF', 'AFG']

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data1)

data2 = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data2)

