import pandas as pd
from PRODUCTO import PRODUCTO
from PROVEEDOR import PROVEEDOR

class ORDEN:
    def __init__(self, IdOrden, producto, cantidad, proveedor, fechaOrden, estado="Pendiente"):
        """Inicializa una orden y carga los datos directamente desde el archivo CSV."""
        self.IdOrden = IdOrden
        self.producto = producto
        self.cantidad = cantidad
        self.proveedor = proveedor
        self.fechaOrden = fechaOrden
        self.estado = estado  # Estado de la orden: 'Pendiente', 'Cancelada', 'Completada'
        
        # Cargar el archivo CSV cuando se inicializa la clase
        self.archivo_ordenes = 'Datos/orden.csv'
        
        # Crear el archivo si no existe
        try:
            pd.read_csv(self.archivo_ordenes)
        except FileNotFoundError:
            columnas = ['ID Orden', 'Producto', 'Cantidad', 'Proveedor', 'Fecha Orden', 'Estado']
            pd.DataFrame(columns=columnas).to_csv(self.archivo_ordenes, index=False)

    def to_dict(self):
        """Convertir la orden en un diccionario para agregarla al DataFrame."""
        return {
            'ID Orden': self.IdOrden,
            'Producto': self.producto.idProducto,
            'Cantidad': self.cantidad,
            'Proveedor': self.proveedor.IdProveedor,
            'Fecha Orden': self.fechaOrden,
            'Estado': self.estado
        }

    def realizarOrden(self):
        """Agregar una nueva orden al archivo CSV con estado 'Pendiente'."""
        ordenes = pd.read_csv(self.archivo_ordenes)
        nueva_orden = pd.DataFrame([self.to_dict()])
        ordenes = pd.concat([ordenes, nueva_orden], ignore_index=True)
        ordenes.to_csv(self.archivo_ordenes, index=False)  # Guardar en el archivo CSV
        print("Orden realizada con éxito.")

    def cancelarOrden(self):
        """Cambiar el estado de la orden a 'Cancelada' en el archivo CSV."""
        ordenes = pd.read_csv(self.archivo_ordenes)
        if self.IdOrden in ordenes['ID Orden'].values:
            ordenes.loc[ordenes['ID Orden'] == self.IdOrden, 'Estado'] = 'Cancelada'
            ordenes.to_csv(self.archivo_ordenes, index=False)
            print(f"Orden con ID {self.IdOrden} cancelada.")
        else:
            print(f"Orden con ID {self.IdOrden} no encontrada.")

    def consultarEstado(self):
        """Consultar el estado actual de la orden directamente desde el archivo CSV."""
        ordenes = pd.read_csv(self.archivo_ordenes)
        orden = ordenes[ordenes['ID Orden'] == self.IdOrden]
        if not orden.empty:
            estado = orden.iloc[0]['Estado']
            print(f"El estado de la orden con ID {self.IdOrden} es: {estado}")
            return estado
        else:
            print(f"Orden con ID {self.IdOrden} no encontrada.")
            return "No encontrado"
