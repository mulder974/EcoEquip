# import csv

# data = {}
# with open('Fichiers de données conso annuelles_V1.csv', newline='', encoding='latin-1') as csvfile:
#     csv_reader = csv.DictReader(csvfile, delimiter=';')
#     for row in csv_reader:
#         appareil_suivi = row['Appareil suivi']
#         conso_an1 = row['Consommation annuelle  AN1']
#         conso_an2 = row['Consommation annuelle AN2']
#         type_appareil = row['Type']

#         if conso_an1 and conso_an1 != '-':
#             conso_an1 = float(conso_an1.replace(',', '.'))
#         else:
#             conso_an1 = 0.0

#         if conso_an2 and conso_an2 != '-':
#             conso_an2 = float(conso_an2.replace(',', '.'))
#         else:
#             conso_an2 = 0.0

#         key = (appareil_suivi, type_appareil)
#         if key in data:
#             data[key]['count'] += 1
#             data[key]['conso_an1'] += conso_an1
#             data[key]['conso_an2'] += conso_an2
#         else:
#             data[key] = {'count': 1, 'conso_an1': conso_an1, 'conso_an2': conso_an2, 'type': type_appareil}

# with open('resultats.csv', mode='w', newline='', encoding='utf-8') as csv_file:
#     fieldnames = ['Appareil suivi unique', 'Type', 'Moyenne consommation annuelle AN1', 'Moyenne consommation annuelle AN2']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for (appareil_suivi, type_appareil), values in data.items():
#         moyenne_conso_an1 = values['conso_an1'] / values['count']
#         moyenne_conso_an2 = values['conso_an2'] / values['count']
#         writer.writerow({'Appareil suivi unique': appareil_suivi,
#                          'Type': type_appareil,
#                          'Moyenne consommation annuelle AN1': moyenne_conso_an1,
#                          'Moyenne consommation annuelle AN2': moyenne_conso_an2})


with open('resultats.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Appareil suivi unique', 'Type', 'Moyenne consommation annuelle AN1', 'Moyenne consommation annuelle AN2']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    for line in csv_file:

        if line[1] == "" :
            type = line[0]
        elif line[2] == "":

            writer.writerow({'Appareil suivi unique': line[0],
                                'Type': line[1],
                                'Moyenne consommation annuelle AN1': line[2],
                                'Moyenne consommation annuelle AN2': line[3]})
        writer.writeheader()
    for (appareil_suivi, type_appareil), values in data.items():
        
        if appareil_suivi
        writer.writerow({'Appareil suivi unique': appareil_suivi,
                         'Type': type_appareil,
                         'Moyenne consommation annuelle AN1': moyenne_conso_an1,
                         'Moyenne consommation annuelle AN2': moyenne_conso_an2})
