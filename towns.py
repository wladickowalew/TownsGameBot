import csv

towns = []


def load_towns():
    with open('data/city.csv', newline='', encoding='1251') as f:
        reader = csv.reader(f, delimiter=';', quotechar='"')
        for row in reader:
            towns.append(row[3])
    towns.pop(0)



