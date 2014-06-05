#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller

class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.resize(800, 500)
        #http://srinikom.github.io/pyside-docs/PySide/QtGui/QVBoxLayout.html
        self.main_layout = QtGui.QVBoxLayout(self)
        #Dibujar grilla
        self.render_toolbox()
        self.render_table()
        self.load_data()
        self.set_signals()
        self.show()

    def render_toolbox(self):
        self.toolbox = QtGui.QWidget(self)
        self.tb_layout = QtGui.QHBoxLayout()
        self.vl = QtGui.QVBoxLayout()
        self.hl = QtGui.QHBoxLayout()
        self.tb_layout.setAlignment(QtCore.Qt.AlignRight)


        self.qle = QtGui.QLineEdit(self)
        self.lbl = QtGui.QLabel("Seleccione una marca", self)

        self.combo = QtGui.QComboBox(self)
        brands = controller.obtener_marcas()
        i = 0
        while i < len(brands):
            self.combo.addItem(brands[i][1])
            i = i + 1
        self.combo.addItem("Todas las marcas")

        self.btn_add = QtGui.QPushButton(u"&Nuevo Producto")
        self.btn_edit = QtGui.QPushButton(u"&Editar")
        self.btn_delete = QtGui.QPushButton(u"&Eliminar")
        #Agregamos los botones al layout
        self.tb_layout.addWidget(self.btn_add)
        self.tb_layout.addWidget(self.btn_edit)
        self.tb_layout.addWidget(self.btn_delete)
        self.hl.addWidget(self.qle)
        self.hl.addWidget(self.lbl)
        self.hl.addWidget(self.combo)
        #Agregamos el widget toolbox a la pantalla principal
        self.vl.addLayout(self.hl)
        self.vl.addLayout(self.tb_layout)
        self.toolbox.setLayout(self.vl)
        self.main_layout.addWidget(self.toolbox)

    def render_table(self):
        self.table = QtGui.QTableView(self)
        self.table.setFixedWidth(790)
        self.table.setFixedHeight(450)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        #Se incorpora la tabla al layout
        self.main_layout.addWidget(self.table)

    def load_data(self):

        productos = controller.obtener_productos()
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(productos), 4)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"ID"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Atributos"))

        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['atributos'])
            r = r+1
            self.table.setModel(self.model)

            self.table.setColumnWidth(0, 100)
            self.table.setColumnWidth(1, 210)
            self.table.setColumnWidth(2, 210)
            self.table.setColumnWidth(3, 220)

    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.btn_delete.clicked.connect(self.delete)
        self.qle.textChanged[str].connect(self.onChanged)


    def delete(self):
        model = self.table.model()
        index = self.table.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            msgBox2 = QtGui.QMessageBox()
            msgBox2.setText(u"Se eliminará el registro")
            msgBox2.setInformativeText(u"¿Está seguro de eliminar el registro?")
            msgBox2.setStandardButtons(QtGui.QMessageBox.Cancel | QtGui.QMessageBox.Ok)
            msgBox2.setDefaultButton(QtGui.QMessageBox.Ok)
            ret = msgBox2.exec_()
            if ret == QtGui.QMessageBox.Ok:
                if (controller.delete(rut)):
                    self.load_data()
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText("EL registro fue eliminado.")
                    msgBox.exec_()
                    return True
                else:
                    self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                    self.ui.errorMessageDialog.showMessage("Error al eliminar el registro")
                    return False

    def onChanged(self, text):
        producto = controller.obtener_nombres(text)
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(producto), 4)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"ID"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Codigo"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Atributos"))

        r = 0
        for row in producto:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['id'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['atributos'])
            r = r+1
            self.table.setModel(self.model)

            self.table.setColumnWidth(0, 100)
            self.table.setColumnWidth(1, 210)
            self.table.setColumnWidth(2, 210)
            self.table.setColumnWidth(3, 220)

''' def llenar_combo(self, combo):
        #funcion que retorna un vector con las marcas que estan contenidas en la base de datos.
        marcas = obtener_marcas()
        self
		
       '''


def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())


class Ventana_emergente(object): # Esta ventana tiene la funcionalidad de editar / agregar productos a la base de datos
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 833)
        MainWindow.setMaximumSize(QtCore.QSize(16777210, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textbox_buscar = QtGui.QLineEdit(self.centralwidget)
        self.textbox_buscar.setMaxLength(45)
        self.textbox_buscar.setObjectName("textbox_buscar")
        self.verticalLayout.addWidget(self.textbox_buscar)
        self.btn_buscar = QtGui.QPushButton(self.centralwidget)
        self.btn_buscar.setObjectName("btn_buscar")
        self.verticalLayout.addWidget(self.btn_buscar)
        spacerItem = QtGui.QSpacerItem(387, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(True)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setText("")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setPixmap(QtGui.QPixmap("../../Descargas/funny-monkey-2.jpg"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Agregar / Editar productos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Codigo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Descripción:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Atributos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Precio Neto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Precio Neto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
    def salir(self):
        exit()

if __name__ == '__main__':
    run()

