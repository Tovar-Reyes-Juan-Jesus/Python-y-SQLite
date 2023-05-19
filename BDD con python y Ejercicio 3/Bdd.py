import sqlite3

conexion = sqlite3.connect('Ejemplo.db')

c = conexion.cursor()

c.execute('''CREATE TABLE acciones (fecha text, operacion text, simbolo text, cantidad real, precio real)''')

c.execute("INSERT INTO acciones VALUES ('24/nov/2016', 'compra', 'INV', 100, 15.43)")

c.execute("INSERT INTO acciones VALUES ('25/dic/2011', 'venta', 'INB', 90, 23.43), ('10/feb/2000', 'robo', 'INC', 80, 34.43), ('22/may/2014', 'renta', 'INZ', 70, 44.43), ('11/feb/2022', 'compra', 'INM', 60, 54.43), ('14/ene/2018', 'venta', 'INL', 50, 64.43)")


conexion.commit()

conexion.close()