from modulos.jsonNomina import *
from modulos.empleados import *

while True:
    try:
        print("BIENVENIDO\n",
            "1.Registrar empleados\n",
            "2.Registrar inasistencias\n",
            "3.Registro bonos\n",
            "4.Generar nomina\n",
            "5.Salir")
        opc = int(input("Digite un número (1-5) según lo que necesite -> "))
        match opc:
            case 1:
                print("REGISTRAR EMPLEADO")
                registrar()
            case 2:
                print("REGISTRAR INASISTENCIAS")
                inasistencias()
            case 3:
                print("REGISTRAR BONOS")
                bonos()
            case 4:
                print("GENERAR NOMINA")
                pago()
                generarNomina()
            case 5:
                break
        guardar()
    except ValueError:
        print("Dato incorrecto")
    except Exception as e:
        print("ERROR: ", e)