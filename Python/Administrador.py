from INVENTARIO import INVENTARIO
from TIENDA import TIENDA
from PROVEEDOR import PROVEEDOR

class ADMINISTRADOR:
    def __init__(self, tienda):
        """Inicializa el administrador con una tienda asociada."""
        self.tienda = tienda
        self.inventario = INVENTARIO(self.tienda) # Asocia el inventario de la tienda con la clase INVENTARIO

    def agregarProducto(self):
        """Agrega un producto al inventario usando el método de la clase INVENTARIO."""
        self.inventario.agregarProducto()

    def eliminarProducto(self):
        """Elimina un producto del inventario usando el método de la clase INVENTARIO."""
        self.inventario.eliminarProducto()

    def actualizarPrecios(self):
        """Actualiza el precio de un producto en el inventario."""
        IdProducto = input("Ingrese el ID del producto: ")
        NuevoPrecio = input("Ingrese el Nuevo Precio del producto: ")

    def consultarInventario(self):
        """Consulta y muestra el inventario de la tienda usando el método de INVENTARIO."""
        inventario = self.inventario.listarProductos()
        print(inventario)

    def agregarProveedor(self):
        """Agrega un nuevo proveedor a la tienda."""
        Tienda = TIENDA(self.tienda)
        TIENDA.AgregarProveedor(Tienda)

    def generarOrdenDeCompra(self):
        """Genera una orden de compra para el proveedor especificado con una lista de productos."""
        Tienda = TIENDA(self.tienda)
        TIENDA.AgregarOrden(Tienda)
    
    def buscarProducto(self):
        IdProducto = input("Ingrese el ID del producto que desea buscar: ")
        self.inventario.buscarProducto(IdProducto)

    def ObtenerContacto(self):
        idProveedor = input("Ingrese el ID del proveedor a contactar: ")
        proveedor = PROVEEDOR(idProveedor, self.tienda)
        PROVEEDOR.ObtenerContacto(proveedor)
    
     def ActualizarContacto(self):
        idProveedor = input("Ingrese el ID del proveedor a contactar: ")
        nuevotelefono = input("Ingrese el nuevo telefono: ")
        nuevaDireccion = input("Ingrese la nueva direccion: ")
        proveedor = PROVEEDOR(idProveedor, self.tienda)
        proveedor.ActualizarDatos(nuevotelefono, nuevaDireccion)
