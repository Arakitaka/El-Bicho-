import openpyxl
import re

# variables, excel
wb = openpyxl.load_workbook("planillaRFID.xlsx")
sheet = wb.active


# funciones del excel
def add_value(cell, value):
    sheet[f'{cell}'] = value


def mostrar_valor(cell):
    return sheet[cell].value


def save_excel():
    wb.save("planillaRFID.xlsx")


def primera_celda_vacia():
    dimensiones = wb.active.calculate_dimension()
    columna, fila = re.search(r"([A-Z]+)\d+:[A-Z]+(\d+)", dimensiones).groups()
    return f"{columna}{int(fila) + 1}"


def hallar_valor(valor):  # para las casillas lol
    numero = ""
    for i in valor:
        if i != "A":
            numero = numero + i
    return numero


def hallar_codigo_rfid_excel(codigo_rfid):
    for cell in sheet["C"]:
        if cell.value == codigo_rfid:
            name = mostrar_valor("A" + str(cell.row))
            owner = mostrar_valor("B" + str(cell.row))
            location = mostrar_valor("D" + str(cell.row))

            print("se ha encontrado el codigo")
            print(f"Codigo: {cell.value}\n"
                  f"Nombre: {name}\n"
                  f"Dueño: {owner}\n"
                  f"Ubicacion: {location}\n")
            return
    return print("no se encontro")


hallar_codigo_rfid_excel(input("Ingrese el codigo: "))
