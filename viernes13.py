import datetime

def es_viernes_13(mes, ano):
    try:
        # Crear un objeto datetime para el 13 del mes y año dados
        fecha = datetime.datetime(ano, mes, 13)
        # Verificar si el día de la semana es viernes (4 en el formato de 0=lunes a 6=domingo)
        return fecha.weekday() == 4
    except ValueError:
        # Capturar errores si el mes o el año son inválidos
        return False

# Ejemplo de uso
mes = int(input("Ingrese el mes (1-12): "))
ano = int(input("Ingrese el año: "))

if es_viernes_13(mes, ano):
    print(f"El 13 de {mes}/{ano} es un viernes.")
else:
    print(f"El 13 de {mes}/{ano} no es un viernes.")
