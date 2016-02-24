# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\plugin_form.ui'
#
# Created: Tue Feb 23 15:48:52 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
from cute import QtCore, QtGui, QtWidgets, connect


class Ui_PluginDialog(object):
    def setupUi(self, PluginDialog):
        PluginDialog.setObjectName("PluginDialog")
        PluginDialog.resize(546, 210)
        self.formLayout_3 = QtWidgets.QFormLayout(PluginDialog)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(PluginDialog)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameLineEdit = QtWidgets.QLineEdit(PluginDialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_2 = QtWidgets.QLabel(PluginDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLineEdit = QtWidgets.QLineEdit(PluginDialog)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.browsePushButton = QtWidgets.QPushButton(PluginDialog)
        self.browsePushButton.setObjectName("browsePushButton")
        self.horizontalLayout.addWidget(self.browsePushButton)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(PluginDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.groupBox = QtWidgets.QGroupBox(PluginDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.systemCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.systemCheckBox.setObjectName("systemCheckBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.systemCheckBox)
        self.userCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.userCheckBox.setObjectName("userCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.userCheckBox)
        self.directoryCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.directoryCheckBox.setObjectName("directoryCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.directoryCheckBox)
        self.idbCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.idbCheckBox.setObjectName("idbCheckBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.idbCheckBox)
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(PluginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(PluginDialog)
        connect(self.buttonBox, "accepted()", PluginDialog.accept)
        connect(self.buttonBox, "rejected()", PluginDialog.reject)

    def browse(self):
        pass

    def retranslateUi(self, PluginDialog):
        PluginDialog.setWindowTitle("IDA Plugin Manager")
        self.label.setText("Name")
        self.label_2.setText("Path")
        self.browsePushButton.setText("Browse")
        self.label_3.setText("Settings")
        self.systemCheckBox.setText("System")
        self.userCheckBox.setText("User")
        self.directoryCheckBox.setText("Directory")
        self.idbCheckBox.setText("IDB")

