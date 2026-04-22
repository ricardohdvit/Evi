#metodos magicos 
class Equipo :
    liga = "liga mx"
    directivo = "arreola"
    total_equipos = 0 

    def __init__(self,nombre,estadio):
        self.__nombre = nombre
        self.__estadio = estadio
        Equipo.total_equipos +=  1

    def reset (self,valor):
        self.estadio = valor
        self.nombre = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre = nuevo
    
    @property
    def estadio(self):
        return self.__estadio
    
    
    @estadio.setter
    def estadio(self,nuevo):
        self.__estadio = nuevo
#como nuevo cls es la clase y el como genral tu propio equipo

    @classmethod
    def crear_equipo(cls,nom,estadio):
        return cls(nom,estadio)
    
#para imprimir el total de equipos 
   
    @classmethod
    def imprimir_total(cls):
        print(f"total de equipos {cls.total_equipos}")

#para imprimir como encabezado
    @classmethod
    def imprimir_encabezado(cls):
        print(f"sistema para control de liga")
        print(f"liga {cls.liga}")
        print(f"directivo {cls.directivo}")
        print(f"total de equipos {cls.total_equipos}")

#__repr es una metodo utilizado para representar en cadena nuentro objeto para depurar
#y debe ser pensado en el desarrollador

    def __repr__(self):
        return f"equipo(nombre = {self.__nombre},estadio ={self.__estadio})"

    def __str__(self):
        return f"equipo {self.__nombre},estadio:{self.__estadio}"

    def __eq__(self, valor):
        return self.__nombre == valor
#se borro el menu y se puso una lista para colocar 100 equipos 
lista_equipo = []
lista_equipo.append(Equipo.crear_equipo("tigres","volcan"))
lista_equipo.append(Equipo.crear_equipo("queretaro","sepa"))


#con los metodos eq 
print(lista_equipo)
lista_equipo.remove("tigres")
print(lista_equipo)


