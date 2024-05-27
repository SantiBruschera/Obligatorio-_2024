from medico_dos import Medico
from socio_dos import Socio

class ConsultaMedica():
    def __init__(self, nombre_especialidad, nombre_medico, fecha_consulta, cant_pacientes):
        self.__nombre_medico = nombre_medico
        self.__nombre_especialidad = nombre_especialidad
        self.__fecha_consulta= fecha_consulta
        self.__cant_pacientes = cant_pacientes

    @property
    def get_nombre_medico(self):
        return self.__nombre_medico
    
    @property
    def get_nombre_especialidad(self):
        return self.__nombre_especialidad
    
    @property
    def get_fecha_consuulta(self):
        return self.__fecha_consulta
    
    @property
    def get_cant_pacientes(self):
        return self.__cant_pacientes
    
    def set_fecha_consulta(self, fecha_consulta_nueva):
        self.__fecha_consulta=fecha_consulta_nueva

    def set_cant_pacientes(self, cant_pacientes_nueva):
        self.__cant_pacientes=cant_pacientes_nueva

        #busco medico por el nombre, recorro la lista y veo si aparece el nombre del medico
        #erorr, qu eno este el medico ingresado 


#recolecto los datos, una vez que este todo ok, lo agrego sumo al cantidad de pacientes 
# lista especiales. nombre == especialidad

#chequear que haya capaciad
    