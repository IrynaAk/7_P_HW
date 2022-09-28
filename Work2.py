# Export

# def export_data():
#     with open('Data.txt', 'r') as a,open ('Export.csv','w') as b:
#         b.write(a.read())


# Import

imp_file = 'Import.txt'
def import_data(imp_file):
    with open(imp_file, 'r') as a, open ('Data.txt','a') as b:
        b.write(a.read())

import_data(imp_file)