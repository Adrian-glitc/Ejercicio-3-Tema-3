from NaveEspacial import NaveEspacial, naves
class Operaciones: 
    
    @staticmethod
    def ordenar_naves():
        # Ordenar por nombre ascendente y longitud descendente
        naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
        return naves_ordenadas

    @staticmethod
    def informacion_naves_especificas():
        # Información de "Cometa Veloz" y "Titán del Cosmos"
        return [nave for nave in naves if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]]

    @staticmethod
    def cinco_mayor_pasajeros():
        # Cinco naves con mayor cantidad de pasajeros
        return sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]

    @staticmethod
    def nave_mayor_tripulacion():
        # Nave que requiere mayor cantidad de tripulación
        return max(naves, key=lambda x: x.tripulantes)

    @staticmethod
    def naves_comienzan_gx():
        # Naves cuyo nombre comienza con "GX"
        return [nave for nave in naves if nave.nombre.startswith("GX")]

    @staticmethod
    def naves_seis_o_mas_pasajeros():
        # Naves que pueden llevar seis o más pasajeros
        return [nave for nave in naves if nave.pasajeros >= 6]

    @staticmethod
    def nave_mas_pequena_y_grande():
        # Nave más pequeña y más grande
        nave_mas_pequena = min(naves, key=lambda x: x.longitud)
        nave_mas_grande = max(naves, key=lambda x: x.longitud)
        return nave_mas_pequena, nave_mas_grande
