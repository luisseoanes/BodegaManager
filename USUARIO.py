class USUARIO:
    Usuarios =  {
        "hola" : {"Contrasena": "123GOL", "email": "Hola@gmail.com", "Cuenta":"Administrador", "Tienda":"DonJuan"}
    }
    def __init__(self, usuario, email, contraseña) -> None:
        self.usuario = usuario
        self.email = email
        self.contraseña = contraseña

    def InicioSesion(self, usuario, contraseña) -> bool:
        if self.usuario in USUARIO.usuarios:
            if USUARIO.usuarios[self.usuario]["Contrasena"] == contraseña:
                print("Inicio de Sesion exitoso")
                return True
            else:
                print("Contraseña incorrecta")
                return False
        else: 
            print("El usuario no existe, vuelva a intentarlo")
            return False