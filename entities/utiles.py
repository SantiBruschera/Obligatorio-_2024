from datetime import datetime
from entities.especialidad_dos import Especialidad
from entities.medico_dos import Medico
from entities.consulta_medica import ConsultaMedica
from entities.socio_dos import Socio
from entities.persona_dos import Persona

def es_fecha_valida(fecha_str):#utiliza datetime para fijarse que sea una fecha valida
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False 
        

#1. Dar de alta especialidad
def verificar_nombre_especialidad(nombre_especialidad):
    while nombre_especialidad.isdigit() or nombre_especialidad=='':
        nombre_especialidad= input("La especialidad debe ser un string")
    return nombre_especialidad

def verificar_precio(precio):
            while not precio.isdigit() or int(precio)<=0:
                print("El precio de la especialidad es incorrecto, ingréselo nuevamente")
                precio = str(input("Precio: "))


#2. Dar de alta un socio
def verificar_nombre(nombre):#cambie el verificar datos, a una funcion por dato para que la correccion sea inmediata
    while nombre.isdigit() or nombre=='':
        print("No es un nombre válido, ingréselo de nuevo.")
        nombre = input("Ingrese el nombre: ")
    return nombre

def verificar_apellido(apellido):
    while apellido.isdigit() or apellido=='':
        print("No es un apellido válido, ingréselo de nuevo.")
        apellido = input("Ingrese el apellido: ")
    return apellido

def verificar_cedula(cedula):
    while not str(cedula).isdigit() or len(str(cedula)) != 8:
        print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        cedula = input("Ingrese la cédula de identidad (8 dígitos): ")
    return cedula

def verificar_fecha_nac(fecha_nac):
    while not es_fecha_valida(fecha_nac):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_nac = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
    return fecha_nac

def verificar_fecha_ing(fecha_ing):
    while not es_fecha_valida(fecha_ing):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_ing = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
    return fecha_ing

def verificar_celular(celular):
    while not celular.isdigit() or len(str(celular)) != 9 or not str(celular).startswith('09'):
        print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
        celular = input("Ingrese el número de celular (9 dígitos): ")
    return celular

def verificar_tipo_socio(tipo):
        while int(tipo) != 1 and int(tipo) != 2:
            print('El valor ingresado no es correcto, elige la opción 1 o 2.')
            tipo=int(input('tipo de socio: '))
        return tipo


#3. Dar de alta un médico, las del 2 pero en vez de verificar tipo socio, verificar especialidad
def buscar_especialidad(especialidad, especialidades):
    for item in especialidades:
        if item.especialidad == especialidad:
            return True
    return False

def verificar_especialidad_2(especialidades, especialidad_dada):
    while especialidad_dada not in especialidades:
        for especialidad in especialidades:
            if especialidad.especialidad==especialidad_dada:
                return especialidad_dada
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
                especialidad_dada = input('Especialidad: ')
            elif opcion == 2:
                precio = input('Precio: ')
                verificar_precio(precio)
                e=Especialidad(especialidad_dada, precio)
                especialidades.append(e)
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")




#4. Dar de alta una consulta médica (ademas despues verificar especialidad)
def verificar_nombre_especialidad(nombre_especialidad):
    while nombre_especialidad.isdigit() or nombre_especialidad=='':    
        print("La especialidad debe ser un string")
        nombre_especialidad = input("Ingrese la especialidad: ")
    return nombre_especialidad

def verificar_nombre_medico(nombre_medico):
    while nombre_medico.isdigit() or nombre_medico=='':    
        print("El medico debe ser un string")
        nombre_medico = input("Ingrese el medico: ")
    return nombre_medico

def verificar_nombre_completo_medico(nombre_completo, medicos, especialidades):
    while True:
        for medico in medicos:
            if medico.get_nombre+' '+medico.get_apellido==nombre_completo:
                return nombre_completo
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
                nombre_completo= input('Medico: ')
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
                verificar_especialidad_2(especialidades, especialidad)
                m=Medico(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, especialidad)
                medicos.append(m)
        except ValueError:
                print("Por favor, ingrese un número válido.")



