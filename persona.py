from mailbox import NoSuchMailboxError


class Persona:
    especie = "Humano"
    def __init__(self, nombre, apellido, trabajo):
        self.nombre = nombre
        self.apellido = apellido
        self.trabajo = trabajo

    def hablar(self):
        print(f"Hola soy {self.nombre} {self.apellido}, trabajo de {self.trabajo}")
    
    def trabajar(self, trabajo):
        if trabajo == "Ingeniero":
            print("Sos crack loco eh")

Agus = Persona("Agustin", "Masson", "Ingeniero")

Agus.hablar()
Agus.trabajar("Ingeniero")