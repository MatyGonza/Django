'''
HERENCIA
'''
from abc import ABC,abstractmethod

#Maquetas o plantillas
class Empleado(ABC):
    def __init__(self,nombre,apellido):
        #__Atributo privado
        #name mangling manipula en nombre de las variables
        self.__nombre = nombre
        self.__apellido = apellido
    #Como es la igualdad entre 2 instancias
    def __eq__(self, other):
        pass
    @property #getter nombre completo
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property #defino nombre como publico #getter nombre
    def nombre(self):
        return self.__nombre
    
    @property #getter apellido
    def apellido(self):
        return self.__apellido
    
    @property #getter salarios
    @abstractmethod
    def salario(self):
        pass
    

    #defino el seter a nombre para modificar el nombre
    
    #@nombre.setter
    #def nombre(self,nombre):
     #   self.__nombre=nombre
        
        
    #GETTER
    #def get_nombre(self):
     #   return self.__nombre
    #SETTER
    #def set_nombre(self,nombre):
     #   self.__nombre=nombre
     
class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido,salario):
        super().__init__(nombre, apellido)
        self.__salario=salario

    @property
    def salario(self):
        return self.__salario

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido,horas_mes,precio_hora):
        super().__init__(nombre, apellido)
        self.__horas_mes=horas_mes
        self.__precio_hora=precio_hora
    @property
    def salario(self):
        return self.__horas_mes * self.__precio_hora

#Herencia multiple

class Estudiante:
    def __init__(self, legajo):
        self.__legajo = legajo
        
        
    @property
    def legajo(self):
        return self.__legajo
    
class EstudiantePasante(Empleado, Estudiante):
    def __init__(self, nombre, apellido,legajo):
        Empleado.__init__(self,nombre,apellido)
        Estudiante.__init__(self,legajo)
        
    @property
    def salario(self):
        return 0
    
    
#Creando el objeto
#Instanciando la clase Empleado para crear un objeto                
#e1=Empleado("Carlos","Lopez")
#e2=Empleado("Maria","Del cerro")

#Name mangling para ver los atributos privados
#print(e1._Empleado__nombre,e1._Empleado__apellido)

#llamado al metodo como funcion
#print(e1.nombre_completo())

#llamdo metodo como atributo usando property
#print(e1.nombre_completo)

#GETTER Y SETTER
#print(e1.get_nombre())
#print(e1.set_nombre("Benja"))


eft1=EmpleadoFullTime("Martin","Gomez",1000)
print(eft1.nombre_completo)
print(eft1.salario)

epxh1=EmpleadoPorHora("Martin","Gonzalez",2,500)
print(epxh1.nombre_completo)
print(epxh1.salario)


ep1=EstudiantePasante("Gaston","Perez",10001)
print(ep1.salario)