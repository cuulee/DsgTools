# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_createComplex.ui'
#
# Created: Mon Nov 10 16:21:34 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(550, 410)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.fileLineEdit = QtGui.QLineEdit(Dialog)
        self.fileLineEdit.setObjectName(_fromUtf8("fileLineEdit"))
        self.horizontalLayout_2.addWidget(self.fileLineEdit)
        self.filePushButton = QtGui.QPushButton(Dialog)
        self.filePushButton.setObjectName(_fromUtf8("filePushButton"))
        self.horizontalLayout_2.addWidget(self.filePushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.selectedFeaturesTreeWidget = QtGui.QTreeWidget(Dialog)
        self.selectedFeaturesTreeWidget.setObjectName(_fromUtf8("selectedFeaturesTreeWidget"))
        self.selectedFeaturesTreeWidget.header().setVisible(True)
        self.horizontalLayout_3.addWidget(self.selectedFeaturesTreeWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.selectAllButton = QtGui.QPushButton(Dialog)
        self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
        self.verticalLayout.addWidget(self.selectAllButton)
        self.selectOneButton = QtGui.QPushButton(Dialog)
        self.selectOneButton.setObjectName(_fromUtf8("selectOneButton"))
        self.verticalLayout.addWidget(self.selectOneButton)
        self.deselectOneButton = QtGui.QPushButton(Dialog)
        self.deselectOneButton.setObjectName(_fromUtf8("deselectOneButton"))
        self.verticalLayout.addWidget(self.deselectOneButton)
        self.deselectAllButton = QtGui.QPushButton(Dialog)
        self.deselectAllButton.setObjectName(_fromUtf8("deselectAllButton"))
        self.verticalLayout.addWidget(self.deselectAllButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.componentFeaturesTreeWidget = QtGui.QTreeWidget(Dialog)
        self.componentFeaturesTreeWidget.setObjectName(_fromUtf8("componentFeaturesTreeWidget"))
        self.horizontalLayout_3.addWidget(self.componentFeaturesTreeWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Create Complex Features", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.filePushButton.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Select the Complex Feature Class:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectedFeaturesTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "Selected Features", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAllButton.setText(QtGui.QApplication.translate("Dialog", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectOneButton.setText(QtGui.QApplication.translate("Dialog", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.deselectOneButton.setText(QtGui.QApplication.translate("Dialog", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.deselectAllButton.setText(QtGui.QApplication.translate("Dialog", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.componentFeaturesTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "Component Features", None, QtGui.QApplication.UnicodeUTF8))
