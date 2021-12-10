#Nombre de la aplicación: OP helper
#Creado por Pablo Calvo Espinar
#Descripción:
#Esta aplicación brinda al usuario promedio la posibilidad de usar una base de datos sin tener conocimientos sobre el tema, posee las siguientes funcionalidades:
#Menu de usuario con contraseña y opción a registrarte, esto seguro ya que se deja asignado.
#Apartado para gestionar tus empleados, productos y notas personales

#conexion base de datos
import mysql.connector
cnn=mysql.connector.connect(host="localhost",user="root",
passwd="",database="aplicacion")
#print(cnn) #si quieres comprobar que tu conexión a base de datos está bien elimina el # y te deberá aparecer al ejecutarlo algo similar a esto: <mysql.connector.connection_cext.CMySQLConnection object at 0x00000291BF3A1100>

#otras librerias
from time import sleep       #libreria standar de python
import os #para limpiar pantalla os.system ("cls")
def directorio():
    print("")
    print(" _____________________________________________________________________________________")
    print("|                                                                                     |")
    print("|  Opciones:                                                                          |")
    print("|      Lista de empleados y sueldos escriba:    1                                     |")
    print("|      Lista de productos escriba:              2                                     |")
    print("|      Notas personales escriba:                3                                     |")
    print("|      Cerrar sesion escriba:                   4                                     |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|_____________________________________________________________________________________|")
    print("")
    sleep(2)
    eleccion=int(input("A dónde quieres acceder? "))
    if eleccion>4 or eleccion<1:
        print("Número invalido")  
    if eleccion==1:   #funcion empleados
        print("Accediendo al apartado de empleados")    
        sleep(1.3)
        os.system("cls")
        lista_empleados()
    if eleccion==2:   #funcion productos
        print("Accediendo al apartado de productos")
        sleep(1.3)
        lista_productos()    
    if eleccion==3:   #funcion notas
        print("Accediendo a tus notas")
        sleep(1.3)
        notas()
    if eleccion==4:
        exit()    #stopea la app

