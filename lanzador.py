from Operaciones import Operaciones
def main():
    print("Naves ordenadas por nombre ascendente y longitud descendente:")
    for nave in Operaciones.ordenar_naves():
        print(nave)

    print("\nInformación de 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in Operaciones.informacion_naves_especificas():
        print(nave)

    print("\nCinco naves con mayor cantidad de pasajeros:")
    for nave in Operaciones.cinco_mayor_pasajeros():
        print(nave)

    print("\nNave que requiere mayor cantidad de tripulación:")
    print(Operaciones.nave_mayor_tripulacion())

    print("\nNaves cuyo nombre comienza con 'GX':")
    for nave in Operaciones.naves_comienzan_gx():
        print(nave)

    print("\nNaves que pueden llevar seis o más pasajeros:")
    for nave in Operaciones.naves_seis_o_mas_pasajeros():
        print(nave)

    nave_mas_pequena, nave_mas_grande = Operaciones.nave_mas_pequena_y_grande()
    print("\nNave más pequeña:")
    print(nave_mas_pequena)
    print("\nNave más grande:")
    print(nave_mas_grande)