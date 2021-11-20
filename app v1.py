#Nombre de la aplicación: OP helper
#Creado por Pablo Calvo Espinar

#Descripción:Esta aplicación busca automatizar tareas administrativas cotidianas de un empresario promedio, posee las siguientes funcionalidades:
#por un lado tiene un apartado que permite acceder y modificar de forma simplificada una base de datos de empleados pudiendo modificarlo,

#conexion base de datos
import mysql.connector
cnn=mysql.connector.connect(host="localhost",user="root",
passwd="",database="app1")
#print(cnn)

import calendar 

#otras librerias
from time import sleep       #libreria standar de python


print("Bienvenido a Secretario OP")

def directorio():
    print("Opciones:")
    sleep(1.5)  #sirve para crear un tiempo entre uno y otro, asi se lee mejor
    print("Para acceder al listado de empleados y sueldos escriba: 1")
    sleep(2)
    print("Para acceder al listado de productos escriba: 2")
    sleep(2)
    print("Para acceder a sus notas escriba: 3")
    sleep(2)
    eleccion=int(input("A dónde quieres acceder?"))
    if eleccion>3 or eleccion<1:
        print("Número invalido")  
    if eleccion==1:   #funcion empleados
        lista_empleados()
    if eleccion==2:   #funcion productos
        lista_productos()    
    if eleccion==3:   #funcion notas
        notas()

def lista_empleados():
    print("Se encuentra en la lista de empleados")
    sleep(2)
    print("Para introducir un empleado nuevo escriba:1")
    sleep(2)
    print("Para borrar a un empleado de la lista escriba:2")
    sleep(2)
    print("Para ver la lista escriba:3")
    sleep(2)
    print("Para volver al menu principal escriba:4")
    sleep(2)
    print("-----------------------------------------------------")
    eleccion1=int(input("A donde desea acceder?"))
    if eleccion1==1:   #añadir datos
        print("Ha accedido al registro de empleados")
        sleep(1)
        cursor1=cnn.cursor()    #crea un cursor para mysql
        sql="insert into empleados (nombre, apellido, sueldo, puesto) values (%s, %s, %s, %s)"  #consulta, %s son valores que luego se sustituyen
        nombre=input("Introduce el nombre")
        apellido=input("Introduce el apellido")
        sueldo=float(input("Introduce el sueldo"))
        puesto=input("Introduce el puesto ")
        datos=(nombre, apellido, sueldo, puesto)
        cursor1.execute(sql, datos)   #introduce los datos en la consulta y lo ejecuta
        cnn.commit()
        cnn.close() #final 
        print("Redirreccionando al menu de empleados")
        print("--------------------------------------------")
        lista_empleados()   #te redirige hasta el menú principal de lista de empleados
    if eleccion1==2:   #borrar/modificar datos
        print("Ha accedido a la base de datos de trabajadores")
        cursor2=cnn.cursor()
        sql="delete from trabajador where (nombre, apellido) values (%s, %s)"  #borra filas enteras
        nombre=input("Introduce el nombre del trabajador que quieres borrar")
        apellido=input("Introduce el apellido del trabajador que quieres borrar")
        eleccion1borrado=input("Estás seguro de que deseas borrar PERMANENTEMENTE al trabajador",nombre,apellido)
        if eleccion1borrado=="si" or eleccion1borrado=="Si" or eleccion1borrado=="s" or eleccion1borrado=="S":   
            datos=(nombre,apellido)
            cursor2.execute(sql,datos)
            cnn.commit()
            cnn.close()
        else:
            print("Operación cancelada")
        print("Redirreccionando al menu de empleados")
        print("--------------------------------------------")
        lista_empleados()   #te redirige hasta el menú principal de lista de empleados
    if eleccion1==3:       #MUESTRA EL LISTADO DE TRABAJADORES
        print("Ha accedido a la base de datos de empleados")
        cursor3=cnn.cursor()
        cursor3.execute("select nombre, apellido, sueldo, puesto from trabajador")
        for fila in cursor3:          #printea la tabla entera con sus valores exactos
            print(fila) 
        cnn.close()
        sleep(3)
        print("Redirreccionando al menu de empleados")
        print("--------------------------------------------")
        lista_empleados()
    if eleccion1==4:  #vuelta al inicio (directorio)
        #te manda al inicio(directorio)
        print("----------------------------------------")
        directorio()
    if eleccion1>4 or eleccion1<1:    #valor fuera de rango
        print("Error, el número introducido no corresponde a ningún apartado")
        #te devuelve al inicio de la lista de empleados(vuelve a arrancar la función)
        print("--------------------------------------------------------")
        lista_empleados()  
        
