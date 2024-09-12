class PRODUCTO:
    def __init__(self, idProducto, nombre, descripcion, precio, cantidad):
        self.idProducto = idProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizarPrecio(self, nuevoPrecio):
        """Actualizar el precio del producto."""
        self.precio = nuevoPrecio
    
    def actualizarCantidad(self, nuevaCantidad):
        """Actualizar la cantidad en stock del producto."""
        self.cantidad = nuevaCantidad
    
    def obtenerInformacion(self):
        """Obtener información detallada del producto."""
        return (f"ID: {self.idProducto}\n"
                f"Nombre: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Precio: {self.precio}\n"
                f"Cantidad en Stock: {self.cantidad}")

    def to_dict(self):
        """Convertir el producto en un diccionario para agregarlo al DataFrame."""
        return {
            'ID': self.idProducto,
            'Nombre': self.nombre,
            'Descripción': self.descripcion,
            'Precio': self.precio,
            'Cantidad en Stock': self.cantidad
        }
