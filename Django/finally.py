
try:
    archivo=open("ejemple.txt","w")
    
    print("Prosesando data")
    #supongamos que estamos sacando un reporte
    resultadoparcial=7/0

    print("Resultado ok")
except ZeroDivisionError as zde:
    print("Un dato esta cargado erroneamente como 0, revisar y volver a ejecutar el script")

#Solo se ejecuta solo cuando no hay error,no se suele usar
else:
    print("No ocurrio ningun error")

#Ocurre siempre    
finally:
    print("Liberando recuros")
    archivo.close()
    
#Creando una exepcion
#Se hace mucho cuando tienen errores de negocio
#Se manejan errores con nombre del negocio que esta creando
class RegisteredUserError(Exception):
    pass

