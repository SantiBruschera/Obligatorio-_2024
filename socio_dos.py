from persona_dos import Persona 
class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nac, fecha_ing, celular, tipo, deuda=0):
        self.__tipo=tipo
        self.__deuda=deuda
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
    
    def set_deuda(self, deuda_nueva):
        self.__deuda+=deuda_nueva
    
    @property
    def get_nombre(self):
        return self.__nombre
