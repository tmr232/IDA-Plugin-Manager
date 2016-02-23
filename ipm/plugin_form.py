# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\plugin_form.ui'
#
# Created: Tue Feb 23 15:48:52 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PluginDialog(object):
    def setupUi(self, PluginDialog):
        PluginDialog.setObjectName("PluginDialog")
        PluginDialog.resize(546, 210)
        self.formLayout_3 = QtGui.QFormLayout(PluginDialog)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtGui.QLabel(PluginDialog)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.nameLineEdit = QtGui.QLineEdit(PluginDialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_2 = QtGui.QLabel(PluginDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLineEdit = QtGui.QLineEdit(PluginDialog)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.browsePushButton = QtGui.QPushButton(PluginDialog)
        self.browsePushButton.setObjectName("browsePushButton")
        self.horizontalLayout.addWidget(self.browsePushButton)
        self.formLayout_3.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtGui.QLabel(PluginDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.groupBox = QtGui.QGroupBox(PluginDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.systemCheckBox = QtGui.QCheckBox(self.groupBox)
        self.systemCheckBox.setObjectName("systemCheckBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.systemCheckBox)
        self.userCheckBox = QtGui.QCheckBox(self.groupBox)
        self.userCheckBox.setObjectName("userCheckBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.userCheckBox)
        self.directoryCheckBox = QtGui.QCheckBox(self.groupBox)
        self.directoryCheckBox.setObjectName("directoryCheckBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.directoryCheckBox)
        self.idbCheckBox = QtGui.QCheckBox(self.groupBox)
        self.idbCheckBox.setObjectName("idbCheckBox")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.idbCheckBox)
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(PluginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(PluginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PluginDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PluginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginDialog)

    def browse(self):
        pass

    def retranslateUi(self, PluginDialog):
        PluginDialog.setWindowTitle(QtGui.QApplication.translate("PluginDialog", "IDA Plugin Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PluginDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PluginDialog", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.browsePushButton.setText(QtGui.QApplication.translate("PluginDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PluginDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.systemCheckBox.setText(QtGui.QApplication.translate("PluginDialog", "System", None, QtGui.QApplication.UnicodeUTF8))
        self.userCheckBox.setText(QtGui.QApplication.translate("PluginDialog", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.directoryCheckBox.setText(QtGui.QApplication.translate("PluginDialog", "Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.idbCheckBox.setText(QtGui.QApplication.translate("PluginDialog", "IDB", None, QtGui.QApplication.UnicodeUTF8))

