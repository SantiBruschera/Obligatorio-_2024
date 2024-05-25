class Especialidad():
    def __init__(self, especialidad, precio):
        self.__especialidad=especialidad
        self.__precio=precio

    @property
    def especialidad(self):
        return self.__especialidad
    
    @property
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio_nuevo):
        self.__precio=precio_nuevo