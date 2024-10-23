from .comprobar import *
from .jsonNomina import empleados

def registrar():
    empleado = {}
    print(" Por favor digite el documento del empleado")
    doc = int(input())
    if buscar(doc):
        print(" El empleado ya esta registrado")
    else:
        empleado["doc"] = doc
        print(" Por favor digite el nombre del empleado")
        empleado["nom"] = input()
        print(" Por favor digite el cargo del empleado")
        empleado["car"] = input()
        empleado["inas"] = []
        empleado["bonos"] = []
        print(" Por favor digite el salario del empleado")
        empleado["sal"] = int(input())
        empleados.append(empleado)

def inasistencias():
    print(" Por favor digite el documento del empleado")
    doc = int(input())
    empleado = buscar(doc)
    if empleado:
        while True:
            dia = int(input(" Por favor digite el dia de la falta"))
            empleado["inas"].append(dia)
            seguir = input(" Si desea segur agregando inasistencias precione (s)").lower()
            if seguir != "s":
                break

def bonos():
    print(" Por favor digite el documento del empleado")
    doc = int(input())
    empleado = buscar(doc)
    if empleado:
        while True:
            dia = int(input(" Por favor digite el dia"))
            valor = int(input(" Digite el valor del bono"))
            conc = input(" Escriba el concepto del bono")
            bono = {
                "dia": dia,
                "valor": valor,
                "conc": conc
            }
            empleado["bonos"].append(bono)
            seguir = input(" Si desea segur agregando bonos precione (s)").lower()
            if seguir != "s":
                break