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
    def sestadio(self,nuevo):
        self.__estadio = nuevo

tigres = Equipo("tigres","banote")
tigres.estadio = "azteca"
print(f"equipo :{tigres.nombre} estadio : {tigres.estadio}")
 
