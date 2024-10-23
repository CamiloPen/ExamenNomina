from .comprobar import *
from .jsonNomina import empleados

def registrar():
    empleado = {}
    print(" Por favor digite el documento del empleado")
    doc = int(input())
    if not(negativo(doc)):
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
            sal = int(input(" Por favor digite el salario del empleado"))
            if not(negativo(sal)):
                empleado["sal"] = sal
                empleados.append(empleado)

def inasistencias():
    print(" Por favor digite el documento del empleado")
    doc = int(input())
    if not(negativo(doc)):
        empleado = buscar(doc)
        if empleado:
            while True:
                dia = int(input(" Por favor digite el día de la falta (1-30) -> "))
                if dias(dia, empleado):
                    empleado["inas"].append(dia)
                    seguir = input(" Si desea segur agregando inasistencias precione (s) ").lower()
                    if seguir != "s":
                        break

def bonos():
    print(" Por favor digite el documento del empleado")
    doc = int(input())
    if not(negativo(doc)):
        empleado = buscar(doc)
        while True:
            dia = int(input(" Por favor digite el dia -> "))
            if dias(dia, empleado):
                valor = int(input(" Digite el valor del bono -> "))
                if not(negativo(valor)):
                    conc = input(" Escriba el concepto del bono -> ")
                    bono = {
                        "dia": dia,
                        "valor": valor,
                        "conc": conc
                    }
                    empleado["bonos"].append(bono)
                    seguir = input(" Si desea segur agregando bonos precione (s) ").lower()
                    if seguir != "s":
                        break
