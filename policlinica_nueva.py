from socio_dos import Socio
from medico_dos import Medico
from especialidad_dos import Especialidad
from consulta_medica import ConsultaMedica
from utiles import verificar_cantidad_max
from utiles import verificar_fecha_consulta
from utiles import verificar_especialidad
from utiles import verificar_tipo_socio
from utiles import verificar_especialidad
from utiles import verificar_precio
from utiles import verificar_nombre
from utiles import verificar_apellido
from utiles import verificar_cedula
from utiles import verificar_fecha_nac
from utiles import verificar_fecha_ing
from utiles import verificar_celular
from utiles import verificar_fecha
from utiles import verificar_medico
from utiles import verificar_nombre_medico
from utiles import verificar_especialidad
from utiles import verificar_nombre_especialidad
from utiles import mostrar_consultas
from utiles import verificar_cedula_in_socio
from utiles import agregar_deuda
from utiles import mostrar_deuda_ordenada
from utiles import elegir_consulta
from utiles import cant_consultas_entre_fechas
from utiles import ganancias_entre_dos_fechas
# from utiles import mostrar_consultas


class Policlinica():
    def __init__(self, nombre): #los arrayssiempre tienen que ir como constructores, dentro del init. Tenemos que hacerles getters y setters. Arreglar lo que nos dijo flor de que escribiamos mal los getters y setters. Y hacer lo de socios bonificados y no bonificados. 
        self.__nombre = nombre
        self.medicos = [] 
        self.socios = [] 
        self.especialidades = []
        self.consultas = []
    
    @property
    def get_nombre_policlinica(self):
        return self.__nombre
    
    def get_especialidad(self):
        for especialidad in self.especialidades:
            return especialidad.get_especialidad#funcion para retornar el nombre de la especialidad

    def menu(self):
        while True:
            opcion = input('Seleccione una opción del menú:\n'
                '1. Dar de alta una especialidad\n'
                '2. Dar de alta un socio\n'
                '3. Dar de alta un médico\n'
                '4. Dar de alta una consulta médica\n'
                '5. Emitir un ticket de consulta\n'
                '6. Realizar consultas\n'
                '7. Salir del programa\n'
                '')
            
            if opcion.isdigit() and 0 < int(opcion) < 8:
                opcion = int(opcion) 

                if opcion == 1:
                    especialidad = input('Ingrese el nombre de la especialidad: ')
                    verificar_nombre_especialidad(especialidad)
                    precio = input('Ingrese el precio asociado: ')
                    verificar_precio(precio)
                    e=Especialidad(especialidad, precio)
                    self.especialidades.append(e)
                    for especialidad in self.especialidades:
                        print(especialidad.especialidad)

                elif opcion == 2:
                    nombre=input('Ingrese el nombre: ')
                    verificar_nombre(nombre)
                    apellido=input('Ingrese el apellido: ')
                    verificar_apellido(apellido)
                    cedula=input('Ingrese la cédula de identidad: ')
                    verificar_cedula(cedula)
                    fecha_nac=input('Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ')
                    verificar_fecha_nac(fecha_nac)
                    fecha_ing=input('Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ')
                    verificar_fecha_ing(fecha_ing)
                    num_celular=input('Ingrese el número de celular: ')
                    verificar_celular(num_celular)
                    tipo=input('Ingrese el tipo de socio: 1- Bonificado 2- No bonificado ')
                    verificar_tipo_socio(tipo)
                    s=Socio(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, tipo, 0)
                    self.socios.append(s)
                    for socio in self.socios:
                        print (socio.get_nombre)
                        
                elif opcion == 3:
                    nombre=input('Ingrese el nombre: ')
                    verificar_nombre(nombre)
                    apellido=input('Ingrese el apellido: ')
                    verificar_apellido(apellido)
                    cedula=input('Ingrese la cédula de identidad: ')
                    verificar_cedula(cedula)
                    fecha_nac=input('Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ')
                    verificar_fecha_nac(fecha_nac)
                    fecha_ing=input('Ingrese la fecha de ingreso a la institucion en formato aaaa-mm-dd: ')
                    verificar_fecha_ing(fecha_ing)
                    num_celular=input('Ingrese el número de celular: ')
                    verificar_celular(num_celular)
                    especialidad=input('Ingrese la especialidad: ')
                    verificar_especialidad(especialidad,self.especialidades)
                    m=Medico(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, especialidad)
                    self.medicos.append(m)
                    for medico in self.medicos:
                        print(medico.get_nombre)
                        print(medico.get_especialidad)

                elif opcion == 4:
                    nombre_especialidad = input('Ingrese la especialidad: ')
                    verificar_nombre_especialidad(nombre_especialidad)
                    verificar_especialidad(nombre_especialidad, self.especialidades)
                    nombre_medico = input('Ingrese el nombre del médico: ')      
                    verificar_nombre_medico(nombre_medico)                      
                    verificar_medico(nombre_medico, self.medicos, self.especialidades)             
                    fecha_consulta = input('Ingrese la fecha de consulta (aaaa-mm-dd): ')
                    verificar_fecha_consulta(fecha_consulta)
                    cant_pacientes = input('Ingrese la cantidad de pacientes que se atenderán: ')
                    verificar_cantidad_max(cant_pacientes)
                    consulta = ConsultaMedica(nombre_especialidad, nombre_medico, fecha_consulta, cant_pacientes)
                    self.consultas.append(consulta)


                elif opcion == 5:
                    especialidad=str(input('Ingrese la especialidad: '))
                    verificar_nombre_especialidad(especialidad)
                    verificar_especialidad(especialidad, self.especialidades)
                    mostrar_consultas(self.consultas, especialidad)#
                    opcion_i=input('Seleccione la opción deseada ')
                    elegir_consulta(opcion_i, self.consultas, especialidad)
                    numero=input('Seleccionar el número de atención deseado ')
                    cedula=input('Ingrese la cédula de identidad del socio: ')
                    verificar_cedula(cedula)
                    verificar_cedula_in_socio(cedula, self.socios)
                    agregar_deuda(cedula, especialidad, self.especialidades, self.socios)
                    #agregar descuento dependiendo del tipo de socio

                elif opcion == 6:#verificar porque no funcionan los getters
                    while True:
                        opcion_6=int(input('Seleccione una opción:\n'
                        '1. Obtener todos los médicos asociados a una especialidad específica.\n'
                        '2. Obtener el precio de una consulta de una especialidad en específico.\n'
                        '3. Listar todos los socios con sus deudas asociadas en orden ascendente.\n'
                        '4. Realizar consultas respecto a cantidad de consultas entre dos fechas\n'
                        '5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.'))
                        if int(opcion_6)==1:
                            especialidad_especifica=input('Especialidad especifica: ')
                            verificar_nombre_especialidad(especialidad_especifica)
                            verificar_especialidad(especialidad_especifica, self.especialidades)
                            #si doy de alta una especialidad se termina el programa, va al menu principal, o vuelve a las 5 opciones?
                            for medico in self.medicos:
                                if medico.get_especialidad==especialidad_especifica:
                                    print(medico.get_nombre)
                        elif int(opcion_6)==2:
                            especialidad_especifica=input('Especialidad especifica: ')
                            verificar_nombre_especialidad(especialidad_especifica)
                            verificar_especialidad(especialidad_especifica, self.especialidades)
                            for especialidad in self.especialidades:
                                if especialidad.especialidad==especialidad_especifica:
                                    print(especialidad.get_precio)
                        elif int(opcion_6)==3:
                            mostrar_deuda_ordenada(self.socios)
                        elif int(opcion_6)==4:
                            fecha_inicio=input('Fecha inicio: ')
                            verificar_fecha(fecha_inicio)
                            fecha_final=input('Fecha_final: ')
                            verificar_fecha(fecha_final)
                            cant_consultas_entre_fechas(fecha_inicio, fecha_final, self.consultas)

                        elif int(opcion_6)==5:
                            fecha_inicio=input('Fecha inicio: ')
                            verificar_fecha(fecha_inicio)
                            fecha_final=input('Fecha_final: ')
                            verificar_fecha(fecha_final)
                            ganancias_entre_dos_fechas(fecha_inicio, fecha_final, self.consultas, self.socios)
                        break

                elif opcion == 7:
                    break
                else:
                    print("La opción seleccionada no es correcta, vuelva a intentar con otra opción. ")

if __name__ == '__main__':
    poli = Policlinica('hola')
    poli.menu()