def lista_empleados():
    print("")
    print(" _____________________________________________________________________________________")
    print("|                               Lista de empleados                                    |")
    print("|  Opciones:                                                                          |")
    print("|      Nuevo empleado escriba:               1                                        |")
    print("|      Borrar empleado escriba:              2                                        |")
    print("|      Ver listado empleados:                3                                        |")
    print("|      Volver al menu escriba:               4                                        |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|_____________________________________________________________________________________|")
    print("")
    sleep(1.5)
    eleccion1=int(input("¿Qué desea hacer? "))
    if eleccion1==1:   #añadir datos
        os.system("cls")
        print("Ha accedido al registro de empleados.")
        sleep(1)
        cursor1=cnn.cursor()    #crea un cursor, conjunto de registros devueltos por una instrucción sql
        sql="insert into empleados (usuario, nombre, apellido, sueldo, puesto) values (%s,%s, %s, %s, %s)"  #consulta, %s son valores que luego se sustituyen
        nombre=input("Introduce el nombre: ")
        apellido=input("Introduce el apellido: ")
        sueldo=float(input("Introduce el sueldo: "))
        puesto=input("Introduce el puesto: ")
        datos=(usuario, nombre, apellido, sueldo, puesto)
        cursor1.execute(sql, datos)   #introduce los datos en la consulta y lo ejecuta
        cnn.commit()
        print("GUARDADO")
        print("")
        cnn.close() #final 
        print("Redirreccionando al menu de empleados")
        print("--------------------------------------------")
        sleep(1.5)
        os.system("cls")
        lista_empleados()   #te redirige hasta el menú principal de lista de empleados
    if eleccion1==2:   #borrar/modificar datos
        print("Ha accedido a la base de datos de trabajadores")
        #El primer cursor muestra todos los datos para poder elegir cual borrar correctamente
        print("Mostrando listado de empleados: ")
        cursor=cnn.cursor()
        cursor.execute("select usuario, codigo_trabajador, nombre, apellido, sueldo, puesto from empleados")
        cont=0
        for fila in cursor:
            if fila[0]==usuario:
                print("codigo del trabajador:",fila[1], ", nombre:",fila[2],", apellido:",fila[3],", sueldo:",fila[4],", puesto:",fila[5])
                cont=cont+1
                print("------------------------------------")
        if cont==0:
            print("No tienes ningún empleado registrado")
            lista_empleados()
        cursor2=cnn.cursor()
        sql=("delete from empleados where usuario=%s and codigo_trabajador=%s")
        codigo_trabajador=int(input("¿Cual es el código del trabajador? ")) 
        eleccion1borrado=input("Estás seguro de que deseas borrar PERMANENTEMENTE al trabajador? [s/n]: ")
        if eleccion1borrado=="si" or eleccion1borrado=="Si" or eleccion1borrado=="s" or eleccion1borrado=="S":   
            datos=(usuario, codigo_trabajador)
            cursor2.execute(sql,datos)
            cnn.commit()
            print("Borrado con exito")
            sleep(1.3)
        else:
            print("Operación cancelada")
        print("Redirreccionando al menu de empleados")
        print("--------------------------------------------")
        sleep(1.8)
        cnn.close()
        os.system("cls")
        lista_empleados()   #te redirige hasta el menú principal de lista de empleados
    if eleccion1==3:       #MUESTRA EL LISTADO DE TRABAJADORES
        os.system("cls")
        print("Ha accedido a la base de datos de empleados")
        cursor=cnn.cursor()
        cursor.execute("select usuario, codigo_trabajador, nombre, apellido, sueldo, puesto from empleados")
        cont=0
        print("Empleados:")
        for fila in cursor:
            if fila[0]==usuario:
            #usamos esto en vez de print(fila) para que no se muestre el nombre de usuario
                print("codigo del trabajador:",fila[1], ", nombre:",fila[2],", apellido:",fila[3],", sueldo:",fila[4],", puesto:",fila[5]) 
                print("--------------------------------------------")
                cont=cont+1   #este contador sirve para detectar si se tiene algun empleado registrado
        if cont==0:       #al detectar que cont=!0 se asume que si había registros, al no haberlos te muestra que no tienes ningun dato
            print("No tienes ningún empleado registrado")
        print("Redirreccionando al menu de empleados")
        sleep(1)
        print("----------------------------------------")
        sleep(1.8)
        lista_empleados()
    if eleccion1==4:  #vuelta al inicio (directorio)
        #te manda al inicio(directorio)
        print("Redirrecionando")
        print("----------------------------------------")
        sleep(1.3)
        os.system("cls")
        directorio()
    if eleccion1>5 or eleccion1<1:    #valor fuera de rango
        print("Error, el número introducido no corresponde a ningún apartado")
        #te devuelve al inicio de la lista de empleados(vuelve a arrancar la función)
        print("--------------------------------------------------------")
        sleep(1.5)
        os.system("cls")
        lista_empleados()  
        
