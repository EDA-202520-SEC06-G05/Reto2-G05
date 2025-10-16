import sys
from App import logic as lg

data_structure = None

def new_logic(data_structure):
    """
        Se crea una instancia del controlador
    """
    data = lg.new_logic(data_structure)
    return data 
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    pass

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    taxis, neighborhoods = lg.load_data(control)
    print("\n=== DATOS CARGADOS ===")
    print(taxis,neighborhoods)
    #TODO: Realizar la carga de datos
    pass


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    datetime_initial = input("Ingrese la fecha y hora inicial, con el siguiente formato ()YYYY-MM-DD HH:MM:SS): ")
    datetime_final = input("Ingrese la fecha y hora final, con el siguiente formato ()YYYY-MM-DD HH:MM:SS): ")
    size =int(input("Ingrese el número de datos a visualizar: "))
    result = lg.req_1(control,datetime_initial,datetime_final,size)
    print("\n=== RESULTADO REQ 1 ===")
    print(f"Tiempo de ejecución: {result['load_time']} ms")
    print(f"Total trayectos: {result['trip_total']}")
    print(f"Primeros {size} trayectos: {result['first']}")
    print(f"Ultimos {size} trayectos: {result['last']}")
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    latitude_initial = float(input("Ingrese la latitud inicial: "))
    latitude_final = float(input("Ingrese la latitud final: "))
    size =int(input("Ingrese el número de datos a visualizar: "))
    
    result = lg.req_2(control,latitude_initial,latitude_final,size)
    print("\n=== RESULTADO REQ 1 ===")
    print(f"Tiempo de ejecución: {result['load_time']} ms")
    print(f"Total trayectos: {result['trip_total']}")
    print(f"Primeros {size} trayectos: {result['first']}")
    print(f"Ultimos {size} trayectos: {result['last']}")
    
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    initial_distance = float(input("Ingrese la distancia inicial: "))
    final_distance = float(input("Ingrese la distancia final: "))
    size =int(input("Ingrese el número de datos a visualizar: "))
    result = lg.req_3(control,initial_distance,final_distance,size)
    print("\n=== RESULTADO REQ 3 ===")
    print(f"Tiempo de ejecución: {result['time_total']} ms")
    print(f"Total trayectos: {result['trip_total']}")
    print(f"Primeros {size} trayectos: {result['first']}")
    print(f"Ultimos {size} trayectos: {result['last']}")
    
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    date = input("Ingrese la fecha de terminacion del trayecto, con el siguiente formato (YYYY-MM-DD): ")
    crit = input("Ingrese el momento de interes (ANTES o DESPUES): ")
    time = input("Ingrese la hora de terminacion del trayceto, con el siguiente formato (HH:MM:SS): ")
    size =int(input("Ingrese el número de datos a visualizar: "))
    result = lg.req_4(control,date,crit,time,size)
    print("\n=== RESULTADO REQ 4 ===")
    print(f"Tiempo de ejecución: {result['tiempo_ms']} ms")
    print(f"Total trayectos: {result['total_filtered']}")
    print(f"Primeros {size} trayectos: {result['first5']}")
    print(f"Ultimos {size} trayectos: {result['last5']}")
    
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    object_time = input("Ingrese la fecha y hora de terminacion del trayecto, con el siguiente formato (“%Y-%M-%D %H”)")
    size =int(input("Ingrese el número de datos a visualizar: "))
    result = lg.req_5(control,object_time,size)
    print("\n=== RESULTADO REQ 5 ===")
    print(f"Tiempo de ejecución: {result['time_total']} ms")
    print(f"Total trayectos: {result['trip_total']}")
    print(f"Primeros {size} trayectos: {result['first']}")
    print(f"Ultimos {size} trayectos: {result['last']}")
    
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic(data_structure)

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
