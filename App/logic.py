import time
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp
import csv
import os
import math 
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-2'

def new_logic(data_structure):
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "Neighborhoods": None,
        "taxis_info": None}
    
    catalog["Neighborhoods"] = al.new_list()
    catalog["taxis_info"] = lp.new_map(500000, 0.75,None)
    
    return catalog


def load_data(catalog):
    """
    Carga los datos del reto
    """
    taxi = load_taxis(catalog)
    neigh = load_neigh(catalog)
    return taxi, neigh
    # TODO: Realizar la carga de datos


def load_neigh(catalog):
    neigh_file = data_dir + "/nyc-neighborhoods.csv"
    input_file = csv.DictReader(open(neigh_file, encoding="utf-8"), delimiter=";")
    for neigh in input_file:
        add_neigh(catalog, neigh)
    return neigh_size(catalog)

def load_taxis(catalog):
    
    inicio = get_time()
    trip_total = 0
    min_trip = None
    max_trip = None
    first5 = al.new_list()
    last5 = al.new_list()
    
    
    taxi_file = data_dir + "/taxis-large.csv"
    input_file = csv.DictReader(open(taxi_file, encoding="utf-8"), delimiter=",")
    for taxi in input_file:
        if taxi and "pickup_datetime" in taxi and "dropoff_datetime" in taxi:
            add_taxi(catalog, taxi)
            trip_total += 1
            
            pick_up = taxi["pickup_datetime"]
            dropoff = taxi["dropoff_datetime"]
            start = pick_up[11:16]
            finish = dropoff[11:16]
            
            h1str, m1str = start.split(":")
            h2str, m2str = finish.split(":")
            
            h1, m1 = int(h1str), int(m1str)
            h2, m2 = int(h2str), int(m2str)
            
            duration = (h2 *60 + m2) - (h1 *60 + m1)
            if duration < 0:
                duration += 24*60
        
            distance = float(taxi["trip_distance"])
            cost = float(taxi["total_amount"])
            
            register = {
                "pickup_datetime": pick_up,
                "dropoff_datetime": dropoff,
                "duration_min": duration,
                "distance": distance,
                "cost": cost    
            }
            if al.size(first5) < 5:
                al.add_last(first5, register)

            al.add_last(last5, register)
            if al.size(last5) > 5:
                al.remove_first(last5)

            if distance > 0:
                if min_trip is None or distance < min_trip["distance"]:
                    min_trip = {
                        "pickup_datetime": pick_up,
                        "distance": distance,
                        "cost": cost
                    }

            if max_trip is None or distance > max_trip["distance"]:
                max_trip = {
                    "pickup_datetime": pick_up,
                    "distance": distance,
                    "cost": cost
                }
    final = get_time()       

    return {
        "load_time": final - inicio,
        "total_trips": trip_total,
        "min_trip": min_trip,
        "max_trip": max_trip,
        "first5": first5,
        "last5": last5      
    }
    
def add_neigh(catalog, neigh):
    n = new_neigh(
        neigh["borough"],
        neigh["neighborhood"],
        neigh["latitude"],
        neigh["longitude"]
        )
    al.add_last(catalog["Neighborhoods"], n)
    return catalog

def add_taxi(catalog, taxi):
    taxi_map = catalog["taxis_info"]
    key = taxi_map["size"]+1
    lp.put(taxi_map,key,taxi)
    return catalog

    
def new_neigh(borough, neighbor, lat, longi):
    neigh = {"borough":borough, 
            "neighborhood":neighbor, 
            "latitude":lat, 
            "longitude": longi}   
    return neigh  

def neigh_size(catalog):
    return al.size(catalog["Neighborhoods"])

def taxi_size(catalog):
    part1 = catalog["taxis_info"]
    part2 = part1["size"]
    return part2

