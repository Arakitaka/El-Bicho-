import openpyxl
import re

# Pregunta al usuario que desea hacer, llamar a esta funcion para iniciar el programa
def menu():
    espacio = "-----------"
    print(espacio)
    print("Que desea hacer?")
    print("Salir del programa: 0 \n Usar la calculadora: 1")
    input()

# variables, excel
wb = openpyxl.load_workbook("planillaRFID.xlsx")
sheet = wb.active


# funciones del excel
def add_value(cell, value):
    sheet[f'{cell}'] = value


def save_excel():
    wb.save("planillaRFID.xlsx")


def primera_celda_vacia():
    dimensiones = wb.active.calculate_dimension()
    columna, fila = re.search(r"([A-Z]+)\d+:[A-Z]+(\d+)", dimensiones).groups()
    return f"{columna}{int(fila) + 1}"


def hallar_valor(valor):
    numero = ""
    for i in valor:
        if i != "A":
            numero = numero + i
    return numero

def escribir_excel():
    name = input("Ingrese nombre")
    owner = input("Ingrese nombre del dueño")
    code = input("Ingrese código de RFID")
    location = input("Ingrese las coordenadas de ubicación")
    escribir = primera_celda_vacia()
    add_value("A" + escribir[1], name)
    add_value("B" + escribir[1], owner)
    add_value("C" + escribir[1], code)
    add_value("D" + escribir[1], location)
    save_excel()


# funciones del excel
def primera_celda_vacia():
    dimensiones = wb.active.calculate_dimension()
    columna, fila = re.search(r"([A-Z]+)\d+:[A-Z]+(\d+)", dimensiones).groups()
    return f"{columna}{int(fila) + 1}"


def buscar_code(hex_code):
    final = "C"+ str(int(primera_celda_vacia()[1:])-1)
    for rowOfCellObjects in sheet[f'C2:{final}']:
            for cellObj in rowOfCellObjects:
                if cellObj.value == hex_code:
                    return True
            return False

print(buscar_code("r"))



print(primera_celda_vacia())
