from tabulate import tabulate
import csv
from InquirerPy import inquirer
import json

data = []
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    with open('data.csv', newline='', encoding='utf-8') as csv_file:
        file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')
        next(file_reader)
        for row in file_reader:
            data.append(row)

while True:
    print("1. Izdrukāt visas gŗāmatas")
    print("2. Pievienot jaunu grāmatu")
    print("3. Kārtot grāmatas pēc % no izlasītām grāmatām")
    print("4. Kārtot grāmatas pēc nosaukuma")
    print("5. Kārtot grāmatas pēc lasīšanas statusa")
    print("0. Iziet")

    choice = input("Ievadi komandu: ")

    print("\n==========================\n")

    if choice == '1':
        table_data = []
        for row in data:
            try:
                total_pages = int(row[2])
                read_pages = int(row[3])
                if total_pages == 0:
                    percentage = 0
                else:
                    percentage = round(read_pages / total_pages * 100, 1)
                table_data.append([row[0], row[1], total_pages, read_pages, percentage, row[4], row[5]])
            except ValueError:
                print("Kļūda datu apstrādē:", row)
        headers = ["Nosaukums", "Autors", "Kopējo Lappušu Skaits", "Izlasīto Lappušu Skaits", "Izlasīto Lappušu Skaits %", "Piezimes", "Lasīšanas Statuss"]
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    elif choice == '2':
        print("Jauna grāmata:")
        title = input("Nosaukums: ")
        author = input("Autors: ")
        total_pages = input("Kopējais lappušu skaits: ")
        read_pages = input("Izlasīto lappušu skaits: ")
        notes = input("Piezimes: ")
        status = inquirer.select(
            message="Lasīšanas statuss:",
            choices=["Lasu", "Izlasīta", "Neesmu sācis"],
        ).execute()
        data.append([title, author, total_pages, read_pages, notes, status])
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    elif choice == '3':
        data.sort(key=lambda x: (int(x[3]) / int(x[2])) if int(x[2]) > 0 else 0, reverse=True)
        table_data = []
        for row in data:
            try:
                total_pages = int(row[2])
                read_pages = int(row[3])
                if total_pages == 0:
                    percentage = 0
                else:
                    percentage = round(read_pages / total_pages * 100, 1)
                table_data.append([row[0], row[1], total_pages, read_pages, percentage, row[4], row[5]])
            except ValueError:
                print("Kļūda datu apstrādē:", row)
        headers = ["Nosaukums", "Autors", "Kopējo Lappušu Skaits", "Izlasīto Lappušu Skaits", "Izlasīto Lappušu Skaits %", "Piezimes", "Lasīšanas Statuss"]
        print("Grāmatas kārtotas pēc % no izlasītām lappusēm (no lielākā uz mazāko):")
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    elif choice == '4':
        data.sort(key=lambda x: x[0])
        table_data = []
        for row in data:
            try:
                total_pages = int(row[2])
                read_pages = int(row[3])
                if total_pages == 0:
                    percentage = 0
                else:
                    percentage = round(read_pages / total_pages * 100, 1)
                table_data.append([row[0], row[1], total_pages, read_pages, percentage, row[4], row[5]])
            except ValueError:
                print("Kļūda datu apstrādē:", row)
        headers = ["Nosaukums", "Autors", "Kopējo Lappušu Skaits", "Izlasīto Lappušu Skaits", "Izlasīto Lappušu Skaits %", "Piezimes", "Lasīšanas Statuss"]
        print("Grāmatas kārtotas pēc nosaukuma (A-Z):")
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    elif choice == '5':
        data.sort(key=lambda x: x[5])
        table_data = []
        for row in data:
            try:
                total_pages = int(row[2])
                read_pages = int(row[3])
                if total_pages == 0:
                    percentage = 0
                else:
                    percentage = round(read_pages / total_pages * 100, 1)
                table_data.append([row[0], row[1], total_pages, read_pages, percentage, row[4], row[5]])
            except ValueError:
                print("Kļūda datu apstrādē:", row)
        headers = ["Nosaukums", "Autors", "Kopējo Lappušu Skaits", "Izlasīto Lappušu Skaits", "Izlasīto Lappušu Skaits %", "Piezimes", "Lasīšanas Statuss"]
        print("Grāmatas kārtotas pēc lasīšanas statusa:")
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
    elif choice == '0':
        break
    else:
        print("Komanda nav atpazīta vai vēl nav ieviesta.")
