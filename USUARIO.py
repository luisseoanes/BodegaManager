import csv
import os
from Verificaciones import Verificaciones

class USUARIO:
    def __init__(self, usuario, email, contraseña):
        self.usuario = usuario
        self.email = email
        self.contraseña = contraseña
        self.ruta_usuarios = 'usuarios.csv'  # Archivo CSV para almacenar usuarios

    def cargarUsuarios(self):
        """Cargar todos los usuarios desde el archivo CSV."""
        usuarios = {}
        if os.path.exists(self.ruta_usuarios):
            with open(self.ruta_usuarios, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    usuarios[row['Usuario']] = {
                        "Contraseña": row['Contraseña'],
                        "Email": row['Email'],
                        "Cuenta": row['Cuenta'],
                        "Tienda": row['Tienda']
                    }
        return usuarios

    def guardarUsuarios(self, usuarios):
        """Guardar todos los usuarios en el archivo CSV."""
        with open(self.ruta_usuarios, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Usuario', 'Contraseña', 'Email', 'Cuenta', 'Tienda']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for usuario, datos in usuarios.items():
                writer.writerow({
                    'Usuario': usuario,
                    'Contraseña': datos['Contraseña'],
                    'Email': datos['Email'],
                    'Cuenta': datos['Cuenta'],
                    'Tienda': datos['Tienda']
                })

    def InicioSesion(self):
        """Verificar si el usuario existe y si la contraseña es correcta."""
        usuarios = self.cargarUsuarios()
        if self.usuario in usuarios:
            if usuarios[self.usuario]["Contraseña"] == self.contraseña:
                print("Inicio de Sesión exitoso.")
                return True
            else:
                print("Contraseña incorrecta.")
                return False
        else:
            print("El usuario no existe.")
            return False

    def CrearCuenta(self, TipoCuenta, Tienda):
        """Crear una nueva cuenta y guardarla en el archivo CSV."""
        Comprobacion = Verificaciones(self.email, TipoCuenta)

        if not Comprobacion.ValidoEmail():
            print("El correo electrónico no es válido.")
            return False
        
        if not Comprobacion.ValidoTCuenta():
            print("El tipo de cuenta no valido (Empleado o Administrador)")
            return False
        
        
        usuarios = self.cargarUsuarios()
        if self.usuario in usuarios:
            print("El usuario ya existe.")
            return False
        else:
            usuarios[self.usuario] = {
                "Contraseña": self.contraseña,
                "Email": self.email,
                "Cuenta": TipoCuenta,
                "Tienda": Tienda
            }
            self.guardarUsuarios(usuarios)
            print(f"Usuario {self.usuario} creado con éxito.")
            return True
