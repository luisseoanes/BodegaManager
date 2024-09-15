from INVENTARIO import INVENTARIO
from ORDEN import ORDEN

import os

class Empleado:
    def __init__(self, tienda):
        """Inicializa el administrador con una tienda asociada."""
        self.tienda = tienda  
        self.inventario = INVENTARIO(self.tienda) # Asocia el inventario de la tienda con la clase INVENTARIO
        self.ruta_base = "Tiendas"  # Carpeta que sí existe
        self.ruta_tienda = os.path.join(self.ruta_base, self.tienda)



    def consultarInventario(self):
        """Consulta y muestra el inventario de la tienda usando el método de INVENTARIO."""
        inventario = self.inventario.listarProductos()
        print(inventario)

    def consultarOrden(self):
        IdOrden = input("Ingrese el Id de la Orden: ")
        ruta = os.path.join(self.ruta_tienda, 'ordenes.csv')
        ORDEN(ruta)
        ORDEN.consultarEstado(IdOrden)

