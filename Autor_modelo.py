class autor_modelo:
    def __init__(self, dato_nombre , dato_fecha, dato_nacionalidad):
        self.nombre = dato_nombre
        self.fecha = dato_fecha
        self.nacionalidad = dato_nacionalidad
        
    def registrar_datos(self):
        mensaje = "Se registraron los datos"
        return mensaje
    
    def dato_nombre(self):
        mensaje = "nombre autor"
        return mensaje
    
    def dato_fecha(self):
        mensaje = "Fecha es : " + self.fecha
        return mensaje
         
    def buscar_autor(self, dato_buscar):
        mensaje = "autor existe en la base de datos" + dato_buscar
        return mensaje
    
    def dar_baja_autor(self, dato):
        mensaje = "el autor esta inactivo" + dato
        return mensaje  
    
    def ver_info(self):
        print(f"nombre: {self.nombre} - fecha de obra: {self.fecha} - nacionalidad: {self.nacionalidad} ✅")