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
import model 
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def loadCSVFile (file, lst):
    input_file = csv.DictReader(open(file))
    for row in input_file:  
        lt.addLast(lst,row)


def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)



def compareauthors (authorname1, author):
    return  (authorname1.lower() in author['name'].lower())


def compareratings (book1, book2):
    return ( float(book1['average_rating']) > float(book2['average_rating']))


def comparetagids (id, tag):
    return (id  == tag['tag_id'])



def comparegoodreadsid (id, book):
    return (id  == book['goodreads_book_id'])



def comparetagnames (name, tag):
    return (name  == tag['name'])


# Funciones para la carga de datos 

def loadBooks (catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    t1_start = process_time() #tiempo inicial
    booksfile = cf.data_dir + 'GoodReads/books.csv'
    input_file = csv.DictReader(open(booksfile))
    for book in input_file:  
        # Se adiciona el libro a la lista de libros
        lt.addLast(catalog['books'],book)
        # Se obtienen los autores del libro
        authors = book['authors'].split(",")
        # Cada autor, se crea en la lista de libros del catalogo, y se 
        # crea un libro en la lista de dicho autor (apuntador al libro)
        for author in authors:
            model.addBookAuthor (catalog, author.strip(), book, compareauthors)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga libros",t1_stop-t1_start," segundos")



def loadTags(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    t1_start = process_time() #tiempo inicial
    tagsfile = cf.data_dir + 'GoodReads/tags.csv'
    input_file = csv.DictReader(open(tagsfile))
    for tag in input_file:  
        model.addTag (catalog, tag)
    t1_stop = process_time() #tiempo inicial
    print("Tiempo de ejecución carga tags",t1_stop-t1_start," segundos")

    


def loadBooksTags (catalog):
    """
    Carga la información que asocia tags con libros. 
    Primero se localiza el tag y se le agrega la información leida. 
    Adicionalmente se le agrega una referencia al libro procesado.
    """
    t1_start = process_time() #tiempo inicial
    booktagsfile = cf.data_dir + 'GoodReads/book_tags.csv'
    input_file = csv.DictReader(open(booktagsfile))
    for booktag in input_file: 
        model.addBookTag (catalog, booktag)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga book tags",t1_stop-t1_start," segundos")

def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog



def loadData (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadBooks(catalog)
    sort.sort(catalog['books'],compareratings)
    loadTags(catalog)
    loadBooksTags(catalog)


# Funciones llamadas desde la vista y enviadas al modelo

def getBooksByAuthor (catalog, authorname):
    author = model.getBooksByAuthor (catalog, authorname, compareauthors)
    return author


def getBestBooks (catalog, number):
    books = catalog['books']
    bestbooks = lt.newList()
    for cont in range (1, number+1):
        book = lt.getElement (books, cont)
        lt.addLast (bestbooks, book)
    return bestbooks
    

def countBooksByTag (catalog, tag):
    t1_start = process_time() #tiempo inicial
    tags = catalog['tags']
    bookcount=0
    pos = lt.isPresent (tags, tag, comparetagnames)
    if pos>0:
        tag_element = lt.getElement (tags, pos)
        if tag_element != None:
            iterator = it.newIterator(catalog['book_tags'])
            while  it.hasNext(iterator):
                book_tag = it.next(iterator)
                if tag_element['tag_id']==book_tag['tag_id']:
                    bookcount+=1
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución conteo libros por género",t1_stop-t1_start," segundos")
    return bookcount 
