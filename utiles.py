from datetime import datetime
from especialidad_dos import Especialidad
from medico_dos import Medico
    
def verificar_fecha(fecha):
    while not es_fecha_valida(fecha):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha = input("Ingrese la fecha en formato aaaa-mm-dd: ")

def es_fecha_valida(fecha_str):#utiliza datetime para fijarse que sea una fecha valida
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

def verificar_nombre(nombre):#cambie el verificar datos, a una funcion por dato para que la correccion sea inmediata
    while not nombre.isalpha():
        print("No es un nombre válido, ingréselo de nuevo.")
        nombre = input("Ingrese el nombre: ")

def verificar_apellido(apellido):
    while not apellido.isalpha():
        print("No es un apellido válido, ingréselo de nuevo.")
        apellido = input("Ingrese el apellido: ")

def verificar_cedula(cedula):
    while not str(cedula).isdigit() or len(str(cedula)) != 8:
        print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        cedula = input("Ingrese la cédula de identidad (8 dígitos): ")

def verificar_fecha_nac(fecha_nac):
    while not es_fecha_valida(fecha_nac):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_nac = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")

def verificar_fecha_ing(fecha_ing):
    while not es_fecha_valida(fecha_ing):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_ing = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
    
def verificar_celular(celular):
    while not celular.isdigit() or len(str(celular)) != 9 or not str(celular).startswith('09'):
        print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
        celular = input("Ingrese el número de celular (9 dígitos): ")

def es_fecha_valida(fecha_str):#utiliza datetime para fijarse que sea una fecha valida
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False 

def verificar_tipo_socio(tipo):
        while int(tipo) != 1 and int(tipo) != 2:
            print('El valor ingresado no es correcto, elige la opción 1 o 2.')
            tipo=int(input('tipo de socio: '))

def verificar_especialidad(especialidad):
        while True:
            if not str(especialidad).isalpha():
                print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                especialidad = str(input("Especialidad: "))
            else:
                break

def verificar_precio(precio):
            while True:
                if not precio.isdigit() or precio<0:
                    print("El precio de la especialidad es incorrecto, ingréselo nuevamente")
                    precio = str(input("Precio: "))
                else:
                    break

def verificar_nombre_medico(nombre_medico):
    while True:
        nombre_medico = input("Ingrese la especialidad: ")
        while not nombre_medico.isalpha():
            print("El médico debe ser un string")   

def verificar_nombre_especialidad(nombre_especialidad):
    while True:    
        nombre_especialidad = input("Ingrese la especialidad: ")
        while not nombre_especialidad.isalpha():
            print("La especialidad debe ser un string")


def verificar_especialidad(especialidad, especialidades):
    while especialidad not in especialidades:
        try:
            opcion = int(input(': Esta especialidad no está dada de alta. Elija una opción:\n'
                            '1 - Volver a ingresar la especialidad\n'
                            '2 - Dar de alta esta especialidad: '))
            while opcion not in [1, 2]:
                print('La opción no es correcta')
                opcion = int(input(': Esta especialidad no está dada de alta. Elija una opción:\n'
                                    '1 - Volver a ingresar la especialidad\n'
                                    '2 - Dar de alta esta especialidad: '))

            if opcion == 1:
                especialidad = input('Especialidad: ')
            elif opcion == 2:
                precio = input('Precio: ')
                verificar_precio(precio)
                e=Especialidad(especialidad, precio)
                especialidades.append(e)
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

def verificar_medico(medico, medicos):
    while medico not in medicos:
        try:
            opcion = int(input(': Este medico no está dado de alta. Elija una opción:\n'
                            '1 - Volver a ingresar el medico\n'
                            '2 - Dar de alta el medico '))
            while opcion not in [1, 2]:
                print('La opción no es correcta')
                opcion = int(input(': Este medico no está dado de alta. Elija una opción:\n'
                            '1 - Volver a ingresar el medico\n'
                            '2 - Dar de alta el medico '))

            if opcion == 1:
                medico = input('Medico: ')
            elif opcion == 2:
                nombre=input('nombre: ')
                verificar_nombre(nombre)
                apellido=input('apellido: ')
                verificar_apellido(apellido)
                cedula=input('cedula: ')
                verificar_cedula(cedula)
                fecha_nac=input('fecha de nacimiento en formato aaaa-mm-dd: ')
                verificar_fecha_nac(fecha_nac)
                fecha_ing=input('fecha de ingreso a la institucion en formato aaaa-mm-dd: ')
                verificar_fecha_ing(fecha_ing)
                num_celular=input('numero de ceulular: ')
                verificar_celular(num_celular)
                especialidad=input('especialidad: ')
                verificar_especialidad(especialidad)
                m=Medico(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, especialidad)
                medicos.append(m)
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")