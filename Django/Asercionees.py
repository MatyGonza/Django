#Asesrciones
#Forma de hacer validaciones
try:
    a=int(input("Ingrese un numero"))
        
    b=int(input("Ingrese otro numero"))
        
        #Se hace mucho en testing con logica, validamoslo que queremos
    assert b!=0,"El divisor no puede ser 0"
    
except AssertionError as ae:
    print(str(ae))    

