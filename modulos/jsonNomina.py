import json
from csv import DictWriter

nombre = "archivo/empleados.json"

def openFile():
    data = []
    try:
        file = open(nombre)
        data = json.load(file)
        return data
    except ValueError:            
        return data                
    except FileNotFoundError:     
        return data
    except Exception as e:
        print(" ALGO PASÓ -- ERROR: ", e)
    file.close()         

empleados = openFile()

def guardar():
    file = open(nombre, "w") 
    new = json.dumps(empleados, indent=2)    
    file.write(new)                     
    file.close()
    
def generarNomina():
    for empleado in empleados:
        file = f"nomina/{empleado["doc"]}.csv"
        headers = ["DOCUMENTO", "NOMBRE", "CARGO", 
                   "SALARIO-BASE", "DESCUENTO-SALUD", 
                   "DESCUENTO-PENSION", "INASISTENCIAS", 
                   "BONOS", "TOTAL"]
        with open(file,"w", newline='') as f2:                                                    
            writer = DictWriter(f2,  fieldnames = headers )                                            
            if headers:                                                                               
                writer.writeheader()                                                                                                                   
                writer.writerow({
                    "DOCUMENTO": empleado["doc"], 
                    "NOMBRE": empleado["nom"], 
                    "CARGO": empleado["car"], 
                    "SALARIO-BASE": empleado["sal"], 
                    "DESCUENTO-SALUD": empleado["sal"]*0.04,
                    "DESCUENTO-PENSION": empleado["sal"]*0.04,
                    "INASISTENCIAS": len(empleado["inas"]), 
                    "BONOS": empleado["bonos"], 
                    "TOTAL": empleado["total"]
                })                                                                  
            f2.close()     
