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


class ventana_emgergente(QDialog):

    def __init__(self):
        QDialog.__init__(self, parent)

        contenedor = QVBoxLayout()
        self.setLayout(contenedor)
        self.setWindowTitle("Agregar / Editar producto")

        btnSalir = QPushButton("Salir",None)
        contenedor.addWidget(btnSalir)
        self.connect(btnSalir, SIGNAL("clicked()"), self.salir)

    def salir(self):
        exit()

if __name__ == '__main__':
    run()