def eleccionproducto():
    eleccion2=int(input("A dónde desea acceder? "))
    if eleccion2==1:       #MUESTRA EL LISTADO DE PRODUCTOS
        print("Ha accedido a la base de datos de productos")
        cursor4=cnn.cursor()
        cursor4.execute("select usuario, codigo, categoria, nombre_producto, cantidad, precio, stock_minimo from productos")
        #printea la tabla entera con sus valores exactos
        cont=0
        for fila in cursor4:
            if fila[0]==usuario:
                print("codigo", fila[1],", categoria:",fila[2],", nombre:",fila[3],", cantidad:",fila[4],", precio",fila[5],", stock minimo:",fila[6])
                cont=cont+1
        if cont==0:
            print("No dispones de productos en stock")
        sleep(3)
        print("Redirreccionando al menu de productos")
        print("--------------------------------------------")
        sleep(1.3)
        os.system("cls")
        lista_productos()
    if eleccion2==2:    #añadir nuevo producto
        print("Ha accedido al registro de productos")
        sleep(1)
        cursor5=cnn.cursor()  #crea un cursor para mysql
        sql="insert into productos (usuario, categoria, nombre_producto, cantidad, precio) values (%s, %s, %s, %s,%s)"  #consulta para hacer %s son valores que luego se sustituyen
        categoria=input("Introduce la categoria del producto")
        nombre_producto=input("Introduce el nombre del producto")
        precio=float(input("Introduce el precio"))
        cantidad=int(input("Introduce la cantidad"))
        datos=(usuario,categoria, nombre_producto, precio, cantidad, )
        cursor5.execute(sql, datos)  #introduce los datos en la consulta y lo ejecuta
        cnn.commit()
        cnn.close() #final 
        print("Producto añadido con exito")
        print("")
        print("Redirreccionando al menu de productos")
        print("--------------------------------------------")
        sleep(1.5)
        os.system("cls")
        lista_productos()
    if eleccion2==3: #modificar cantidad producto
        print("Ha accedido al registro de productos")
        print("Aquí podrá modificar la cantidad de productos disponibles en stock")
        cursor6=cnn.cursor()
        sql="update productos SET cantidad = (cantidad3) WHERE usuario, nombre_producto = (producto) values (%s,%s, %s)"   #cambia el valor de cantidad en el producto seleccionado
        producto=("Introduce el nombre del producto")
        cantidad3=int(input("Introduce la nueva cantidad del producto"))
        datos=(usuario,producto,cantidad3)
        cursor6.execute(sql, datos)
        print("Producto guardado con exito")
        cnn.commit()
        cnn.close()
        #este cursor comprueba si el producto para el cual acabas de hacer un cambio en la cantidad se encuentra bajo la cantidad preestablecida, si no ocurre
        #no mostrará ningun mensaje en pantalla, es la funcion de avisos reciclada. 
        cursor9=cnn.cursor()
        sql=("select usuario, codigo, categoria, nombre_producto, cantidad, precio, cantminima from productos where usuario, producto values (%s,%s)")
        datos=(usuario,producto)
        cursor9.execute(sql,datos)
        for fila in cursor9:
            if fila[0]==usuario and fila[3]==producto and fila[4]<fila[6]:
                print("El producto: ",fila[3],"se encuentra por debajo del stock mínimo, repongalo con la mayor brevedad posible")
        print("Redirreccionando al menu de productos")
        print("---------------------------------------------------")
        sleep(1.3)
        os.system("cls")
        lista_productos()
    if eleccion2==4:    #avisos 
        print("Accediendo al apartado de avisos de existencias")
        print("Avisos:")
        cursor7=cnn.cursor()
        cursor7.execute("select usuario, codigo, categoria, nombre_producto, cantidad, precio, stock_minimo from productos")
        cont=0
        for fila in cursor7:
            if fila[0]==usuario:    #fila[0] corresponde con el nombre del usuario en la base de datos
                if fila[4]<fila[6]:
                    print("El producto:",fila[3],"se encuentra por debajo de la cantidad prevista, esperado:",fila[6],",en stock:",fila[4])
                    cont=cont+1    #si no hay ningun aviso cont lo dectectará pues sería igual a 0 
        if cont==0:
            print("No tienes ningún aviso, todo en órden!")
        if cont!=0:
            sleep(2)
        print("Redirreccionando al menu de productos")
        print("---------------------------------------------------")
        sleep(1.3)
        os.system("cls")
        lista_productos()

def lista_productos(): 
    os.system("cls")
    print("")
    print(" _____________________________________________________________________________________")
    print("|                                Productos                                            |")
    print("|  Opciones:                                                                          |")
    print("|      Lista de productos escriba:            1                                       |")
    print("|      Añadir un nuevo producto:              2                                       |")
    print("|      Modificar cantidad producto escriba:   3                                       |")
    print("|      Ver avisos escriba:                    4                                       |")
    print("|      Volver al menu escriba:                5                                       |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|_____________________________________________________________________________________|")
    print("")
    sleep(1.5)
    eleccionproducto()

