from Operaciones import Operaciones
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
def iniciar_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menú de Naves Espaciales")
    fuente = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    opciones = [
        "1. Ordenar naves por nombre ascendente y longitud descendente",
        "2. Información de 'Cometa Veloz' y 'Titán del Cosmos'",
        "3. Cinco naves con mayor cantidad de pasajeros",
        "4. Nave que requiere mayor cantidad de tripulación",
        "5. Naves cuyo nombre comienza con 'GX'",
        "6. Naves que pueden llevar seis o más pasajeros",
        "7. Nave más pequeña y más grande",
        "8. Salir"
    ]

    while True:
        pantalla.fill((0, 0, 0))
        y = 50

        for opcion in opciones:
            texto = fuente.render(opcion, True, (255, 255, 255))
            pantalla.blit(texto, (50, y))
            y += 50

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                return
            elif evento.type == MOUSEBUTTONDOWN:
                x, y = evento.pos
                if 50 <= x <= 750:
                    opcion_seleccionada = (y - 50) // 50 + 1
                    if 1 <= opcion_seleccionada <= 8:
                        manejar_opcion(opcion_seleccionada)

        clock.tick(30)

def manejar_opcion(opcion):
    if opcion == 1:
        print("\nNaves ordenadas por nombre ascendente y longitud descendente:")
        for nave in Operaciones.ordenar_naves():
            print(nave)
    elif opcion == 2:
        print("\nInformación de 'Cometa Veloz' y 'Titán del Cosmos':")
        for nave in Operaciones.informacion_naves_especificas():
            print(nave)
    elif opcion == 3:
        print("\nCinco naves con mayor cantidad de pasajeros:")
        for nave in Operaciones.cinco_mayor_pasajeros():
            print(nave)
    elif opcion == 4:
        print("\nNave que requiere mayor cantidad de tripulación:")
        print(Operaciones.nave_mayor_tripulacion())
    elif opcion == 5:
        print("\nNaves cuyo nombre comienza con 'GX':")
        for nave in Operaciones.naves_comienzan_gx():
            print(nave)
    elif opcion == 6:
        print("\nNaves que pueden llevar seis o más pasajeros:")
        for nave in Operaciones.naves_seis_o_mas_pasajeros():
            print(nave)
    elif opcion == 7:
        nave_mas_pequena, nave_mas_grande = Operaciones.nave_mas_pequena_y_grande()
        print("\nNave más pequeña:")
        print(nave_mas_pequena)
        print("\nNave más grande:")
        print(nave_mas_grande)
    elif opcion == 8:
        print("Saliendo del programa...")
        pygame.quit()
        exit()