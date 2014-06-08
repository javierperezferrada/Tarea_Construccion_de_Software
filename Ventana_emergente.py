# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):



    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self ):

        #Creando los labels
        self.Codigo_lbl = QtGui.QLabel(self)
        self.Nombre_lbl = QtGui.QLabel(self)
        self.Atributos_lbl = QtGui.QLabel(self)
        self.Descripcion_lbl = QtGui.QLabel(self)
        self.Imagen_lbl = QtGui.QLabel(self)
        self.Color_lbl = QtGui.QLabel(self)
        self.Precio_neto_lbl = QtGui.QLabel(self)
        self.Precio_bruto_lbl = QtGui.QLabel(self)
        self.Marca_id_lbl = QtGui.QLabel(self)
        ################################################

        #Creando los QLine donde iran los datos a editar o agregar
        self.Codigo = QtGui.QLineEdit(self)
        self.Nombre = QtGui.QLineEdit(self)
        self.Atributos = QtGui.QLineEdit(self)
        self.Descripcion = QtGui.QLineEdit(self)
        self.Imagen = QtGui.QLineEdit(self)
        self.Color = QtGui.QLineEdit(self)
        self.Precio_neto = QtGui.QLineEdit(self)
        self.Precio_bruto = QtGui.QLineEdit(self)
        self.Marca_id = QtGui.QLineEdit(self)
        ###################################################



        #Definiendo los contenidos de los labels
        self.Codigo_lbl.setText("Codigo:")
        self.Nombre_lbl.setText("Nombre:")
        self.Atributos_lbl.setText("Atributos:")
        self.Descripcion_lbl.setText("Descripcion:")
        self.Imagen_lbl.setText("Imagen:")
        self.Color_lbl.setText("Color:")
        self.Precio_neto_lbl.setText("Precio Neto:")
        self.Precio_bruto_lbl.setText("Precio Bruto:")
        self.Marca_id_lbl.setText("Marca:")
        ############################################

        #definiendo posicion de los Qline's
        self.Codigo.move(130, 50)
        self.Nombre.move(130, 100)
        self.Atributos.move(130, 150)
        self.Descripcion.move(130, 200)
        self.Imagen.move(130, 250)
        self.Color.move(130, 300)
        self.Precio_neto.move(130, 350)
        self.Precio_bruto.move(130, 400)
        self.Marca_id.move(130, 450)
        ###############################################

        #Definiendo la pocisiones de los LABELS
        self.Codigo_lbl.move(30, 50)
        self.Nombre_lbl.move(30, 100)
        self.Atributos_lbl.move(30, 150)
        self.Descripcion_lbl.move(30, 200)
        self.Imagen_lbl.move(30, 250)
        self.Color_lbl.move(30, 300)
        self.Precio_neto_lbl.move(30, 350)
        self.Precio_bruto_lbl.move(30, 400)
        self.Marca_id_lbl.move(30, 450)
        ################################################

        #Ajustando el ancho de los QLine's
        self.Codigo.setFixedWidth(385)
        self.Nombre.setFixedWidth(385)
        self.Atributos.setFixedWidth(385)
        self.Descripcion.setFixedWidth(385)
        self.Imagen.setFixedWidth(200)
        self.Color.setFixedWidth(385)
        self.Precio_neto.setFixedWidth(385)
        self.Precio_bruto.setFixedWidth(385)
        self.Marca_id.setFixedWidth(385)
        ##########################################

        #Definiendo el largo maximo permitido en los QLine's
        self.Codigo.setMaxLength(45)
        self.Nombre.setMaxLength(45)
        self.Atributos.setMaxLength(45)
        self.Descripcion.setMaxLength(45)
        self.Imagen.setMaxLength(45)
        self.Color.setMaxLength(45)
        self.Precio_bruto.setMaxLength(254)
        self.Precio_neto.setMaxLength(254)
        # BOTON Guardar datos
        btn_Guardar = QtGui.QPushButton('Guardar', self)
        btn_Guardar.move(490, 550)
        btn_Guardar.clicked.connect(self.btn_guardar_clicked) # HACER FUNCION!!!!!!!!!! #################################################################################

        # BOTON cancelar
        btn_Cancelar = QtGui.QPushButton('Cancelar', self)
        btn_Cancelar.move(390, 550)
        btn_Cancelar.clicked.connect(self.btn_cancelar_clicked)

        # BOTON LIMPIAR Campos
        btn_Limpiar = QtGui.QPushButton('Limpiar', self)
        btn_Limpiar.move(50, 550)
        btn_Limpiar.clicked.connect(self.btn_limpiar_clicked)

        # BOTON CARGAR IMAGEN
        btn_imagen = QtGui.QPushButton('Cargar imagen', self)
        btn_imagen.move(350, 250)
        btn_imagen.clicked.connect(self.btn_imagen_clicked)

        #Validando que sean solo numeros
        self.Precio_neto.textChanged[str].connect(self.onChangedNeto)
        self.Precio_bruto.textChanged[str].connect(self.onChangedBruto)

        self.setGeometry(0, 0, 600, 700)
        self.setFixedSize(600, 600)
        self.setWindowTitle('Ventana Editar/Agregar Productos')
        self.show()

    # Esto permite cargar imagenes, y deja la ruta en qline de imagen
    def btn_imagen_clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Elige la imagen del producto', '/home','Imagenes (*.png  *.bmp *.psd *.xpm *.jpg)')
        fname = ''.join(fname)
        fname = fname.split("Imagenes (*.png  *.bmp *.psd *.xpm *.jpg)")
        if fname[0] != '':
            self.Imagen.setText(fname[0])

    def btn_guardar_clicked(self):
        #verifica si algunos de los campos ESTA VACIO
        if (self.hay_espacios(self.Codigo.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo CODIGO se encuentra vacio')

        elif (self.hay_espacios(self.Nombre.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo NOMBRE se encuentra vacio')

        elif (self.hay_espacios(self.Atributos.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo ATRIBUTOS se encuentra vacio')

        elif (self.hay_espacios(self.Descripcion.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo DESCRIPCION se encuentra vacio')

        elif (self.hay_espacios(self.Imagen.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo IMAGEN se encuentra vacio')

        elif (self.hay_espacios(self.Color.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo COLOR se encuentra vacio')

        elif (self.hay_espacios(self.Precio_neto.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo PRECIO NETO se encuentra vacio')

        elif (self.hay_espacios(self.Precio_bruto.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo PRECIO BRUTO se encuentra vacio')

        elif (self.hay_espacios(self.Marca_id.text())):
            QtGui.QMessageBox.information(self, 'Campo Vacio', 'El campo MARCA se encuentra vacio')
        ############################################################################

        else:
            resp = QtGui.QMessageBox.question(self, 'Editar/Agregar Producto',
                     '¿Desea Editar/Agregar producto?','Si','No', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if resp == QtGui.QMessageBox.Yes:
                print "bien" # >>>>>>>>>>>AQUI QUEDEEE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            else:
                print "mal"

    #Detecta si el texto ingresado es vacio o lleno de espacios
    def hay_espacios(self, textoo):
        s = textoo
        t = s.split(" ")
        largos = len(s)
        largot =len(t)-1
        if not s or (largot == largos): # Es vacio o lleno de espacios
            return True
        else:
            return False #Todo bien
    #############################################################

    #Cierra Ventana_emergente.py
    def btn_cancelar_clicked(self):
        sys.exit(1)


    #Limpiar todos los campos
    def btn_limpiar_clicked(self):
        self.Codigo.setText("")
        self.Nombre.setText("")
        self.Atributos.setText("")
        self.Descripcion.setText("")
        self.Imagen.setText("")
        self.Color.setText("")
        self.Precio_neto.setText("")
        self.Precio_bruto.setText("")
        self.Marca_id.setText("")
    ############################################

    #funcion para validar numeros y borrar letras de PRECIO_BRUTO
    def onChangedBruto(self, text):
        try:
            text = int(text)
        except Exception:
            self.Precio_bruto.setText(text[:-1])

    #funcion para validar numeros y borrar letras de PRECIO_NETO
    def onChangedNeto(self, text):
        try:
            text = int(text)
        except Exception:
            self.Precio_neto.setText(text[:-1])

    #funcion para validar hay espacios





def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()