def req_1(catalog,fecha_ini,fecha_fin,n):
    """
    Retorna el resultado del requerimiento 1
    (Viajes con pickup_datetime entre dos fechas dadas, ordenados del más antiguo al más reciente)
    """
    start=get_time()
    filtered=al.new_list()
    table= catalog["taxis_info"]["table"]
    fecha_inicial= time.strptime(fecha_ini,"%Y-%m-%d %H:%M:%S")
    fecha_final= time.strptime(fecha_fin,"%Y-%m-%d %H:%M:%S")
    for entry in table["elements"]:
        if entry["value"] is not None:
            taxi= entry["value"]
            if taxi["pickup_datetime"]!= "":
                pickup_date= time.strptime(taxi["pickup_datetime"],"%Y-%m-%d %H:%M:%S")
                if fecha_inicial<= pickup_date<= fecha_final:
                    register= {
                        "pickup_datetime": taxi["pickup_datetime"],
                        "dropoff_datetime": taxi["dropoff_datetime"],
                        "pickup_latitude_longitude": [float(taxi["pickup_latitude"]),float(taxi["pickup_longitude"])],
                        "dropoff_latitude_longitude": [float(taxi["dropoff_latitude"]),float(taxi["dropoff_longitude"])],
                        "distance": float(taxi["trip_distance"]),
                        "total_amount": float(taxi["total_amount"])
                    }
                    al.add_last(filtered, register)
    trip_total= al.size(filtered)
    def sort_crit(a, b):
        fecha_a= time.strptime(a["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        fecha_b= time.strptime(b["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        return fecha_a < fecha_b
    al.shell_sort(filtered, sort_crit)
    if trip_total<=2* n:
        first= filtered["elements"]
        last= []
    else:
        first= filtered["elements"][:n]
        last= filtered["elements"][-n:]
    end= get_time()
    return{
        "load_time": (end - start)*1000,
        "trip_total": trip_total,
        "first": first,
        "last":last
        }
    # TODO: Modificar el requerimiento 1
    


def req_2(catalog, coor_ini, coor_fin, n):
    """
    Retorna el resultado del requerimiento 2
    """
    start = get_time()
    filtered = al.new_list()
    table = catalog["taxis_info"]["table"]    
    for entry in table["elements"]:
        if entry["value"] is not None:
            taxi = entry["value"]
            
            if taxi["pickup_latitude"] != "" and taxi["pickup_longitude"] != "":
                lat = float(taxi["pickup_latitude"])
                lon = float(taxi["pickup_longitude"])
                
                if coor_ini <= lat <= coor_fin:
                    register = {
                        "pickup_datetime": taxi["pickup_datetime"],
                        "dropoff_datetime": taxi["dropoff_datetime"],
                        "pickup_latitude_longitude": [lat,lon],
                        "dropoff_latitude_longitude": [float(taxi["dropoff_latitude"]),float(taxi["dropoff_longitude"])],
                        "distance": float(taxi["trip_distance"]),
                        "total_amount": float(taxi["total_amount"])
                    }
                    al.add_last(filtered, register)
    trip_total = al.size(filtered)
    
    def sort_crit(a,b):
        if a["pickup_latitude_longitude"][0] > b["pickup_latitude_longitude"][0]:
            return True
        elif a["pickup_latitude_longitude"][0] == b["pickup_latitude_longitude"][0]:
            return a["pickup_latitude_longitude"][1] > b ["pickup_latitude_longitude"][1]
        else:
            return False
    al.shell_sort(filtered, sort_crit)
    
    if trip_total <= 2*n:
        first = filtered["elements"]
        last = []
    else:
        first = filtered["elements"][:n]
        last = filtered["elements"][-n:]
    
    end = get_time()
    
    return {
        "load_time": end - start,
        "trip_total": trip_total,
        "first": first,
        "last": last
    }    
    # TODO: Modificar el requerimiento 2



def req_3(catalog, initial_distance, final_distance, n):
    """
    Retorna el resultado del requerimiento 3
    """
    if n <= 0:
        return {
        "time_total": 0, 
        "trip_total" : 0,
        "first" : al.new_list(),
        "last" : al.new_list()
    }
    
    start = get_time()
    result =  {
        "time_total": 0, 
        "trip_total" : 0,
        "first" : al.new_list(),
        "last" : al.new_list()
    }
    
    table = catalog["taxis_info"]["table"]
    filtred = al.new_list()
    for i in table["elements"]:
        if i["value"] is not None :
            single = i["value"]
            distance = float(single["trip_distance"])
            if initial_distance <= distance <= final_distance:
                result["trip_total"] += 1
                each = {
                    "pickup_datetime": single["pickup_datetime"],
                    "pickup_latitude_longitude": [single["pickup_latitude"],single["pickup_longitude"]],
                    "dropoff_datetime": single["dropoff_datetime"],
                    "dropoff_latitude_longitude":  [single["dropoff_latitude"],single["dropoff_longitude"]],
                    "trip_distance": float(single["trip_distance"]),
                    "total_amount": float(single["total_amount"])                
                }  
                al.add_last(filtred,each)
            
    def sort_crit(a,b):
        centinela = False
        if a["trip_distance"] > b["trip_distance"]:
            centinela = True 
        elif a["trip_distance"] == b["trip_distance"]:
            if a["total_amount"] > b["total_amount"]:
                centinela = True
                
        return centinela 
    
    al.merge_sort(filtred, sort_crit)
    
    if al.size(filtred) == 0:
        end = get_time()
        result["time_total"] = delta_time(start,end)
        return result
    
    elif al.size(filtred) <=2*n:
        result["first"] = filtred
        end = get_time()
        result["time_total"] = delta_time(start,end)
        
    else:
        result["first"] = al.sub_list(filtred,0,n)
        result["last"] = al.sub_list(filtred,al.size(filtred)-n ,n)
        end = get_time()
        result["time_total"] = delta_time(start,end)
    
    return result

    # TODO: Modificar el requerimiento 3


def req_4(catalog, obj_date, interest_m, ref_time, n):
    """
    Retorna el resultado del requerimiento 4
    """
    start = get_time()

    taxis_map = catalog["taxis_info"]
    dropoff_map = lp.new_map(500000, 0.75, None)


    for i in range(taxis_map["capacity"]):
        par = al.get_element(taxis_map["table"], i)
        if par["key"] is not None:
            taxi = par["value"]
            fecha = taxi["dropoff_datetime"][:10]

            lista = lp.get(dropoff_map, fecha)
            if lista is None:
                lista = al.new_list()
                lp.put(dropoff_map, fecha, lista)

            al.add_last(lista, taxi)

    viajes_dia = lp.get(dropoff_map, obj_date)
    if viajes_dia is None:
        end = get_time()
        return {
            "tiempo_ms": delta_time(start, end),
            "total": 0,
            "primeros": None,
            "ultimos": None
        }

    ref_h, ref_m, ref_s = ref_time.split(":")
    ref_seg = int(ref_h)*3600 + int(ref_m)*60 + int(ref_s)
    
    filtrados = al.new_list()

    for i in range(al.size(viajes_dia)):
        viaje = al.get_element(viajes_dia, i)
        hora = viaje["dropoff_datetime"][11:19]
        h, m, s = hora.split(":")
        seg = int(h)*3600 + int(m)*60 + int(s)
        del viaje["vendor"], viaje["passenger_count"], viaje["rate_code"], viaje["payment_type"], viaje["fare_amount"], viaje["extra"], viaje["mta_tax"], viaje["tip_amount"], viaje["tolls_amount"], viaje["improvement_surcharge"]
        viaje["pickup_latitude_longitude"] = [viaje["pickup_latitude"], viaje["pickup_longitude"]]
        viaje["dropoff_latitude_longitude"] = [viaje["dropoff_latitude"], viaje["dropoff_longitude"]]
        del viaje["pickup_latitude"], viaje["pickup_longitude"], viaje["dropoff_latitude"], viaje["dropoff_longitude"]

        if interest_m == "ANTES" and seg < ref_seg:
            al.add_last(filtrados, viaje)
        elif interest_m == "DESPUES" and seg > ref_seg:
            al.add_last(filtrados, viaje)

    total = al.size(filtrados)


    def ordenar_desc(v1, v2):
        return v1["dropoff_datetime"] > v2["dropoff_datetime"]

    filtered = al.merge_sort(filtrados, ordenar_desc)



    if al.size(filtered) <= 2*n:
        show_final = filtered
        return {
        "tiempo_ms": end - start,
        "total_filtered": total,
        "all": show_final
    }
    
    first = al.sub_list(filtered, 0, n)
    last = al.sub_list(filtered, al.size(filtered)-n, n)
    
    end = get_time()
    return {
        "tiempo_ms": end - start,
        "total_filtered": total,
        "first5": first,
        "last5": last
    }  

def req_5(catalog, object_time, n):     
    
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    result = {
        "time_total": 0,
        "trip_total": 0,
        "first": al.new_list(),
        "last": al.new_list()
    }
    
    table = catalog["taxis_info"]["table"]
    map_new = lp.new_map(500000, 0.75,None)
    lp.put(map_new, object_time, al.new_list())
    for i in table["elements"]:
        if i["value"] is not None:
            single = i["value"]
            format_date = single["dropoff_datetime"][:10] + " " + single["dropoff_datetime"][11:13]
            if format_date == object_time:
                single = {
                    "pickup_datetime": single["pickup_datetime"],
                    "pickup_latitude_longitude": [single["pickup_latitude"],single["pickup_longitude"]],
                    "dropoff_datetime": single["dropoff_datetime"],
                    "dropoff_latitude_longitude":  [single["dropoff_latitude"],single["dropoff_longitude"]],
                    "trip_distance": float(single["trip_distance"]),
                    "total_amount": float(single["total_amount"])                
                } 
                array_map = lp.get(map_new,object_time)
                al.add_last(array_map, single)
                
    array = lp.get(map_new,object_time)
    def sort_crit(a,b):
        centinela = False
        if a["dropoff_datetime"] > b["dropoff_datetime"]:
            centinela = True 
                
        return centinela
    al.merge_sort(array,sort_crit)
    
    if al.size(array) == 0:
        end_time = get_time()
        result["time_total"] = delta_time(start_time,end_time)
        result["trip_total"] = 0
        return result
    elif al.size(array) <= 2*n:
        result["first"] = array
        end_time = get_time()
        result["time_total"] = delta_time(start_time,end_time)
        result["trip_total"] = al.size(array)
    else:
        result["first"] = al.sub_list(array,0,n)
        result["last"] = al.sub_list(array,al.size(array)-n,n)
        end_time = get_time()
        result["time_total"] = delta_time(start_time,end_time)
        result["trip_total"] = al.size(array)
        
    return result
    
    
    # TODO: Modificar el requerimiento 5
    

def harvesine_miles(lat1, lon1, lat2, lon2):
    R = 3958.8
    lat1 = lat1 * math.pi / 180
    lon1 = lon1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    lon2 = lon2 * math.pi / 180
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2) **2)
    c = 2 * math.asin(math.sqrt(a))
    return R * c


