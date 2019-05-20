# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QAbstractListModel, QThread
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import translator
import asyncio

""" Translate language model """
class LangModel(QAbstractListModel):
    def __init__(self, data=None, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, role=None):
        item = self._data[QModelIndex.row()]

        if role == Qt.DisplayRole:
            return "%s" % (item['name'])
        elif role == Qt.DecorationRole:
            return QColor(item['color'])
        elif role == Qt.BackgroundRole:
            return QBrush(Qt.Dense7Pattern)
        elif role == Qt.ToolTipRole:
            return "Tool Tip: %s" % (item['name'])
        return QVariant()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 611)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(210, 30, 131, 41))
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 100, 131, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.model = QStandardItemModel()
        self.model.appendRow(QStandardItem("ko"))
        self.model.appendRow(QStandardItem("en"))

        # self.listView = QtWidgets.QListView(self.centralwidget)
        # self.listView.setGeometry(QtCore.QRect(360, 40, 271, 31))
        # self.listView.setObjectName("departure_list")
        # self.listView.setModel(self.model)

        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(360, 100, 271, 31))
        self.listView_2.setObjectName("destination_list")
        self.listView_2.setModel(self.model)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 210, 311, 311))
        self.textEdit.setObjectName("departure_edit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(450, 210, 311, 311))
        self.textEdit_2.setObjectName("destination_edit")
        self.textEdit_2.setReadOnly(True)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 131, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 160, 131, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickPushBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NDY Translator"))
        # self.label.setText(_translate("MainWindow", "번역할 언어"))
        self.label_2.setText(_translate("MainWindow", "번역될 언어"))
        self.label_3.setText(_translate("MainWindow", "번역할 Text"))
        self.label_4.setText(_translate("MainWindow", "번역된 Text"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))

    def onClickPushBtn(self):
        translate_target_str = self.textEdit.toPlainText()
        destination_lang = translator.get_lang(self.listView_2.selectionModel().currentIndex().row())
        print(destination_lang)
        print(translate_target_str)
        self.textEdit_2.setPlainText(translator.translate(destination_lang, translate_target_str))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windowForm = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(windowForm)

    windowForm.show()
    sys.exit(app.exec_())