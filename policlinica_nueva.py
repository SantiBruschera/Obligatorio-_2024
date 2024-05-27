from socio_dos import Socio
from medico_dos import Medico
from especialidad_dos import Especialidad
from consulta_medica import ConsultaMedica
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

class Policlinica():
    def __init__(self, nombre): #los arrayssiempre tienen que ir como constructores, dentro del init. Tenemos que hacerles getters y setters. Arreglar lo que nos dijo flor de que escribiamos mal los getters y setters. Y hacer lo de socios bonificados y no bonificados. 
        self.__nombre = nombre
        self.medicos = [] #le saque lo oculto para que funcione otra cosa
        self.__socio = [] 
        self.especialidades = []
        self.__consultas = []
    
    @property
    def get_nombre_policlinica(self):
        return self.__nombre
    
    def get_especialidad(self):
        for especialidad in self.especialidades:
            return especialidad.especialidad

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
                    especialidad = input('Especialidad: ')
                    verificar_especialidad(especialidad)
                    precio = input('Precio: ')
                    verificar_precio(precio)
                    e=Especialidad(especialidad, precio)
                    self.especialidades.append(e)
                
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
                    tipo=input('tipo de socio, bonificado(1) o no bonificado(2)')
                    verificar_tipo_socio(tipo)
                    s=Socio(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, tipo)
                    Policlinica.socio.append(s)

                elif opcion == 3:
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
                    verificar_especialidad(especialidad,self.especialidades)
                    m=Medico(nombre, apellido, cedula, fecha_nac, fecha_ing, num_celular, especialidad)
                    Policlinica.medicos.append(m)
                    
                elif opcion == 4:
                    nombre_especialidad=str(input('Ingrese la especialidad'))
                    nombre_medico= str(input('Ingrese el nombre del médico'))
                    fecha_consulta= str(input('Ingrese la fecha de consulta'))
                    cant_pacientes= str(input('Ingrese la cantidad de pacientes que se atenderán'))
                    verificar_nombre_medico(nombre_medico)
                    verificar_nombre_especialidad(nombre_especialidad)
                    #verifico date time y cant pacientes maximlo    
                    verificar_medico(nombre_medico, self.medicos)
                    verificar_especialidad(nombre_especialidad, self.especialidades)            
                    c=ConsultaMedica(nombre_especialidad, nombre_medico, fecha_consulta, cant_pacientes)
                    Policlinica.consultas.append(c)
                    break


                #     pass
                elif opcion == 5:
                    especialidad=str(input('Ingrese la especialidad'))
                elif opcion == 6:#verificar porque no funcionan los getters
                    while opcion not in [1,6]:#definir deudas
                        opcion_6=input('Seleccione una opción:\n'
                        '1. Obtener todos los médicos asociados a una especialidad específica.\n'
                        '2. Obtener el precio de una consulta de una especialidad en específico.\n'
                        '3. Listar todos los socios con sus deudas asociadas en orden ascendente.\n'
                        '4. Realizar consultas respecto a cantidad de consultas entre dos fechas\n'
                        '5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.')
                    if int(opcion_6)==1:
                        especialidad_especifica=input('especialidad especifica')
                        for medico in self.medicos:
                            if medico.get_especialidad==especialidad_especifica:
                                print(medico.get_nombre)
                    elif int(opcion_6)==2:
                        especialidad_especifica=input('especialidad especifica: ')
                        for especialidad in self.especialidades:
                            if especialidad.get_especialidad==especialidad_especifica:
                                print(especialidad.get_precio)
                    elif int(opcion_6)==3:
                        pass
                    elif int(opcion_6)==4:
                        fecha_inicio=input('fecha inicio: ')
                        verificar_fecha(fecha_inicio)
                        fecha_final=input('fecha_final: ')
                        verificar_fecha(fecha_final)
                    elif int(opcion_6)==5:
                        fecha_inicio=input('fecha inicio: ')
                        verificar_fecha(fecha_inicio)
                        fecha_final=input('fecha_final: ')
                        verificar_fecha(fecha_final)




                elif opcion == 7:
                    break
                else:
                    print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")

if __name__ == '__main__':
    poli = Policlinica('hola')
    poli.menu()
