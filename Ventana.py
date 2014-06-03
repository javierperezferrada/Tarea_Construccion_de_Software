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
        self.tb_layout.setAlignment(QtCore.Qt.AlignRight)
        self.toolbox.setLayout(self.tb_layout)

        self.btn_add = QtGui.QPushButton(u"&Nuevo Producto")
        self.btn_edit = QtGui.QPushButton(u"&Editar")
        self.btn_delete = QtGui.QPushButton(u"&Eliminar")
        #Agregamos los botones al layout
        self.tb_layout.addWidget(self.btn_add)
        self.tb_layout.addWidget(self.btn_edit)
        self.tb_layout.addWidget(self.btn_delete)
        #Agregamos el widget toolbox a la pantalla principal
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

        alumnos = controller.obtener_alumnos()
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(alumnos), 4)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"RUT"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellidos"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Correo"))

        r = 0
        for row in alumnos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['rut'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombres'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['apellidos'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['correo'])
            r = r+1
        self.table.setModel(self.model)

        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 210)
        self.table.setColumnWidth(2, 210)
        self.table.setColumnWidth(3, 220)

    def set_signals(self):
        self.btn_delete.clicked.connect(self.delete)

    def delete(self):
        model = self.table.model()
        index = self.table.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
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

def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()

