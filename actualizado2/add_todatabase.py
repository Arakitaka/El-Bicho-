import random
from csv import writer


def load_val_csv(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def coordenadas_random():
    return (round(random.uniform(90, -90), 3)), str(round(random.uniform(90, -90), 3))


print(coordenadas_random())

hexcode = input("hexcode >>> ")
objecto = input("object >>> ")
owner = input("owner >>> ")
location = coordenadas_random()
el_lista = [hexcode, objecto, owner, str(location)]
print(el_lista)

name_file = "mecadb.csv"
load_val_csv(name_file, el_lista)
print("funco")
