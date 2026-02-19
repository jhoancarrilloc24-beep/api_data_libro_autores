class base_datos_libro:
    def __init__(self):
        self.base_datos_libro = []
        
    def guardar_libro(self, obj_libro):
        self.base_datos_libro.append(obj_libro)
        print("libro guardado 👌", obj_libro.get_tematica())  
        
    def extender_libro(self, nueva_lista):
        self.base_datos_libro.extend(nueva_lista)
        
    def insertar_libro(self, obj_libro, pos_index):
        self.base_datos_libro.insert(pos_index, obj_libro)
        
    def remover_libro(self, obj_libro):
        self.base_datos_libro.remove(obj_libro)
        
    def eliminar_libro(self, pos_index):
        self.base_datos_libro.pop(pos_index)
        
    def buscar_libro(self, nombre_obj):
        return self.base_datos_libro.index(nombre_obj)
        
    def contar_libro(self, valor):
        return self.base_datos_libro.count(valor)
        
    def ordenar_libro(self):
        self.base_datos_libro.sort()
        
    def invertir_libro(self):
        self.base_datos_libro.reverse()

    def mostrar_info(self,base_datos_libro):
        print("mostrar info libro")
        for i in range(len(len(self,base_datos_libro))):
            tematica = self, base_datos_libro[i].get_tematica() 
            fecha = self.base_datos_libro[i].get_fecha()
            print(f"tematica libro:{tematica} - fecha libro {fecha} ✅.")
        
