import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

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
        Codigo = QtGui.QLineEdit(self)
        Nombre = QtGui.QLineEdit(self)
        Atributos = QtGui.QLineEdit(self)
        Descripcion = QtGui.QLineEdit(self)
        Imagen = QtGui.QLineEdit(self)
        Color = QtGui.QLineEdit(self)
        Precio_neto = QtGui.QLineEdit(self)
        Precio_bruto = QtGui.QLineEdit(self)
        Marca_id = QtGui.QLineEdit(self)
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
        Codigo.move(130, 50)
        Nombre.move(130, 100)
        Atributos.move(130, 150)
        Descripcion.move(130, 200)
        Imagen.move(130, 250)
        Color.move(130, 300)
        Precio_neto.move(130, 350)
        Precio_bruto.move(130, 400)
        Marca_id.move(130, 450)
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
        Codigo.setFixedWidth(385)
        Nombre.setFixedWidth(385)
        Atributos.setFixedWidth(385)
        Descripcion.setFixedWidth(385)
        Imagen.setFixedWidth(200)
        Color.setFixedWidth(385)
        Precio_neto.setFixedWidth(385)
        Precio_bruto.setFixedWidth(385)
        Marca_id.setFixedWidth(385)
        ##########################################
        Codigo.setMaxLength(45)

        # BOTON CARGAR IMAGEN
        btn_imagen = QtGui.QPushButton('Cargar imagen', self)
        btn_imagen.move(350, 250)
        btn_imagen.clicked.connect(self.btn_imagen_clicked)


        self.setGeometry(300, 350, 600, 700)
        self.setWindowTitle('Buttons')
        self.show()

    def btn_imagen_clicked(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Elige la imagen del producto', '/home','Imagenes (*.png  *.bmp *.psd *.xpm *.jpg)')
        fname = ''.join(fname)
        fname = fname.split("Imagenes (*.png  *.bmp *.psd *.xpm *.jpg)")
        print "------"
        print fname[0]
        print "------"




def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()