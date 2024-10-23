from .jsonNomina import empleados

def buscar(doc):
    i = 0
    while i < len(empleados):
        empleado = empleados[i]
        if empleado["doc"] == doc:
            return empleado
        i += 1
    



def pago():
    for empleado in empleados:
        salario = empleado["sal"] - (empleado["sal"] * 0.08)
        inas = len(empleado["inas"])
        if empleado["sal"] < 2000000:
            auxilio = empleado["sal"]* 0.1
        else:
            auxilio = 0
        if inas > 0:
            descuento = (empleado["sal"]/30)*inas
        else:
            descuento = 0
        bonos = 0
        for bono in empleado["bonos"]:
            bonos += bono["valor"]
        total = salario - descuento + bonos + auxilio
        empleado["total"] = total