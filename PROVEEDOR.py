import pandas as pd
import os

class PROVEEDOR:
    def __init__(self, IdProveedor, NombreTienda):
        """Inicializa el proveedor buscando la información en el archivo CSV."""
        self.rutaProveedores = os.path.join('Tiendas', NombreTienda, 'Proveedores.csv')

        # Leer el archivo CSV
        self.proveedores = pd.read_csv(self.rutaProveedores)
        
        # Limpiar nombres de las columnas de posibles espacios en blanco
        self.proveedores.columns = self.proveedores.columns.str.strip()

        # Asegurarse de que 'ID Proveedor' sea del tipo adecuado para la comparación
        self.proveedores['ID Proveedor'] = self.proveedores['ID Proveedor'].astype(str)

        # Buscar el proveedor por ID
        proveedor = self.proveedores[self.proveedores['ID Proveedor'] == str(IdProveedor)]
        if not proveedor.empty:
            # Si el proveedor existe, inicializar sus datos
            self.IdProveedor = IdProveedor
            self.nombre = proveedor.iloc[0]['Nombre']
            self.telefono = proveedor.iloc[0]['Telefono']
            self.direccion = proveedor.iloc[0]['Direccion']
        else:
            print(f"Proveedor con ID {IdProveedor} no encontrado.")
            self.IdProveedor = None
            self.nombre = None
            self.telefono = None
            self.direccion = None

    def ObtenerContacto(self):
        """Obtener los detalles de contacto del proveedor."""
        if self.IdProveedor:
            contacto = f"Nombre: {self.nombre}, Telefono: {self.telefono}, Direccion: {self.direccion}"
            print(contacto)
            return contacto
        else:
            print("Proveedor no encontrado.")
            return None

    def ActualizarDatos(self, NuevoTelefono, NuevaDireccion):
        """Actualizar el teléfono y la dirección del proveedor en el archivo CSV."""
        if self.IdProveedor:
            self.proveedores.loc[self.proveedores['ID Proveedor'] == str(self.IdProveedor), 'Telefono'] = NuevoTelefono
            self.proveedores.loc[self.proveedores['ID Proveedor'] == str(self.IdProveedor), 'Direccion'] = NuevaDireccion
            self.proveedores.to_csv(self.rutaProveedores, index=False)
            self.telefono = NuevoTelefono
            self.direccion = NuevaDireccion
            print(f"Datos del proveedor con ID {self.IdProveedor} actualizados.")
        else:
            print("Proveedor no encontrado.")
