import pandas as pd

class PROVEEDOR:
    def __init__(self, IdProveedor):
        """Inicializa el proveedor buscando la información en el archivo CSV."""
        self.proveedores = pd.read_csv('Datos/proveedores.csv')
        
        # Buscar el proveedor por ID
        proveedor = self.proveedores[self.proveedores['ID Proveedor'] == IdProveedor]
        if not proveedor.empty:
            # Si el proveedor existe, inicializar sus datos
            self.IdProveedor = IdProveedor
            self.nombre = proveedor.iloc[0]['Nombre']
            self.telefono = proveedor.iloc[0]['Teléfono']
            self.direccion = proveedor.iloc[0]['Dirección']
        else:
            print(f"Proveedor con ID {IdProveedor} no encontrado.")
            self.IdProveedor = None
            self.nombre = None
            self.telefono = None
            self.direccion = None

    def ObtenerContacto(self):
        """Obtener los detalles de contacto del proveedor."""
        if self.IdProveedor:
            contacto = f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Dirección: {self.direccion}"
            print(contacto)
            return contacto
        else:
            print("Proveedor no encontrado.")
            return None

    def ActualizarDatos(self, NuevoTelefono, NuevaDireccion):
        """Actualizar el teléfono y la dirección del proveedor en el archivo CSV."""
        if self.IdProveedor:
            self.proveedores.loc[self.proveedores['ID Proveedor'] == self.IdProveedor, 'Teléfono'] = NuevoTelefono
            self.proveedores.loc[self.proveedores['ID Proveedor'] == self.IdProveedor, 'Dirección'] = NuevaDireccion
            self.proveedores.to_csv('Datos/proveedores.csv', index=False)
            self.telefono = NuevoTelefono
            self.direccion = NuevaDireccion
            print(f"Datos del proveedor con ID {self.IdProveedor} actualizados.")
        else:
            print("Proveedor no encontrado.")
