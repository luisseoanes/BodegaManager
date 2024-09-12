import pandas as pd
from PRODUCTO import PRODUCTO

class INVENTARIO:
    def __init__(self):
        self.inventario = pd.read_csv('Datos/bodega.csv')
    
    def agregarProducto(self, producto):
        """Agregar un nuevo producto al inventario."""
        if isinstance(producto, PRODUCTO):
            nuevo_producto = pd.DataFrame([producto.to_dict()])
            self.inventario = pd.concat([self.inventario, nuevo_producto], ignore_index=True)
            self.inventario.to_csv('bodega.csv', index=False)  # Guardar cambios en el archivo CSV
            print("Producto agregado con éxito.")
        else:
            print("Error: El objeto no es una instancia de Producto.")
    
    def eliminarProducto(self, idProducto):
        """Eliminar un producto del inventario por su ID."""
        if idProducto in self.inventario['ID'].values:
            self.inventario = self.inventario[self.inventario['ID'] != idProducto]
            self.inventario.to_csv('bodega.csv', index=False)  # Guardar cambios en el archivo CSV
            print(f"Producto con ID {idProducto} eliminado.")
        else:
            print(f"Producto con ID {idProducto} no encontrado.")
    
    def buscarProducto(self, idProducto):
        """Buscar un producto por su ID."""
        producto = self.inventario[self.inventario['ID'] == idProducto]
        if not producto.empty:
            # Convertir DataFrame a instancia de Producto
            prod_dict = producto.iloc[0].to_dict()
            return PRODUCTO(prod_dict['ID'], prod_dict['Nombre'], prod_dict['Descripción'], 
                            prod_dict['Precio'], prod_dict['Cantidad en Stock'])
        else:
            print(f"Producto con ID {idProducto} no encontrado.")
            return None
    
    def listarProductos(self):
        """Listar todos los productos del inventario."""
        return self.inventario
    
    def actualizarInventario(self, idProducto, nuevaCantidad):
        """Actualizar la cantidad en stock de un producto dado su ID."""
        if idProducto in self.inventario['ID'].values:
            self.inventario.loc[self.inventario['ID'] == idProducto, 'Cantidad en Stock'] = nuevaCantidad
            self.inventario.to_csv('bodega.csv', index=False)  # Guardar cambios en el archivo CSV
            print(f"Cantidad del producto con ID {idProducto} actualizada a {nuevaCantidad}.")
        else:
            print(f"Producto con ID {idProducto} no encontrado.")
