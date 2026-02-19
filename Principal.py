from Libro_modelo import Libro_modelo
from Autor_modelo import autor_modelo
from libro_bd import base_datos_libro
from api_datos_autores import Api_lista_autores

obj_api_autores = Api_lista_autores()
obj_bd = base_datos_libro()
obj_libro_md = Libro_modelo
obj_autor = autor_modelo

#zona de autores
obj_autor = autor_modelo("lusi martis", "24/07/1009", "estadounidense")
obj_autor1 = autor_modelo("pilatos", "20/02/1001", "griego")
lista_dotos_autor = [obj_autor]
lista_dotos_autor = [obj_autor1]
obj_api_autores.guardar_autores(lista_dotos_autor)

#zona de libros

obj_libro = Libro_modelo("18 de diciembre /", "354 hojas /", "Narnia/", "aventura /")
obj_libro2 = Libro_modelo("30 de octubre /", "400 hojas /", "Harry Potter/", "fantasia /")

#guardar autores en api

obj_api_autores.guardar_autores(obj_autor)
obj_api_autores.guardar_autores (obj_autor1)
nueva_lista = [obj_autor,obj_autor1]

obj_api_autores.inserta_listas(nueva_lista)


#guardar libros

obj_bd.guardar_libro(obj_libro)
obj_bd.guardar_libro(obj_libro2)

#mostrar pocicion de autor pendiente revición 

#----obj_api_autores.mostrar_autores()

#mostrar info del autor 
print()
print("zona info autores 🔶🔷🔸▪️")
obj_autor.ver_info()
obj_autor1.ver_info()
print()

#ver la info del libro 
print("zona libros  🔶🔷🔸▪️")
obj_libro.ver_info_libro()
obj_libro2.ver_info_libro() 