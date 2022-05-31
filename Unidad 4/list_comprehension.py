#List comprehension: Sirve para crear estructuras a partir de otras estructuras.
#Lista: [<dato> <recorrido for> <filtro if>]

#Generar una nueva lista con las frutas que tengan la letra a.
frutas = ['manzana', 'pera', 'kiwi', 'mango', 'melon', 'sandia', 'naranja', 'platano', 'fresa', 'uva', 'papaya', 'limon']
lista = [x for x in frutas if "a" in x]
