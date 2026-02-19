class Libro_modelo:
    def __init__(self, fecha, cantidad_hojas, tematica, genero):
        self.fecha = fecha
        self.cantidad = cantidad_hojas
        self.tematica = tematica
        self.genero = genero
        
    def get_cantidad_hojas(self):
        return self.cantidad    
        
        #hacer responsabilidades de la clase
        
    def registrar_cantidad_hojas(self):
        mensaje = "se registraron en la base de datos"
        return mensaje
    
    def get_fecha(self):
        return self.fecha

    def registrar_fecha_libro(self):
        mensaje = "las fechas se registraron en la b d"
        return mensaje

    def mostrar_cantidad_hojas(self):
        mensaje = "el libro tiene la siguiente cantidad de: "
        mensaje = mensaje + str(self.get_cantidad_hojas())
        return mensaje

    def get_tematica(self):
        return self.tematica
    
    def registrar_tematica(self):
        mensaje = "tematica registrada"
        return mensaje

    def mostrar_tematica(self):
        mensaje = self.get_tematica()
        return mensaje   

    def info_autor(self, obj_autor):
        return obj_autor.ver_info()     
        
    def ver_info_libro(self):
        print(f"info libro📖. fecha: {self.fecha} cantidad de hojas: {self.cantidad} nombre(tematica): {self.tematica} genero: {self.genero} ✅")