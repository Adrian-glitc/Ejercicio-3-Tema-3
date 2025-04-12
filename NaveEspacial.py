class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        return (f"Nombre: {self.nombre}, Longitud: {self.longitud}m, "
                f"Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}")


# Lista de naves espaciales
naves = [
    NaveEspacial("Cometa Veloz", 120, 10, 50),
    NaveEspacial("Titán del Cosmos", 200, 15, 100),
    NaveEspacial("GX-1 Explorer", 150, 8, 6),
    NaveEspacial("GX-2 Voyager", 180, 12, 8),
    NaveEspacial("Estrella Fugaz", 90, 5, 20),
    NaveEspacial("Nebulosa Andrómeda", 250, 20, 150),
    NaveEspacial("Aurora Celeste", 110, 7, 4),
]