def verificar_medico( medico_dado, medicos, especialidades):
    while medico_dado not in medicos:
        for medico in medicos:
            if medico.get_nombre==medico_dado:
                return medico_dado
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
                medico_dado= input('Medico: ')
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
                verificar_especialidad_2(especialidades, especialidad)
                m=Medico(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, especialidad)
                medicos.append(m)
        except ValueError:
                print("Por favor, ingrese un número válido.")

def buscar_medico(medico_i, medicos):
        for medico in medicos:
                if medico.get_nombre+" "+medico.get_apellido==medico_i:
                    return True
                return False


def verificar_cantidad_max(cantidad_max):
    while True:
        if not cantidad_max.isdigit() or int(cantidad_max)<0:
            print("La cantidad maxima no puede ser cero o menor, ingréselo nuevamente")
            cantidad_max = str(input("Cantidad máxima: "))
        else:
            break

def verificar_fecha_consulta(fecha_consulta):
    while not es_fecha_valida(fecha_consulta):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_consulta = input("Ingrese la fecha de consulta en formato aaaa-mm-dd: ")


#5. Emitir un ticket de consulta (verificar nombre especialidad, verificar especialidad)
def mostrar_consultas(consultas, especialidad):
    lista=[]
    n=1
    for consulta in consultas:
        if consulta.get_nombre_especialidad == especialidad:
            print(f"{n} - Doctor:{consulta.get_nombre_medico}  Dia de la consulta: {consulta.get_fecha_consulta}")
            lista.append((consulta.get_nombre_medico, consulta.get_fecha_consulta))
            n+=1
    return lista

def elegir_consulta(nombre, fecha, especialidad, consultas):
    for consulta in consultas:
        if consulta.get_nombre_medico==nombre and consulta.get_fecha_consulta==fecha and consulta.get_nombre_especialidad==especialidad:
            return consulta
    



def verificar_cedula_in_socio(cedula, socios):
    for socio in socios:
        este=False
        if cedula == socio.get_cedula:
            este=True
    if este==False:
        opcion=0
        while opcion not in [1,2]:
            opcion=input('Este socio no está dado de alta, elija una opción:\n'
            '- 1 - Volver a ingresar el socio \n'
            '- 2 - Dar de alta el socio')
            if opcion==1:
                cedula=input("socio: ")
            elif opcion==2:
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
                tipo=input('tipo de socio, bonificado(1) o no bonificado(2)')
                verificar_tipo_socio(tipo)
                s=Socio(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, tipo)
                socios.append(s)
    else: 
        return cedula

def agregar_deuda(cedula, especialidad_1, especialidades, socios):
    for socio in socios:
        if int(socio.get_cedula)==int(cedula):
            for especialidad in especialidades:
                if especialidad.especialidad==especialidad_1:
                    if int(socio.get_tipo)==1:
                        precio_consulta=int(especialidad.get_precio)*0.8
                        socio.set_deuda(precio_consulta)
                        print(socio.get_deuda)
                    else:
                        socio.set_deuda(int(especialidad.get_precio))
                        print(socio.get_deuda)


#6. Realizar consultas
def verificar_fecha(fecha):
    while not es_fecha_valida(fecha):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha = input("Ingrese la fecha en formato aaaa-mm-dd: ") 
    return fecha

def mostrar_deuda_ordenada(socios):
    lista=[]
    print(socios)
    for socio in socios:
        lista.append((socio.get_deuda,socio.get_nombre))
    lista_ordenada= sorted(lista, key=lambda x:x[0])
    print(lista_ordenada)
    

def cant_consultas_entre_fechas(fecha_inicio, fecha_final, consultas):
    cantidad_consultas=0
    if fecha_inicio<=fecha_final:
        for consulta in consultas:
            if fecha_inicio<=consulta.get_fecha_consulta<=fecha_final:
                cantidad_consultas+=int(consulta.get_cant_pacientes)
    print(cantidad_consultas)


def ganancias_entre_fechas(fecha_inicio, fecha_final, socios, especialidades, consultas):
    plata=0
    if fecha_inicio<fecha_final:
        for socio in socios:
            for consulta in consultas:
                for especialidad in especialidades:
                    if fecha_inicio<=consulta.get_fecha_consulta<=fecha_final:
                        if int(socio.get_tipo)==1:
                            plata+=(int(especialidad.get_precio)*0.8)
                        else:
                            plata+=int(especialidad.get_precio)
    return plata