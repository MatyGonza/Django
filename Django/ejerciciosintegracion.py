#1. Escribir una función que calcule el máximo común divisor entre dos números
def mcd(a,b):
    while b:
        a, b = b, a % b
        
        # Misma solucion usando un auxiliar
        # aux=a
        # a=b
        # b=aux % b
    return abs(a)

#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def mcm(a,b):
    return (a*b) / mcd(a,b)

#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def frecuencia(cadena):
    palabras=cadena.split(" ")
    
    resultado={}
    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] +=1
        else:
            resultado[palabra]=1
    return resultado


"""
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia.
"""
def max_frecuencia(palabras):
            #Tupla
    maximo=("",0)
    
    dicc_palabras=frecuencia(palabras)
    
    for palabra,frec in dicc_palabras.items():
        if frec > maximo[1]:
                    #Tupla
            maximo = palabra,frec
    return maximo
    
"""
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva
"""
def get_int():
    
    while True:
        try:
            valor=int(input("Ingrese un numero"))
            break
        except ValueError as ve:
            print("Dato invalido solo se aceptan numeros entero")
        
    return valor

"""
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""
class Persona:
    ADULTEZ=18
    #Funcion con parametro por defectos
                #Al tener parametros x defectos inicializados, es opcional
   # def __init__(self,nombre="",edad=0,dni=0):
    #    pass

    def __init__(self,nombre,edad,DNI):
        self.__nombre=nombre#PRIVADOS
        self.__edad=edad
        self.__DNI=DNI

    @property#GETTER
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor
    
    
    @property#GETTER
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,valor):
        #Validacion
        if valor <0:
            #Raise Crea Una exepcion
            raise ValueError("Edad no puede ser negativa")
        #si no es entero
        if  type(valor) is not int:
            raise TypeError("La edad debe ser un numero entero")
        self.edad=valor
    
     
    @property#GETTER
    def DNI(self):
        return self.__DNI
    
    @DNI.setter
    def DNI(self,valor):
        self.DNI=valor

    def mostrar(self):
        return f"{self.__nombre} {self.__edad} DNI: {self.__DNI}"
    
    def es_mayor_de_edad(self):
        return self.__edad >= Persona.ADULTEZ
    
    def __str__(self):
        return self.mostrar    

    def __repr__(self):
        return self.mostrar    
       
#--------------------------------------------------------------------
#Test
#Ejercicio1
#print(mcd(8,4))
#Prueba rapida
assert mcd(8,4) ==4,"Error"
assert mcd(4,8) ==4,"Error"
assert mcd(-15,-5) ==5,"Error"
#Coprimos
assert mcd(13,8) ==1,"Error"

#Ejercicio2
assert mcm(8,4) ==8,"Error"
assert mcm(4,8) ==8,"Error"
#assert mcm(13,8) ==60,"Error"

#Ejercicio3
assert frecuencia("hola")=={'hola': 1},"Error"
assert frecuencia("hola hola hola")=={'hola': 3},"Error"
assert frecuencia("hola como estas mi nombre es luciano")=={'hola': 1, 'como': 1, 'estas': 1, 'mi': 1, 'nombre': 1, 'es': 1, 'luciano': 1},"Error"
assert frecuencia("si si si no no no no")=={'si': 3, 'no': 4},"Error"

#Ejercicio4
assert max_frecuencia("a a a b b c")==('a', 3),"Error"
assert max_frecuencia("a b c")==('a', 1),"Error"
assert max_frecuencia("c b a")==('c', 1),"Error"

#Ejercicio5
#Como esta funcion implica entrada de usuario por consola la voy a omitir
#get_int()

#Ejercicio6
p1=Persona("Carlos Lopez",25,1234) 
print("Todos bien")
