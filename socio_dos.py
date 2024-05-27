from persona_dos import Persona 
class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nac, fecha_ing, celular, tipo):
        self.__tipo=tipo
        self.__deuda=0
        super().__init__(nombre, apellido, cedula, fecha_nac, fecha_ing, celular)
        self.__nombre=nombre
        self.__apellido=apellido
        self.__cedula=cedula
        self.__fecha_nac=fecha_nac
        self.__fecha_ing=fecha_ing
        self.__celular=celular
    
    @property
    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo_nuevo):
        self.__tipo=tipo_nuevo
    
    @property
    def get_deuda(self):
        return self.__deuda
    
    @property
    def get_nombre(self):
        return self.__nombre
