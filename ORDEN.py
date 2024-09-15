import pandas as pd

class ORDEN:
    def __init__(self, ruta):
        """Inicializa una orden y carga los datos directamente desde el archivo CSV."""
        self.ruta = ruta
         # Estado de la orden: 'Solicitada', 'Pendiente', 'Cancelada', 'Completada'
        self.estado = "Solicitada"

    def realizarOrden(self):
        """Agregar una nueva orden al archivo CSV con estado 'Solicitada'."""
        ordenes = pd.read_csv(self.ruta)

        IdOrden = input("Ingrese el ID de la Orden: ")
        producto = input("Ingrese el producto: ")
        Cliente = input("Ingrese el nombre de su tienda: ")
        cantidad = input("Ingrese la cantidad: ")
        proveedor = input("Ingrese el proveedor: ")
        fechaOrden = input("Ingrese la fecha de la orden: ")

        NuevaOrden = { 
            'ID Orden': IdOrden,
            'Fecha': fechaOrden,
            'Cliente': Cliente,
            'Producto': producto,
            'Cantidad': cantidad,
            'Proveedor': proveedor,
            'Estado': self.estado}

        if ordenes['ID Orden'].astype(str).str.contains(str(IdOrden)).any():
            print(f"La orden con ID {IdOrden} ya existe.")
            return

        nueva_orden = pd.DataFrame([NuevaOrden])
        ordenes = pd.concat([ordenes, nueva_orden], ignore_index=True)
        ordenes.to_csv(self.ruta, index=False)  # Guardar en el archivo CSV
        print("Orden con ID" + IdOrden +  " realizada con éxito con el proveedor: " + proveedor)

    def cancelarOrden(self, IdOrden):
        """Cambiar el estado de la orden a 'Cancelada' en el archivo CSV."""
        ordenes = pd.read_csv(self.ruta)
        ordenes['ID Orden'] = ordenes['ID Orden'].astype(str)
        if IdOrden in ordenes['ID Orden'].values:
            ordenes.loc[ordenes['ID Orden'] == IdOrden, 'Estado'] = 'Cancelada'
            ordenes.to_csv(self.ruta, index=False)
            print(f"Orden con ID {IdOrden} cancelada.")
        else:
            print(f"Orden con ID {IdOrden} no encontrada.")
 
    def consultarEstado(self, IdOrden):
        """Consultar el estado actual de la orden directamente desde el archivo CSV."""
        ordenes = pd.read_csv(self.ruta)
        ordenes['ID Orden'] = ordenes['ID Orden'].astype(str)

        orden = ordenes[ordenes['ID Orden'] == IdOrden]
        if not orden.empty:
            estado = orden.iloc[0]['Estado']
            print(f"El estado de la orden con ID {IdOrden} es: {estado}")
            return estado
        else:
            print(f"Orden con ID {IdOrden} no encontrada.")
            return "No encontrado"
