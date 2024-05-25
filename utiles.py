from datetime import datetime
def verificar_especialidad(especialidad, especialidades):
    while especialidad not in especialidades:
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
                especialidad = input('Especialidad: ')
            elif opcion == 2:
                precio = input('Precio: ')
                while not precio.isdigit():
                    print('El precio debe ser un número.')
                    precio = input('Precio: ')
                dar_alta_especialidad(especialidad, precio)
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    especialidad = especialidad



def es_fecha_valida(fecha_str):#utiliza datetime para fijarse que sea una fecha valida
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

def verificar_nombre(nombre):#cambie el verificar datos, a una funcion por dato para que la correccion sea inmediata
    nombre = nombre#para que no te deje ingresar el sigueinte dato hasta que el anterior este correcto
    while not nombre.isalpha():
        print("No es un nombre válido, ingréselo de nuevo.")
        nombre = input("Ingrese el nombre: ")

def verificar_apellido(apellido):
    apellido = apellido
    while not apellido.isalpha():
        print("No es un apellido válido, ingréselo de nuevo.")
        apellido = input("Ingrese el apellido: ")

def verificar_cedula(cedula):
    cedula = cedula
    while not str(cedula).isdigit() or len(str(cedula)) != 8:
        print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
        cedula = input("Ingrese la cédula de identidad (8 dígitos): ")

def verificar_fecha_nac(fecha_nac):
    fecha_nacimiento = fecha_nac
    while not es_fecha_valida(fecha_nacimiento):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")

def verificar_fecha_ing(fecha_ing):
    fecha_ingreso = fecha_ing
    while not es_fecha_valida(fecha_ingreso):
        print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
        fecha_ingreso = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
    
def verificar_celular(celular):
    celular = celular
    while not celular.isdigit() or len(str(celular)) != 9 or not str(celular).startswith('09'):
        print("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX.")
        celular = input("Ingrese el número de celular (9 dígitos): ")

def es_fecha_valida(fecha_str):#utiliza datetime para fijarse que sea una fecha valida
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False 

def verificar_tipo_socio(tipo):#porque no funciona de entrada?
        while int(tipo) != 1 and int(tipo) != 2:
            print('El valor ingresado no es correcto, elige la opción 1 o 2.')
            tipo=int(input('tipo de socio: '))

def dar_alta_especialidad(especialidad, precio):
        while True:
            if not especialidad.isalpha():
                print("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                especialidad = input("Especialidad: ")
            elif not precio.isdigit():
                print("El precio de la especialidad es incorrecto, ingréselo nuevamente")
                precio = input("Precio: ")
            else:
                especialidad = especialidad
                precio = precio
                break

def verificar_datos_consulta(nombre_especialidad,arrayespecialidad, nombre_medico, arraymedico):
    while True:
        nombre_medico = input("Ingrese la especialidad: ")
        while not nombre_medico.isalpha():
            print("El médico debe ser un string")

        nombre_especialidad = input("Ingrese la especialidad: ")
        while not nombre_especialidad.isalpha():
            print("La especialidad debe ser un string")
            
        especialidad_existe = False
        for especialidad in arrayespecialidad:
            if arrayespecialidad[especialidad]== nombre_especialidad:
                especialidad_existe = True
                break 
        
        medico_existe = False
        for medico in arraymedico:
            if arraymedico[medico] == nombre_medico:
                medico_existe = True
                break
        
        while True:
            if especialidad_existe == False: 
                opcion = input('Esta especialidad no está dada de alta elija una opción: \n'
                        '1 - Volver a ingresar la especialidad \n'
                        ' 2 - Dar de alta esta especialidad')
                
                if opcion == '1':
                    nombre_especialidad = input('Volver a ingresar especialidad')
                    continue
                elif opcion == '2':
                    #ir a la parte de flujo de dar alta especialidad,no se como hacerlo 
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 1 o 2.")
                    continue

            if medico_existe == False:
                opcion = input('Este médico no está dado de alta, elija una opción: \n'
                        '1 - Volver a ingresar el médico \n'
                        ' 2 - Dar de alta el médic')  
                
                if opcion == '1':
                    nombre_medico = input('Volver a ingresar especialidad')
                    continue
                elif opcion == '2':
                    #ir a la parte de flujo de dar alta medico,no se como hacerlo 
                    break
                else:
                    print("Opción no válida. Por favor, seleccione 1 o 2.")
                    continue                              
                
            

                
                arrayespecialidad.append(nombre_especialidad)    
        

                
        
        
        # if especialidad_exiiste:
        #     print("")
        #     else:
        #         return especialidad_existe #print('Esta especialidad no fue dada de alta elija una opción: ')
            #1- Volver a ingresar el médico
            #2- Dar de ala el médico 
        
    

    




    # Vemos si existe la especialidad, si coincide con las dadas
    
        
        
    #     especialidad_existe = False
    #     for especialidad in self.especialidades:
    #        if self.especialidades[especialidad].get_especialidad == nombre_especialidad:
    #            especialidad_existe = True
    #    if especialidad_existe == False:
    #        print("ERROR: la especialidad no existe")