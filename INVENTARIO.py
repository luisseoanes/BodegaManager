import pandas as pd
import os
import PRODUCTO as PRODUCTO

class INVENTARIO:
    def __init__(self, nombreTienda):
        self.nombreTienda = nombreTienda
        self.ruta_bodega = os.path.join('Tiendas', self.nombreTienda, 'bodega.csv')

        self.inventario = pd.read_csv(self.ruta_bodega)

    def agregarProducto(self):
        
        # Solicitar información del producto al usuario
        id_producto = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad_stock = int(input("Ingrese la cantidad en stock: "))
        proveedor = input("Ingrese el nombre del proveedor: ")
        fechaIngreso = input("Ingrese la fecha de ingreso: ")


        # Crear un diccionario con la información del nuevo producto
        nuevo_producto = {
            'ID': id_producto,
            'Nombre del Producto': nombre,
            'Descripcion': descripcion,
            'Precio por Unidad': precio,
            'Cantidad en Stock': cantidad_stock,
            'Proveedor' : proveedor,
            'Fecha de Ingreso': fechaIngreso
        }

        # Convertir el diccionario a un DataFrame
        nuevo_producto_df = pd.DataFrame([nuevo_producto])
        # Agregar el Dataframe al archivo
        self.inventario = pd.read_csv(self.ruta_bodega)
        self.inventario = pd.concat([self.inventario, nuevo_producto_df], ignore_index=True)
        self.inventario.to_csv(self.ruta_bodega, index=False)
        
        print("Producto agregado con éxito.")

    def eliminarProducto(self):
        """Eliminar un producto del inventario por su ID."""
        idProducto = input("Ingrese el ID del producto que desea eliminar: ")

        if self.inventario['ID'].astype(str).isin([str(idProducto)]).any():
            self.inventario = self.inventario[self.inventario['ID'].astype(str) != str(idProducto)]
            self.inventario.to_csv(self.ruta_bodega, index=False)  # Guardar cambios en el archivo CSV
            print(f"Producto con ID {idProducto} eliminado.")
        else:
            print(f"Producto con ID {idProducto} no encontrado.")

    def buscarProducto(self, idProducto):

        self.inventario["ID"] = self.inventario['ID'].astype(str)
        producto = self.inventario.loc[self.inventario['ID'] == idProducto]
        print(producto)

    def listarProductos(self):
        """Listar todos los productos del inventario."""
        return self.inventario
