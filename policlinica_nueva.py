from entities.socio_dos import Socio
from entities.medico_dos import Medico
from entities.especialidad_dos import Especialidad
from entities.consulta_medica import ConsultaMedica
from entities.utiles import verificar_cantidad_max, verificar_numero, verificar_opcion
from entities.utiles import verificar_fecha_consulta
from entities.utiles import verificar_tipo_socio
from entities.utiles import verificar_precio
from entities.utiles import verificar_nombre
from entities.utiles import verificar_apellido
from entities.utiles import verificar_cedula
from entities.utiles import verificar_fecha_nac
from entities.utiles import verificar_fecha_ing
from entities.utiles import verificar_celular
from entities.utiles import verificar_fecha
from entities.utiles import verificar_nombre_medico
from entities.utiles import verificar_especialidad_2
from entities.utiles import verificar_nombre_especialidad
from entities.utiles import mostrar_consultas
from entities.utiles import verificar_cedula_in_socio
from entities.utiles import agregar_deuda
from entities.utiles import mostrar_deuda_ordenada
from entities.utiles import elegir_consulta
from entities.utiles import cant_consultas_entre_fechas
from entities.utiles import ganancias_entre_fechas
from entities.utiles import verificar_nombre_completo_medico
from entities.utiles import mostrar_consultas


