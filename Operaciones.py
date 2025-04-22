from NaveEspacial import naves
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
class Operaciones: 
    
    @staticmethod
    def ordenar_naves():
        naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
        return naves_ordenadas

    @staticmethod
    def informacion_naves_especificas():
        return [nave for nave in naves if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]]

    @staticmethod
    def cinco_mayor_pasajeros():
        return sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]

    @staticmethod
    def nave_mayor_tripulacion():
        return max(naves, key=lambda x: x.tripulantes)

    @staticmethod
    def naves_comienzan_gx():
        return [nave for nave in naves if nave.nombre.startswith("GX")]

    @staticmethod
    def naves_seis_o_mas_pasajeros():
        return [nave for nave in naves if nave.pasajeros >= 6]

    @staticmethod
    def nave_mas_pequena_y_grande():
        nave_mas_pequena = min(naves, key=lambda x: x.longitud)
        nave_mas_grande = max(naves, key=lambda x: x.longitud)
        return nave_mas_pequena, nave_mas_grande

