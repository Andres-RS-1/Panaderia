from abc import abstractmethod, ABC as Abstract

class Persona(Abstract):
    def __init__(self, nombre, numeroId):
        self.__nombre = nombre
        self.__numeroId = numeroId

    def obtenerNombre(self):
        return self.__nombre

    def obtenernumeroID(self):
        return self.__numeroId

    def modificarNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def modificarNumeroID(self, nuevoNumeroID):
        self.__numeroId = nuevoNumeroID

class Pan:
    def __init__(self, tipoPan, nombrePan, cantidadPan):
        self.__tipoPan = tipoPan
        self.__nombrePan = nombrePan
        self.__cantidadPan = cantidadPan
        self.__precioPan = self.definirPrecioPan()

    def definirPrecioPan(self):
        if self.__tipoPan == "calentano":
            return 1000
        elif self.__tipoPan == "hojaldre":
            return 700
        else:
            return 0

    def obtenerTipoPan(self):
        return self.__tipoPan

    def obtenerNombrePan(self):
        return self.__nombrePan

    def obtenercantidadPan(self):
        return self.__cantidadPan

    def obtenerPrecioPan(self):
        return self.__precioPan

    def modificarTipoPan(self, nuevoTipoPan):
        self.__tipoPan = nuevoTipoPan

    def modificarNombrePan(self, nuevoNombrePan):
        self.__nombrePan = nuevoNombrePan

    def modificarCantidadPan(self, nuevaCantidad):
        self.__cantidadPan = nuevaCantidad

    def modificarPrecioPan(self, nuevoPrecio):
        self.__precioPan = nuevoPrecio

class Empleado:
    def __init__(self, salario, añoIngreso):
        self.__tiempoDeExperiencia = 0
        self.__salario = salario
        self.__añoIngreso = añoIngreso

    def obtenerTiempoExperiencia(self):
        return self.__tiempoDeExperiencia

    def modificarTiempoDeExperiencia(self, añoActual):
        self.__tiempoDeExperiencia = añoActual - self.__añoIngreso

    def obtenerSalario(self):
        return self.__salario

    def modificarSalario(self, nuevoSalario):
        self.__salario = nuevoSalario

    def obetenerAñoIngreso(self):
        return self.__añoIngreso

    def modificarAñoIngreso(self, nuevoAñoIngreso):
        self.__añoIngreso = nuevoAñoIngreso

class Cliente:
    def __init__(self, nombre, numeroId):
        self.__nombre = nombre
        self.__numeroId = numeroId
        self.__pedido = []
        self.__totalPuntos = 0

    def agregarProductoAPedido(self, producto):
        self.__pedido.append(producto)

    def obtenerTotalPuntos(self):
        return self.__totalPuntos

    def asignarPuntos(self, puntos):
        self.__totalPuntos += puntos

    def obtenerNombre(self):
        return self.__nombre

    def modificarNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def obtenerNumeroId(self):
        return self.__numeroId

    def modificarNumeroId(self, nuevoNumeroId):
        self.__numeroId = nuevoNumeroId

    def verPedido(self):
        return self.__pedido

    def eliminarProductoDelPedido(self, producto):
        if producto in self.__pedido:
            self.__pedido.remove(producto)

    def vaciarPedido(self):
        self.__pedido.clear()

class Panadero(Empleado):
    def __init__(self, salario, añoIngreso):
        super().__init__(salario, añoIngreso)
        self.__produccionRealizada = 0

    def producirPan(self, cantidadProduccion):
        self.__produccionRealizada += cantidadProduccion
        print(f"se produjeron con exito {cantidadProduccion}")

    def obtenerProduccionRealizada(self):
        return self.__produccionRealizada

class Main:
    def __init__(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                sesion = self.iniciarSesion()
            elif opcion == 2:
                registrar = self.registrarse()
            elif opcion == 3:
                print("se cerro el programa correctamente ")
                break
            else:
                print("opcion incorrecta")

            self.iniciarSesion()
            self.registrarse()
            self.menu()

    def iniciarSesion(self):
        usuario = input("ingrese su usuario")
        contraseña = input("ingrese su contraseña ")
        listaUsuarios = ["Admin"]  # Agregar lista de usuarios
        if usuario == "Admin" and contraseña == "1234":
            print("bienvenido usuario.")
        elif usuario in listaUsuarios:
            pass  # Contraseña:

    def menu(self):
        while True:
            try:
                opcion = int(input("Menú \n Presione 1 para iniciar sesión \nPresione 2 para registrarse\n presione 3 para salir "))
                return opcion
            except:
                print("caracteres no validos")

class Vendedor(Empleado):  # Corregido 'empleado' a 'Empleado'
    def __init__(self, dineroEnCaja, totalVentas):
        self.__dineroEnCaja = 0.0
        self.__totalVentas = 0

    def venderPan(self, tipoDePan, cantidad):
        pass

    def modificarCantidadPan(self, tipoDePan, nuevaCantidad):
        self.__cantidadPan = nuevaCantidad

    def obtenerDineroEnCaja(self):
        return self.__dineroEnCaja

    def modificarDineroEnCaja(self, cantidad):
        self.__dineroEnCaja += cantidad

class Aseador(Empleado):
    def __init__(self, salario, añoIngreso):
        super().__init__(salario, añoIngreso)
        self.__tareasRealizadas = []

    def realizarTarea(self, tarea):
        self.__tareasRealizadas.append(tarea)
        print(f"Se realizó con éxito la tarea: {tarea}")

    def obtenerTareasRealizadas(self):
        return self.__tareasRealizadas

class Administrador:
    def __init__(self):
        self.usuarios = {"Admin": "1234"}
        self.empleados = []

    def iniciarSesion(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
            return True
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
            return False

    def contratarEmpleado(self):
        salario = float(input("Ingrese el salario del empleado: "))
        añoIngreso = int(input("Ingrese el año de ingreso del empleado: "))
        empleado = Empleado(salario, añoIngreso)
        self.empleados.append(empleado)
        return empleado

    def despedirEmpleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            print("Empleado despedido con éxito.")
        else:
            print("El empleado no se encuentra en la lista de empleados activos.")

    def modificarSalarioEmpleado(self, empleado):
        nuevoSalario = float(input("Ingrese el nuevo salario del empleado: "))
        empleado.modificarSalario(nuevoSalario)
        print("Salario del empleado modificado con éxito.")

    def activarDesactivarEmpleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)  # Desactivar empleado
            print("Empleado desactivado con éxito.")
        else:
            self.empleados.append(empleado)  # Activar empleado
            print("Empleado activado con éxito.")
