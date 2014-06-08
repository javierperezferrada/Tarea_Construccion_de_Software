import sqlite3

def conectar():
    #Funcion para conectar con la base de datos db_tarea1.db
    con = sqlite3.connect('db_tarea1.db')
    con.row_factory = sqlite3.Row
    return con

def obtener_productos():
    #Funcion que entrega los productos
    con = conectar()
    c = con.cursor()
    query = '''select p.id,p.nombre, p.atributos,p.descripcion,p.precio_neto,
             p.precio_bruto, m.nombre nombre_m from productos p, marcas m
             where m.id == p.marca_id'''
    resultado= c.execute(query)
    productos = resultado.fetchall()
    con.close()
    return productos

def obtener_marcas():
    #Funcion que entrega las marcas
    con = conectar()
    c = con.cursor()
    query = "SELECT id,nombre FROM marcas"
    resultado = c.execute(query)
    marcas = resultado.fetchall()
    con.close()
    return marcas

def obtener_productos_marca(marca):
    #Funcion que entrega los productos de una marca determinada
    con = conectar()
    c = con.cursor()
    query = '''select p.id,p.nombre, p.atributos,p.descripcion,p.precio_neto,
             p.precio_bruto, m.nombre nombre_m from productos p, marcas m
             where m.id == p.marca_id and m.nombre == ?'''
    resultado = c.execute(query,[marca])
    productos = resultado.fetchall()
    con.close()
    return productos


def obtener_nombres(text):
    '''Funcion que entrega los productos que contienen el string text en su
        campo nombre'''
    con = conectar()
    c = con.cursor()
    query = "select p.id,p.nombre, p.atributos,p.descripcion,p.precio_neto,p.precio_bruto, m.nombre nombre_m from productos p, marcas m where m.id == p.marca_id and p.nombre LIKE'%'||?||'%'"
    try:
        resultado = c.execute(query, [text])
        nombres = resultado.fetchall()
    except sqlite3.Error as e:
        print "Error:", e.args[0]
    con.close()
    return nombres

def delete(producto):
    #Funcion que borra de la bd el producto con id producto
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM productos WHERE id = ?"
    try:
        c.execute(query, [producto])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

