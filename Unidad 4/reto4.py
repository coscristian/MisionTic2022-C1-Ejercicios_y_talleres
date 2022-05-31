from functools import reduce

def ordenes(rutinaContable):
    print('------------------------ Inicio Registro diario ---------------------------------')
    for lista in rutinaContable:
        total_factura = 0
        precio_articulo = list(map(lambda articulo: articulo[1] * articulo[2], lista[1:]))
        total_factura = reduce(lambda x,y: x+y, precio_articulo)
        if total_factura < 600000:
            total_factura += 25000
        print(f"La factura {lista[0]} tiene un total en pesos de {total_factura:,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')

#Datos para correr el programa
rutinaContable = [
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

ordenes(rutinaContable)