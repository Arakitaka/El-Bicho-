# se me olvidaron los codigos :(

class Rfid:
    def __init__(self, name, owner, code, location):
        self.name = name
        self.owner = owner
        self.code = code
        self.location = location

    def __str__(self):
        return f"Name:{self.name}\n" \
               f"Owner:{self.owner}\n" \
               f"Code:{self.code}\n" \
               f"Location:{self.location}\n"


# lo de abajo es para probar nomas

example1 = Rfid("Nombre", "Dueño", "Codigo", "Ubicacion")
example2 = Rfid("Nombre2", "Dueño2", "Codigo2", "Ubicacion2")
print(example1)
print("---")
print(example2)
