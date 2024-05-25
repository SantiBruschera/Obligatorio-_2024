from persona_dos import Persona
class Medico(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nac, fecha_ing, celular, especialidad):
        self.__especialidad=especialidad
        super().__init__(nombre, apellido, cedula, fecha_nac, fecha_ing, celular)
    
    @property 
    def get_especialidad(self):
        return self.__especialidad
# if __name__=='__main__':