def notas():
    os.system("cls")
    print("")
    print(" _____________________________________________________________________________________")
    print("|                                    Notas                                            |")
    print("|  Nota nueva escriba:  1                                                             |")
    print("|  Ver notas escriba:   2                                                             |")
    print("|  Borra notas escriba: 3                                                             |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|_____________________________________________________________________________________|")
    sleep(1.2)
    print("")
    eleccion3=int(input("Qué desea hacer?"))
    if eleccion3==1:
        print("Ha accedido al menu de creación de nuevas notas")
        cursor=cnn.cursor()
        sql="insert into notas (usuario,titulo,nota) values (%s,%s,%s)"
        titulo=input("Introduce el título de la nota: ")
        nota=input("Introduce la nota: ")
        datos=(usuario,titulo,nota)
        cursor.execute(sql,datos)
        cnn.commit()
        cnn.close()
        print("Redirreccionando al menu de notas")
        print("--------------------------------------------")
        sleep(1.5)
        os.system("cls")
        notas()
    if eleccion3==2:
        print("Ha accedido al registro de notas")
        cursor8=cnn.cursor()
        cursor8.execute("select usuario, codigo, titulo, nota from notas")
        #printea la tabla entera con sus valores exactos
        cont=0
        for fila in cursor8:
            if fila[0]==usuario:    #fila[0] en nuestra tabla usuarios es el nombre de usuario
                print("Codigo:",fila[1]," Titulo:",fila[2]," Nota:",fila[3])   #corresponde en la base de datos
                cont=cont+1   #contador para que detecte si no tienes notas registradas, se chekea en el if de debajo
        if cont==0:
            print("No tienes notas registradas :(")
            cnn.close()
        sleep(3)
        print("Redirreccionando al menu de notas")
        print("--------------------------------------------")
        os.system("cls")
        notas()
        
    if eleccion3==3:
            print("Ha accedido al panel de borrado de notas")
            cursor9=cnn.cursor()
            cursor9.execute("delete from notas where usuario, titulo values (%s,%s)")
            titulo=("Introduce el titulo de la nota que deseas borrar")
            eleccion3borrado=print("Estás seguro de que quieres borrar permanentemente la nota:",titulo)
            if eleccion3borrado=="si" or eleccion3borrado=="Si" or eleccion3borrado=="s" or eleccion3borrado=="S":
                datos=(usuario,titulo)
                cnn.execute(sql,datos)
                cnn.commit()
                cnn.close()
                notas()
            else:
                print("Redirigiendo al menu de notas")
                print("--------------------------------------------")
                notas() 
    if eleccion3<1 or eleccion3>3:
        print("Número invalido")
        notas()

def funcion_registro():
    cursor=cnn.cursor()
    nuevousuario=input("Introduce tu nuevo nombre de usuario: ")
    nuevacontraseña=input("Introduce tu nueva contraseña entre 6 y 15 dígitos o letras: ")
    #Esto ejecuta la sentencia sql, esta lee todos los nombres de usuario y contraseñas aunque esta ultima no se usa en este apartado
    cursor.execute("select  nombre_usuario, contraseña_usuario from usuarios")   
    if len(nuevacontraseña)<6 or len(nuevacontraseña)>15:   #valida que la contraseña posea determinados caracteres
        print("Contraseña invalida, vuelve a intentarlo")
        funcion_registro() #reincia la función
    for fila in cursor:
        if fila[0]==nuevousuario: #fila[0] coincide con los nombres de los respectos usuarios en nuestra base de datos
            print("Nombre de usuario en uso")
            print("Introduzca un nuevo nombre de usuario")
            funcion_registro() #reincia la función
    cursor=cnn.cursor()
    #esto sirve para que se registre el usuario con la contraseña en la base de datos
    sql=("INSERT INTO usuarios (nombre_usuario, contraseña_usuario) VALUES (%s,%s)") 
    datos=(nuevousuario,nuevacontraseña)
    cursor.execute(sql,datos)
    cnn.commit()   #hace un "guardado"
    cnn.close()
    print("Reiniciando aplicacion")
    exit()

#codigo principal
os.system("cls")
print("")
print(" _____________________________________________________________________________________")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                            Bienvenido a SecretariOP                                 |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|                                                                                     |")
print("|_____________________________________________________________________________________|")
sleep(1.2)

print("")
respuesta=input("¿Estás registrado? [s/n]: ")
if respuesta=="s" or respuesta=="S":
    usuario=input("Introduce tu nombre de usuario: ")
    contraseña=input("Introduce la contraseña: ")
    cursor=cnn.cursor() #crea un cursor con el cual ejecutaremos el codigo de sql'
    cursor.execute("select  nombre_usuario, contraseña_usuario from usuarios")    #detecta si el usuario y contraseña son correctos
    for fila in cursor:
        #fila[0] en nuestra base de datos corresponde con los distintos nombres de usuarios y fila[1] las contraseñas
        #Esto comprueba si existe el usuario con la contraseña dada fila por fila
        if fila[0]==usuario and fila[1]==contraseña:   
            print("Bienvenido de vuelta",usuario)
            print("----------------------------------")
            sleep(1.7)
            os.system("cls")
            directorio()               #redirección a funcion principal
    else:
        #detecta que no está registrado ya que no coincide con ninguno ya registrado
        respuesta2=input("No estás registrado, deseas registrarte?[s/n]")    
        if respuesta2=="S" or respuesta2=="s":
            funcion_registro()  #realiza la operación registro
        else:
            exit()              #detiene totalmente el programa
else:
    respuesta4=input("Deseas registrarte?[s/n]")
    if respuesta4=="s" or respuesta4=="S":
        funcion_registro()    #realiza la operación de registro
    else:
        exit()    #detiene totalmente el programa