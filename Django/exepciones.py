try:

    a=int(input("Ingrese un numero"))
    b=int(input("Ingrese otro numero"))
    print(a/b)
    
#Error al dividir por 0    
except ZeroDivisionError as zde:
    print(str(zde),"ingrese un numero que no sea 0")

#Error al no poner un string
except ValueError as ve:
    print(str(ve), "Ingrese solo numeros")

#Error general, evitar porque no sabemos de que tipo de error se trata
except Exception as e:
    print("Ocurrio un error")

#Se ejeuta siempre si hay un error o no casoo que se usa cerrar un archiuvo o salir de una base de dato    
finally:
    pass