class Policlinica():
    def __init__(self): 
        self.medicos = [] 
        self.socios = [] 
        self.especialidades = []
        self.consultas = []
    
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
                    especialidad= input('Ingrese el nombre de la especialidad: ')
                    especialidad= verificar_nombre_especialidad(especialidad)
                    precio= input('Ingrese el precio asociado: ')
                    precio= verificar_precio(precio)
                    e= Especialidad(especialidad, precio)
                    self.especialidades.append(e)
                    print('La especialidad se ha creado con éxito')
                    for especialidad in self.especialidades:
                        print(especialidad.especialidad)
                        print(especialidad.get_precio)

                elif opcion == 2:
                    nombre= input('Ingrese el nombre: ')
                    nombre= verificar_nombre(nombre)
                    apellido= input('Ingrese el apellido: ')
                    apellido= verificar_apellido(apellido)
                    cedula= input('Ingrese la cédula de identidad: ')
                    cedula= verificar_cedula(cedula, self.socios)
                    fecha_nac= input('Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ')
                    fecha_nac = verificar_fecha_nac(fecha_nac)
                    fecha_ing= input('Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ')
                    fecha_ing = verificar_fecha_ing(fecha_ing, fecha_nac)
                    num_celular= input('Ingrese el número de celular: ')
                    num_celular = verificar_celular(num_celular)
                    tipo= input('Ingrese el tipo de socio: 1- Bonificado 2- No bonificado ')
                    tipo= verificar_tipo_socio(tipo)
                    s= Socio(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, tipo, 0)
                    self.socios.append(s)
                    for socio in self.socios:
                        print (socio.get_nombre)
                        print(socio.get_tipo)
    
                elif opcion == 3:
                    nombre= input('Ingrese el nombre: ')
                    nombre= verificar_nombre(nombre)
                    apellido= input('Ingrese el apellido: ')
                    apellido = verificar_apellido(apellido)
                    cedula= input('Ingrese la cédula de identidad: ')
                    cedula= verificar_cedula(cedula, self.medicos)
                    fecha_nac= input('Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ')
                    fecha_nac= verificar_fecha_nac(fecha_nac)
                    fecha_ing= input('Ingrese la fecha de ingreso a la institucion en formato aaaa-mm-dd: ')
                    fecha_ing= verificar_fecha_ing(fecha_ing, fecha_nac)
                    num_celular= input('Ingrese el número de celular: ')
                    num_celular= verificar_celular(num_celular)
                    especialidad= input('Ingrese la especialidad: ')
                    especialidad= verificar_especialidad_2(self.especialidades, especialidad)
                    m= Medico(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, especialidad)
                    self.medicos.append(m)
                    for medico in self.medicos:
                        print(medico.get_nombre)
                        print(medico.get_especialidad)

                elif opcion == 4:
                    nombre_especialidad= input('Ingrese la especialidad: ')
                    nombre_especialidad= verificar_nombre_especialidad(nombre_especialidad)
                    nombre_especialidad= verificar_especialidad_2(self.especialidades, nombre_especialidad)
                    nombre_medico= input('Ingrese el nombre completo del médico: ')      
                    nombre_medico= verificar_nombre_medico(nombre_medico)                      
                    nombre_medico= verificar_nombre_completo_medico(nombre_medico, self.medicos, self.especialidades)              
                    fecha_consulta= input('Ingrese la fecha de consulta (aaaa-mm-dd): ')
                    fecha_consulta= verificar_fecha_consulta(fecha_consulta)
                    cant_pacientes= input('Ingrese la cantidad de pacientes que se atenderán: ')
                    cant_pacientes=verificar_cantidad_max(cant_pacientes)
                    consulta= ConsultaMedica(nombre_especialidad, nombre_medico, fecha_consulta, cant_pacientes)
                    self.consultas.append(consulta)
                    for consulta in self.consultas:
                        print(consulta.get_nombre_especialidad)
                        print(consulta.get_nombre_medico)

                elif opcion == 5:
                    especialidad= str(input('Ingrese la especialidad: '))
                    especialidad= verificar_nombre_especialidad(especialidad)
                    especialidad= verificar_especialidad_2(self.especialidades, especialidad)
                    a= mostrar_consultas(self.consultas, especialidad)
                    opcion_i= input('Seleccione la opción deseada ')
                    opcion_i=verificar_opcion(a, opcion_i)
                    medico_select, fecha_select=a[int(opcion_i)-1]
                    consulta_sel=elegir_consulta(medico_select,fecha_select, especialidad, self.consultas)
                    print(f'los turnos libres son: {consulta_sel.turnos_libres}')
                    numero= int(input('Seleccionar el número de atención deseado ')) 
                    numero= verificar_numero(numero, consulta_sel.turnos_libres)
                    cedula= int(input('Ingrese la cédula de identidad del socio: '))
                    cedula= verificar_cedula(cedula, self.socios)
                    cedula= verificar_cedula_in_socio(cedula, self.socios)
                    agregar_deuda(cedula, especialidad, self.especialidades, self.socios)
                    consulta_sel.eliminar_numero(numero)

                elif opcion == 6:
                    while True:
                        opcion_6= int(input('Seleccione una opción:\n'
                        '1. Obtener todos los médicos asociados a una especialidad específica.\n'
                        '2. Obtener el precio de una consulta de una especialidad en específico.\n'
                        '3. Listar todos los socios con sus deudas asociadas en orden ascendente.\n'
                        '4. Realizar consultas respecto a cantidad de consultas entre dos fechas\n'
                        '5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.'))
                        if int(opcion_6)==1:
                            especialidad_especifica= input('Especialidad especifica: ')
                            especialidad_especifica= verificar_nombre_especialidad(especialidad_especifica)
                            especialidad_especifica= verificar_especialidad_2(self.especialidades, especialidad_especifica)
                            #si doy de alta una especialidad se termina el programa, va al menu principal, o vuelve a las 5 opciones?
                            for medico in self.medicos:
                                if medico.get_especialidad==especialidad_especifica:
                                    print(medico.get_nombre, medico.get_apellido)
                        elif int(opcion_6)==2:
                            especialidad_especifica= input('Especialidad especifica: ')
                            especialidad_especifica= verificar_nombre_especialidad(especialidad_especifica)
                            especialidad_especifica= verificar_especialidad_2(self.especialidades, especialidad_especifica)
                            for especialidad in self.especialidades:
                                if especialidad.especialidad==especialidad_especifica:
                                    print(especialidad.get_precio)
                        elif int(opcion_6)==3:
                            mostrar_deuda_ordenada(self.socios)
                        elif int(opcion_6)==4:
                            fecha_inicio= input('Fecha inicio: ')
                            fecha_inicio= verificar_fecha(fecha_inicio)
                            fecha_final= input('Fecha_final: ')
                            fecha_final= verificar_fecha(fecha_final)
                            cant_consultas_entre_fechas(fecha_inicio, fecha_final, self.consultas)

                        elif int(opcion_6)==5:
                            fecha_inicio= input('Fecha inicio: ')
                            fecha_ing= verificar_fecha(fecha_inicio)
                            fecha_final= input('Fecha_final: ')
                            fecha_final= verificar_fecha(fecha_final)
                            print(ganancias_entre_fechas(fecha_inicio, fecha_final, self.socios, self.especialidades, self.consultas))
                        break

                elif opcion == 7:
                    break
            else:
                print("La opción seleccionada no es correcta, vuelva a intentar con otra opción. ")

if __name__ == '__main__':
    poli = Policlinica()
    poli.menu()
