from USUARIO import USUARIO
from TIENDA import TIENDA
from Administrador import ADMINISTRADOR
from Empleado import Empleado


while True:
    OPCION = input(""" 
        Bienvenido a BodegaMaster, Administre su tienda de la manera más sencilla e inteligente
        
        1. INICIE SESION
        2. CREAR CUENTA
                   
        3. SALIR
    """)

    match OPCION:
        case "1": 
            Usuario = input("Ingrese su usuario: ")
            Email = input("Ingrese su email: ")
            Contraseña = input("Ingrese su contraseña: ")

            Sesion = USUARIO(Usuario, Email, Contraseña)
            RespuestaSesion = Sesion.InicioSesion()

            # Si el inicio de sesión fue exitoso, obtenemos los datos del usuario del archivo CSV
            if RespuestaSesion:
                usuarios = Sesion.cargarUsuarios()
                NombreTienda = usuarios[Usuario]["Tienda"]
                TipoCuenta = usuarios[Usuario]["Cuenta"]
                Tienda = TIENDA(NombreTienda)

                if TipoCuenta == "Administrador":
                    print(f"Bienvenido Administrador Sr. {Usuario}. ¿Qué desea hacer?")
                    while True:
                        OPCION2 = input("""
                            1. Agregar un nuevo Producto a la bodega.
                            2. Menu Inventario:
                            3. Agregar Proveedor.
                            4. Menu Proveedores.
                            5. Agregar Orden de compra.
                            6. Menu Ordenes: 

                            7. Cerrar Sesion.
                        """)
                        
                        SesionADMIN = ADMINISTRADOR(NombreTienda)

                        match OPCION2:
                            case "1":
                                ADMINISTRADOR.agregarProducto(SesionADMIN)
                                continue

                            case "2":
                                while True:
                                    OPCION3 = input("""
                                        1. Agregar un nuevo producto a la bodega.
                                        2. Eliminar Producto de la bodega.
                                        3. Buscar Producto por ID.
                                        4. Actualizar precio de producto.
                                        5. Actualizar cantidad de producto.
                                        6. Consultar Inventario.
                                        7. Volver.
                                    """)
                                    
                                    match OPCION3:
                                        case "1":
                                            ADMINISTRADOR.agregarProducto(SesionADMIN)
                                            continue
                                        case "2":
                                            ADMINISTRADOR.eliminarProducto(SesionADMIN)
                                            continue
                                        case "3":
                                            ADMINISTRADOR.buscarProducto(SesionADMIN)
                                            continue
                                        case "4":
                                            TIENDA.actualizarPrecios(Tienda)
                                        case "5":
                                            TIENDA.actualizarCantidad(Tienda)
                                        case "6":
                                            print("Este es el inventario actual: ")
                                            ADMINISTRADOR.consultarInventario(SesionADMIN)
                                            continue
                                        case "7":
                                            break
                
                            case "3":
                                ADMINISTRADOR.agregarProveedor(SesionADMIN)
                                continue

                            case "4":
                                while True:
                                    OPCION3 = input("""
                                        1. Agregar Proveedores.
                                        2. Consultar Proveedores.
                                        3. Obtener contacto proveedor.
                                        4. Actualizar datos proveedor.
                                        5. Volver.
                                    """)
                                    match OPCION3:
                                        case "1":
                                            ADMINISTRADOR.agregarProveedor(SesionADMIN)
                                            continue
                                        case "2":
                                            TIENDA.consultarProveedores(Tienda)
                                            continue
                                        case "3":
                                            ADMINISTRADOR.ObtenerContacto(SesionADMIN)
                                            continue
                                        case "4":
                                            ADMINISTRADOR.ActualizarContacto(SesionADMIN)
                                            continue
                                        case "5":
                                            break

                            case "5":
                                ADMINISTRADOR.generarOrdenDeCompra(SesionADMIN)
                                continue

                            case "6":
                                while True:
                                    OPCION3 = input("""
                                        1. Orden Nueva
                                        2. Cancelar orden
                                        3. Consultar Estado de orden
                                        4. Volver
                                    """)
                                    
                                    match OPCION3:
                                        case "1":
                                            ADMINISTRADOR.generarOrdenDeCompra(SesionADMIN)
                                            continue
                                        case "2":
                                            TIENDA.CancelarOrden(Tienda)
                                            continue
                                        case "3":
                                            TIENDA.consultarOrden(Tienda)
                                            continue
                                        case "4":
                                            break
                            
                            case "7":
                                SesionADMIN = 0
                                Tienda = ""
                                break

                elif TipoCuenta == "Empleado":
                    while True:
                        print(f"Bienvenido Empleado Sr. {Usuario}. ¿Qué desea hacer?")
                        OPCION2 = input("""
                            1. Consultar inventario.
                            2. Consultar Ordenes de compra.
                            3. Cerrar Sesion
                        """)
                        SesionEMPLE = Empleado(NombreTienda)

                        match OPCION2:
                            case "1":
                                print("Este es el inventario actual: ")
                                print(Empleado.consultarInventario(SesionEMPLE))
                                continue
                            case "2":
                                Empleado.consultarOrden(SesionEMPLE)
                                continue
                            case "3":
                                SesionEMPLE = 0
                                Tienda = ""
                                break
                            
        case "2":
            Email = input("Ingrese un email: ")
            Usuario = input("Ingrese un Usuario: ")
            Contraseña = input("Ingrese una contraseña: ")
            TipoCuenta = input("Ingrese el tipo de cuenta: ")
            Tienda = input("Ingrese el nombre de la Tienda: ")

            Sesion = USUARIO(Usuario, Email, Contraseña)
            CuentaCreacion = Sesion.CrearCuenta(TipoCuenta, Tienda)
            continue

        case "3":
            print("Gracias por usar el programa.")
            break
