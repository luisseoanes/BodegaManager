import os

class Tienda:
    def __init__(self, nombreTienda):
        self.nombreTienda = nombreTienda
        self.ruta_base = "Tiendas"  # Carpeta que sí existe
        self.crear_directorio_tienda()
        self.crear_archivos_iniciales()


    def crear_directorio_tienda(self):
        """Crear la carpeta 'Tiendas' si no existe y luego una subcarpeta con el nombre de la tienda."""
        # Verificar si la carpeta 'Tiendas' existe, si no, crearla
        if not os.path.exists(self.ruta_base):
            os.makedirs(self.ruta_base)
            print(f"Directorio base '{self.ruta_base}' creado.")
        else:
            print(f"El directorio base '{self.ruta_base}' ya existe.")
        
        # Crear la carpeta de la tienda dentro de 'Tiendas'
        ruta_tienda = os.path.join(self.ruta_base, self.nombreTienda)
        if not os.path.exists(ruta_tienda):
            os.makedirs(ruta_tienda)
            print(f"Directorio '{ruta_tienda}' creado.")
        else:
            print(f"El directorio '{ruta_tienda}' ya existe.")

    def crear_archivos_iniciales(self):
        """
        Crea los archivos 'Bodega.csv', 'Ordenes.csv' y 'Proveedores.csv' en el directorio
        de la tienda si no existen.
        """
        archivos = ['Bodega.csv', 'Ordenes.csv', 'Proveedores.csv']
        
        for archivo in archivos:
            ruta_archivo = os.path.join(self.ruta_tienda, archivo)
            if not os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'w') as f:
                    # Crear archivos vacíos con encabezados
                    if archivo == 'Bodega.csv':
                        f.write('ID,Nombre,Descripción,Precio,Cantidad en Stock\n')
                    elif archivo == 'Ordenes.csv':
                        f.write('ID Orden,Fecha,Cliente,Producto,Cantidad,Total\n')
                    elif archivo == 'Proveedores.csv':
                        f.write('ID Proveedor,Nombre,Contacto,Teléfono,Email\n')
                print(f"Archivo '{ruta_archivo}' creado.")
            else:
                print(f"El archivo '{ruta_archivo}' ya existe.")

