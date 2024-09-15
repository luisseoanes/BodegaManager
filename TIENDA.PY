import os
import pandas as pd

from PRODUCTO import PRODUCTO
from ORDEN import ORDEN
from PROVEEDOR import PROVEEDOR

class TIENDA:
    def __init__(self, nombreTienda):
        self.nombreTienda = nombreTienda
        self.ruta_base = "Tiendas"  # Carpeta que sí existe
        self.ruta_tienda = os.path.join(self.ruta_base, self.nombreTienda)
        self.crear_directorio_tienda()
        self.crear_archivos_iniciales()

    def crear_directorio_tienda(self):
        """Crear la carpeta 'Tiendas' si no existe y luego una subcarpeta con el nombre de la tienda."""
        # Verificar si la carpeta 'Tiendas' existe, si no, crearla
        if not os.path.exists(self.ruta_base):
            os.makedirs(self.ruta_base)
            print(f"Directorio base '{self.ruta_base}' creado.")
        
        # Crear la carpeta de la tienda dentro de 'Tiendas'
        ruta_tienda = os.path.join(self.ruta_base, self.nombreTienda)
        if not os.path.exists(ruta_tienda):
            os.makedirs(ruta_tienda)
            print(f"Directorio '{ruta_tienda}' creado.")
        
    def crear_archivos_iniciales(self):
        """
        Crea los archivos 'bodega.csv', 'ordenes.csv' y 'proveedores.csv' en el directorio
        de la tienda si no existen.
        """
        archivos = ['bodega.csv', 'ordenes.csv', 'proveedores.csv']
        
        for archivo in archivos:
            ruta_archivo = os.path.join(self.ruta_tienda, archivo)
            if not os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'w') as f:
                    # Crear archivos vacíos con encabezados
                    if archivo == 'bodega.csv':
                        f.write('ID,Nombre del Producto,Descripcion,Cantidad en Stock,Precio por Unidad,Proveedor,Fecha de Ingreso\n')
                    elif archivo == 'ordenes.csv':
                        f.write('ID Orden,Fecha,Cliente,Producto,Cantidad,Total,Estado\n')
                    elif archivo == 'proveedores.csv':
                        f.write('ID Proveedor,Nombre,Contacto,Telefono,Email\n')
                print(f"Archivo '{ruta_archivo}' creado.")

    def AgregarProveedor(self):
        """Agrega un nuevo proveedor al archivo proveedores.csv"""
        ruta_proveedores = os.path.join(self.ruta_tienda, 'proveedores.csv')

        # Leer el archivo CSV
        proveedores_df = pd.read_csv(ruta_proveedores)  # Usamos proveedores_df aquí para consistencia

        IdProveedor = input("Ingrese el ID del proveedor que desea agregar: ")
        Nombre = input("Ingrese el nombre del proveedor: ")
        Contacto = input("Ingrese el contacto del proveedor: ")
        Direccion = input("Ingrese la direccion del proveedor: ")
        Telefono = input("Ingrese el telefono del proveedor: ")
        Email = input("Ingrese el Email del proveedor: ")

        # Verificar si el proveedor ya existe
        if proveedores_df['ID Proveedor'].astype(str).str.contains(str(IdProveedor)).any():
            print(f"El proveedor con ID {IdProveedor} ya existe.")
            return

        # Agregar el nuevo proveedor
        nuevo_proveedor = pd.DataFrame({
            'ID Proveedor': [IdProveedor],
            'Nombre': [Nombre],
            'Contacto': [Contacto],
            'Direccion': [Direccion],
            'Telefono': [Telefono],
            'Email': [Email]
        })

        # Agregar el nuevo proveedor al DataFrame
        proveedores_df = pd.concat([proveedores_df, nuevo_proveedor], ignore_index=True)

        # Guardar los cambios en el archivo CSV
        proveedores_df.to_csv(ruta_proveedores, index=False)
        print(f"Proveedor con ID {IdProveedor} agregado correctamente.")

    def AgregarOrden(self):

        orden = ORDEN(os.path.join(self.ruta_tienda, 'ordenes.csv'))
        # Agregar la orden al archivo de órdenes
        orden.realizarOrden()
    
    def consultarInventario(self):
        """Consulta y devuelve una lista de objetos PRODUCTO que representan el inventario."""
        ruta_bodega = os.path.join(self.ruta_tienda, 'bodega.csv')

        if os.path.exists(ruta_bodega):
            bodega_df = pd.read_csv(ruta_bodega)
            productos = []
            for _, row in bodega_df.iterrows():
                producto = PRODUCTO(row['ID'], row['Nombre'], row['Descripción'], row['Precio'], row['Cantidad en Stock'])
                productos.append(producto)
            return productos
        else:
            print("El archivo de inventario no existe.")
            return []

    def consultarProveedores(self):
        """Consulta y devuelve una lista de objetos PROVEEDOR que representan los proveedores."""
        ruta_proveedores = os.path.join(self.ruta_tienda, 'proveedores.csv')
        proveedores = pd.read_csv(ruta_proveedores)
        print(proveedores)
    
    def CancelarOrden(self):
        orden = ORDEN(os.path.join(self.ruta_tienda, 'ordenes.csv'))
        OrdenCancelar = input("Ingrese el ID de la orden a Cancelar: ")
        ORDEN.cancelarOrden(orden, OrdenCancelar)

    def consultarOrden(self):
        IdOrden = input("Ingrese el Id de la Orden: ")
        ruta = os.path.join(self.ruta_tienda, 'ordenes.csv')
        hola = ORDEN(ruta)
        ORDEN.consultarEstado(hola, IdOrden)

    def actualizarPrecios(self):
        IdProducto = input("Ingrese el ID del producto: ")
        NuevoPrecio = float(input("Ingrese el Nuevo Precio del producto: "))  # Asegúrate de convertir a float
        Producto = PRODUCTO(os.path.join(self.ruta_tienda, 'bodega.csv'))
        PRODUCTO.actualizarPrecio(Producto, IdProducto, NuevoPrecio)

    def actualizarCantidad(self):
        IdProducto = input("Ingrese el ID del producto: ")
        NuevaCantidad = float(input("Ingrese la nueva cantidad del producto: "))  # Asegúrate de convertir a float
        Producto = PRODUCTO(os.path.join(self.ruta_tienda, 'bodega.csv'))
        PRODUCTO.actualizarCantidad(Producto, IdProducto, NuevaCantidad)
