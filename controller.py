#!/usr/bin/python
# -*- coding: utf-8 -*-
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
 

def logines(usuario,contrasenia):
    #verifica la existencia del usuario
    con = conectar()
    c = con.cursor()
    query = "SELECT count(user) FROM usuarios WHERE user = ?"
    #con un contador verifico si existe el usuario
    try:
        resultado = c.execute(query, [usuario])
        cont = resultado.fetchall()
    except sqlite3.Error as e:
        print "Error:", e.args[0]
    a = int(cont[0][0])
    if a > 0:
        query1 = "SELECT id_usuario FROM usuarios WHERE user = ?"
        try:
            resultad = c.execute(query1, [usuario])
            identi = resultad.fetchall()
            identi=int(identi[0][0])
            result = verifica(identi,contrasenia)
            print result
        except sqlite3.Error as e:
            print "Error:", e.args[0]
    else:
        print 'No existe usuario'
        result = False
    con.close()
    return result

def verifica(identi,contrasenia):
    #verifica contraseña
    con = conectar()
    c = con.cursor()
    #si existe usuario, verificamos contraseña
    query = "SELECT password FROM usuarios WHERE id_usuario = ?"
    try:
        resultado = c.execute(query, [identi])
        contras= resultado.fetchall()
    except sqlite3.Error as e:
        print "Error:", e.args[0]
    con.close()
    contra = contras[0][0]
    if contra == contrasenia:
        res = True
    else: 
        print 'Contraseña erronea!!!'
        res = False
    return res    

