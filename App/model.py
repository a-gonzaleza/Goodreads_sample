"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar todos los libros,
    Adicionalmente, crea una lista vacia para los autores, una lista vacia para los 
    generos y una lista vacia para la asociación generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'books':None, 'authors':None, 'tags': None}
    catalog['books'] = lt.newList('ARRAY_LIST')
    catalog['authors'] = lt.newList('ARRAY_LIST')
    catalog['tags'] = lt.newList('ARRAY_LIST')
    catalog['book_tags'] = lt.newList('ARRAY_LIST')

    return catalog


def newAuthor (name):
    """
    Crea una nueva estructura para modelar los libros de un autor y su promedio de ratings
    """
    author = {'name':"", "books":None,  "average_rating":0}
    author ['name'] = name
    author ['books'] = lt.newList('ARRAY_LIST')
    return author


def newTag (name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name':'', 'tag_id':''}
    tag ['name'] = name
    tag ['tag_id'] = id
    return tag

def newBookTag (tag_id, book_id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido 
    marcados con dicho tag.
    """
    booktag = {'tag_id':tag_id, 'book_id':book_id}
    return booktag


# Funciones para agregar informacion al catalogo

def addBookAuthor (catalog, authorname, book, compareauthors):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent (authors, authorname, compareauthors)
    if posauthor > 0:
        author = lt.getElement (authors,posauthor)    
    else:
        author = newAuthor(authorname)
        lt.addLast (authors, author)
    lt.addLast (author['books'], book)
    if (author['average_rating']==0.0):
        author['average_rating']= float (book['average_rating'])
    else:
        author['average_rating'] = (author['average_rating'] + float(book['average_rating']) ) / 2



def addTag (catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag (tag['tag_name'], tag['tag_id'])
    lt.addLast (catalog['tags'], t)



def addBookTag (catalog, booktag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newBookTag (booktag['tag_id'], booktag['goodreads_book_id'])
    lt.addLast (catalog['book_tags'], t)



# Funciones de consulta

def getBooksByAuthor (catalog, authorname, compareauthors):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    posauthor = lt.isPresent (catalog['authors'], authorname, compareauthors)
    if posauthor > 0:
        author = lt.getElement (catalog['authors'], posauthor)
        return author
    return None


