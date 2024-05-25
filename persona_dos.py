from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, apellido, cedula, fecha_nac, fecha_ing, celular):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = fecha_nac
        self.__fecha_ingreso = fecha_ing
        self.__numero_celular = celular

    @property
    def get_nombre(self):
        return self.__nombre
    
    @property
    def get_apellido(self):
        return self.__apellido
    
    @property
    def get_cedula(self):
        return self.__cedula
    
    @property
    def get_fecha_nac(self):
        return self.__fecha_nacimiento
    
    @property
    def get_fecha_ing(self):
        return self.__fecha_ingreso
    
    @property
    def get_celular(self):
        return self.__numero_celular