def req_6(catalog, neigh, ini_hour, fin_hour, n):
    """
    Retorna el resultado del requerimiento 6
    """
    
    start = get_time()
    pickup_map = lp.new_map(500000, 0.75, None)
    neighs = catalog["Neighborhoods"]
    taxis = catalog["taxis_info"]
    
    for i in range(taxis["capacity"]):
        pair = al.get_element(taxis["table"], i)
        if pair["key"] is not None:
            taxi = pair["value"]
            lat = float(taxi["pickup_latitude"])
            lon = float(taxi["pickup_longitude"])
            
            near_neigh = None
            min_dist = 0.5
            for j in range(al.size(neighs)):
                neigh_element = al.get_element(neighs, j)
                latitude = neigh_element["latitude"].replace(",", ".")
                latitude = float(latitude)
                longitude = neigh_element["longitude"].replace(",", ".")
                longitude = float(longitude)
                dist = harvesine_miles(latitude,longitude, lat, lon)
                if dist < min_dist:
                    near_neigh = neigh_element["neighborhood"]
                    min_dist = dist
            
            if near_neigh is not None:
                list = lp.get(pickup_map, near_neigh)
                if list is None:
                    list = al.new_list()
                    lp.put(pickup_map, near_neigh, list)
                al.add_last(list, taxi)
    
    trip_neigh = lp.get(pickup_map, neigh)
    filtered = al.new_list()
    
    if trip_neigh is not None:
        for i in range(al.size(trip_neigh)):
            trip = al.get_element(trip_neigh, i)
            hour = int(trip["pickup_datetime"][11:13])
            if int(ini_hour) <= hour <= int(fin_hour):
                del trip["vendor"], trip["passenger_count"], trip["rate_code"], trip["payment_type"], trip["fare_amount"], trip["extra"], trip["mta_tax"], trip["tip_amount"], trip["tolls_amount"], trip["improvement_surcharge"]
                trip["pickup_latitude_longitude"] = [trip["pickup_latitude"], trip["pickup_longitude"]]
                trip["dropoff_latitude_longitude"] = [trip["dropoff_latitude"], trip["dropoff_longitude"]]
                del trip["pickup_latitude"], trip["pickup_longitude"], trip["dropoff_latitude"], trip["dropoff_longitude"]
                al.add_last(filtered, trip)
    total = al.size(filtered)
    
    def sort_crit(a,b):
        return a["pickup_datetime"] < b["pickup_datetime"]
    
    filtered = al.merge_sort(filtered, sort_crit) 
    
    end = get_time()
    if al.size(filtered) <= 2*n:
        show_final = filtered
        return {
        "tiempo_ms": end - start,
        "total_filtered": total,
        "all": show_final
    }
    
    first = al.sub_list(filtered, 0, n)
    last = al.sub_list(filtered, al.size(filtered)-n, n)
    
    end = get_time()
    return {
        "tiempo_ms": end - start,
        "total_filtered": total,
        "first5": first,
        "last5":last
        }
    # TODO: Modificar el requerimiento 6
    pass


def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
