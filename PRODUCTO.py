import pandas as pd
class PRODUCTO:
    def __init__(self, ruta):
        self.ruta = ruta
        
    def actualizarPrecio(self, IdProducto, nuevoPrecio):
        """Actualizar el precio del producto."""
        productos = pd.read_csv(self.ruta)
        productos['ID'] = productos['ID'].astype(str)

        if IdProducto not in productos['ID'].values:
            print(f"Producto con ID {IdProducto} no encontrado.")
            return


        productos.loc[productos['ID'] == IdProducto, 'Precio por Unidad'] = nuevoPrecio
        productos.to_csv(self.ruta, index=False)
        print(f"El precio del producto con ID {IdProducto} ha sido actualizado a {nuevoPrecio}.")

    def actualizarCantidad(self, IdProducto, nuevaCantidad):
        """Actualizar la cantidad en stock del producto."""
        self.cantidad = nuevaCantidad
        productos = pd.read_csv(self.ruta)
        productos['ID'] = productos['ID'].astype(str)

        if IdProducto not in productos['ID'].values:
            print(f"Producto con ID {IdProducto} no encontrado.")
            return
        productos.loc[productos['ID'] == IdProducto, 'Cantidad en Stock'] = nuevaCantidad
        productos.to_csv(self.ruta, index=False)
        print(f"La cantidad del producto con ID {IdProducto} ha sido actualizado a {nuevaCantidad}.")
    
