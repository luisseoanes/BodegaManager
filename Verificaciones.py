import re

class Verificaciones:
    def __init__(self, correo, cuenta) -> None:
        self.correo = correo
        self.cuenta = cuenta

    def ValidoEmail(self):
        # Expresion regular
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

        # Si el str valida la expresion regular
        if re.match(regex, self.correo):
            return True
        else:
            return False
        
    def ValidoTCuenta(self):
        CuentasValidas = ["Administrador",  "Empleado"]
        if self.cuenta in CuentasValidas:
            return True
        else:
            return False