def eleccionproducto():
    eleccion2=int(input("A dónde desea acceder?"))
    if eleccion2==1:       #MUESTRA EL LISTADO DE PRODUCTOS
        print("Ha accedido a la base de datos de productos")
        cursor4=cnn.cursor()
        cursor4.execute("select codigo, categoria, nombre_producto, cantidad, precio from productos")
        #printea la tabla entera con sus valores exactos
        for fila in cursor4:          
            print(fila)
        cnn.close()
        sleep(3)
        print("Redirreccionando al menu de productos")
        print("--------------------------------------------")
        lista_productos()
    if eleccion2==2:    #añadir nuevo producto
        print("Ha accedido al registro de productos")
        sleep(1)
        cursor5=cnn.cursor()  #crea un cursor para mysql
        sql="insert into productos (categoria, nombre_producto, cantidad, precio) values (%s, %s, %s, %s)"  #consulta para hacer %s son valores que luego se sustituyen
        categoria=input("Introduce la categoria del producto")
        nombre_producto=input("Introduce el nombre del producto")
        precio=float(input("Introduce el precio"))
        cantidad=int(input("Introduce la cantidad"))
        datos=(categoria, nombre_producto, precio, cantidad, )
        cursor5.execute(sql, datos)  #introduce los datos en la consulta y lo ejecuta
        cnn.commit()
        cnn.close() #final 
        print("Redirreccionando al menu de productos")
        print("--------------------------------------------")
        lista_productos()
    if eleccion2==3: #modificar cantidad producto
        print("Ha accedido al registro de productos")
        print("Aquí podrá modificar la cantidad de productos disponibles en stock")
        cursor6=cnn.cursor()
        sql="update productos SET cantidad = (cantidad3) WHERE nombre_producto =(producto) values (%s, %s)"
        producto=("Introduce el nombre del producto")
        cantidad3=int(input("Introduce la nueva cantidad del producto"))
        datos=(producto,cantidad3)
        cursor6.execute(sql, datos)
        cnn.commit()
        cnn.close()
        print("Redirreccionando al menu de productos")
        print("---------------------------------------------------")
        lista_productos()
    if eleccion2==4:    #avisos 
        print("Accediendo al apartado de avisos de existencias")
        print("Avisos:")
        cursor7=cnn.cursor()
        cursor7.execute("select codigo, categoria, nombre_producto, cantidad, precio, cantminima from productos")
        for fila in cursor7:
            if fila[3]<fila[5]:
                print("El producto:",fila[2],"se encuentra por debajo de la cantidad prevista, esperado:",fila[5],",en reserva:",fila[3])
            else:
                print("Todo en orden, no hay ningún artículo bajo mínimos")
        cnn.close()
        print("Redirreccionando al menu de productos")
        print("---------------------------------------------------")
        lista_productos()

def lista_productos(): 
    print("Ha accedido a la lista de productos")
    sleep(1)
    print("Aquí podrá ver los productos disponibles, la cantidad de estos actualmente y su precio")
    sleep(2)
    print("Opciones:")
    sleep(1)
    print("Para acceder al listado de productos escriba: 1")
    sleep(2)
    print("Para añadir un nuevo producto escriba: 2")
    sleep(2)
    print("Para modificar la cantidad de un producto en el almacén escriba: 3")
    sleep(2)
    print("-----------------------------------------------------------------")
    eleccionproducto()

def notas():
    print("Ha accedido a sus notas")
    print("Para escribir una nueva nota escriba:1")
    print("Para ver sus notas escriba:2")
    print("Para borrar alguna nota escriba:3")
    def eleccionnotas():
        eleccion3=int(input("Qué desea hacer?"))
        if eleccion3==1:
            print("Ha accedido al menu de creación de nuevas notas")
            cursor7=cnn.cursor
            sql="insert into notas (titulo, nota) values (%s,%s)"
            titulo=("Introduce el titulo de la nota")
            nota=("Introduce la nueva cantidad del producto")
            datos=(titulo,nota)
            cursor7.execute(sql, datos)
            cnn.commit()
            cnn.close()
            print("Redirreccionando al menu de notas")
            print("--------------------------------------------")
            notas()
        if eleccion3==2:
            print("Ha accedido al registro de notas")
            cursor8=cnn.cursor()
            cursor8.execute("select titulo, nota from notas")
            #printea la tabla entera con sus valores exactos
            for fila in cursor8:          
                print(fila)
            cnn.close()
            sleep(3)
            print("Redirreccionando al menu de notas")
            print("--------------------------------------------")
            notas()
        if eleccion3==3:
            print("Ha accedido al panel de borrado de notas")
            cursor9=cnn.cursor()
            cursor9.execute("delete from notas where (titulo) values (%s)")
            titulo=("Introduce el titulo de la nota que deseas borrar")
            eleccion3borrado=print("Estás seguro de que quieres borrar permanentemente la nota:",titulo)
            if eleccion3borrado=="si" or eleccion3borrado=="Si" or eleccion3borrado=="s" or eleccion3borrado=="S":
                datos=(titulo)
                cnn.execute(sql,datos)
                cnn.commit()
                cnn.close()
            else:
                print("Redirigiendo al menu de notas")
                print("--------------------------------------------")
                notas() 
        if eleccion3<1 or eleccion3>3:
            print("Número invalido")
            eleccionnotas()

def proveedores():
    print("Ha accedido al apartado: Proveedores")
    print("Para acceder al registro de proveedores escriba:1")
    print("")

#ejecutar
directorio()