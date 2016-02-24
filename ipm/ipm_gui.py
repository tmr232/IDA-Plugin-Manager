from collections import namedtuple

import idaapi
from ida_settings import IDASettings
import idc
from cute import QtWidgets, QtGui, QtCore, connect

import plugin_form
import main_form

PluginInfo = namedtuple('PluginInfo', 'name path system user directory idb')

def checked(state):
    if state:
        return QtCore.Qt.Checked
    return QtCore.Qt.Unchecked


class PluginTable(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        super(PluginTable, self).__init__(*args, **kwargs)

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(['Name', 'Path', 'System', 'User', 'Directory', 'IDB'])

    def add_row(self, plugin_info):
        row_index = self.rowCount()
        self.insertRow(row_index)

        self.setItem(row_index, 0, QtWidgets.QTableWidgetItem(plugin_info.name))
        self.setItem(row_index, 1, QtWidgets.QTableWidgetItem(plugin_info.path))
        self.setCellWidget(row_index, 2, QtWidgets.QCheckBox())
        self.setCellWidget(row_index, 3, QtWidgets.QCheckBox())
        self.setCellWidget(row_index, 4, QtWidgets.QCheckBox())
        self.setCellWidget(row_index, 5, QtWidgets.QCheckBox())

class PluginForm(QtWidgets.QWidget):
    def __init__(self):
        super(PluginForm, self).__init__()

        self.table = PluginTable(self)
        self.table.setGeometry(0, 0, 200, 200)
        self.table.add_row(PluginInfo('Autoshit', 'c:/autoshit', True, True, False, False))

# a = PluginTable()
# a.add_row(PluginInfo('Autoshit', 'c:/autoshit', True, True, False, False))
# a.show()


# class MyMain(QtWidgets.QWidget, main_form.Ui_Form):
#     def __init__(self):
#         super(MyMain, self).__init__()
#         self.setupUi(self)
#
#         row = self.tableWidget.rowCount()
#         self.tableWidget.insertRow(row)
#         self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem("wtf"))
#         self.tableWidget.setCellWidget(row, 1, QtWidgets.QCheckBox())
#         row = self.tableWidget.rowCount()
#         self.tableWidget.insertRow(row)
#         self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem("wtf"))
#         self.tableWidget.setHorizontalHeaderLabels(['Name', 'Path', 'System', 'User', 'Directory', 'IDB'])
#
#         connect(self.tableWidget, 'cellDoubleClicked(int, int)', self.cellDoubleClicked)
#
#     def cellDoubleClicked(self, row, column):
#         print "AAA"
#
#
# a  = MyMain()
# a.show()


class PluginDialog(QtWidgets.QDialog, plugin_form.Ui_PluginDialog):
    def __init__(self, plugin_info=None):
        super(PluginDialog, self).__init__()
        self.setupUi(self)


        QtCore.QObject.connect(self.browsePushButton, QtCore.SIGNAL("clicked()"), self.browse)


        self.plugin_info = plugin_info

        if plugin_info:
            self.nameLineEdit.setText(plugin_info.name)
            self.pathLineEdit.setText(plugin_info.path)
            self.systemCheckBox.setCheckState(checked(plugin_info.system))
            self.userCheckBox.setCheckState(checked(plugin_info.user))
            self.directoryCheckBox.setCheckState(checked(plugin_info.directory))
            self.idbCheckBox.setCheckState(checked(plugin_info.idb))

    def accept(self, *args, **kwargs):
        self.plugin_info = PluginInfo(self.nameLineEdit.text(),
                                      self.pathLineEdit.text(),
                                      self.systemCheckBox.isChecked(),
                                      self.userCheckBox.isChecked(),
                                      self.directoryCheckBox.isChecked(),
                                      self.idbCheckBox.isChecked())
        super(PluginDialog, self).accept(*args, **kwargs)

    def browse(self):
        path, selected_filter = QtWidgets.QFileDialog().getOpenFileName(self, 'Plugin Path', self.pathLineEdit.text(), filter='*.py')
        self.pathLineEdit.setText(path)


def ask_plugin(plugin_info=None):
    plugin_dialog = PluginDialog(plugin_info)
    plugin_dialog.setModal(True)
    result = plugin_dialog.exec_()
    if result:
        return plugin_dialog.plugin_info
    return None


def write_plugin(plugin_info, settings):
    for storage_type in ('system', 'user', 'directory', 'idb'):
        if getattr(plugin_info, storage_type):
            try:
                getattr(settings, storage_type)[plugin_info.name] = plugin_info.path
            except:
                pass

