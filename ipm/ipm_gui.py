from collections import namedtuple

import idaapi
from ida_settings import IDASettings
import idc
from cute import QtWidgets, QtGui, QtCore, connect

idaapi.require('plugin_form')
import plugin_form


class PluginInfo(object):
    def __init__(self, name, path, system=False, user=False, directory=False, idb=False):
        self.name = name
        self.path = path
        self.system = system
        self.user = user
        self.directory = directory
        self.idb = idb

    def __repr__(self):
        return 'PluginInfo(name={}, path={}, system={}, user={}, directory={}, idb={})'.format(self.name,
                                                                                               self.path,
                                                                                               self.system,
                                                                                               self.user,
                                                                                               self.directory,
                                                                                               self.idb)

    @property
    def has_storage(self):
        return any((self.system, self.user, self.directory, self.idb, ))


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

        connect(self.browsePushButton, "clicked()", self.browse)

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
        path, selected_filter = QtWidgets.QFileDialog().getOpenFileName(self, 'Plugin Path', self.pathLineEdit.text(),
                                                                        filter='*.py')
        self.pathLineEdit.setText(path)


def ask_plugin(plugin_info=None):
    try:
        plugin_dialog = PluginDialog(plugin_info)
        plugin_dialog.setModal(True)
        result = plugin_dialog.exec_()
        if result:
            return plugin_dialog.plugin_info
        return None
    except:
        import traceback
        traceback.print_exc()
        raise


def write_plugin(plugin_info, settings):
    for storage_type in ('system', 'user', 'directory', 'idb'):
        if getattr(plugin_info, storage_type):
            try:
                getattr(settings, storage_type)[plugin_info.name] = plugin_info.path
            except:
                pass


class MyChoose2(idaapi.Choose2):
    def __init__(self, title, nb=5, flags=0, width=None, height=None, embedded=False, modal=False):
        self.settings = IDASettings('PluginLoader')
        idaapi.Choose2.__init__(
            self,
            title,
            [['Name', 10], ['Path', 50], ['S', 2], ['U', 2], ['D', 2], ['I', 2]],
            flags=flags,
            width=width,
            height=height,
            embedded=embedded)
        self.items = [[str(name),
                       str(path),
                       'x' if name in self.settings.system else '',
                       'x' if name in self.settings.user else '',
                       'x' if name in self.settings.directory else '',
                       'x' if name in self.settings.idb else '',
                       ] for name, path in self.settings.iteritems()]
        self.n = len(self.items)
        self.icon = -1
        self.selcount = 0
        self.modal = modal
        self.popup_names = ['Add', 'Remove', 'Edit', 'Refresh']

    def OnClose(self):
        print "closed", str(self)

    def OnEditLine(self, n):
        old_info = PluginInfo(*self.items[n])
        new_info = ask_plugin(old_info)
        print new_info.has_storage
        if not new_info.has_storage:
            print 'a'
            print idc.AskYN(False, 'This will remove the plugin from all storage. Continue?')

        if old_info != new_info:
            if new_info.name != old_info.name:
                print 'ignoring name changes for now...'

            for storage_type in ('system', 'user', 'directory', 'idb'):
                try:
                    if getattr(new_info, storage_type):
                        getattr(self.settings, storage_type)[old_info.name] = new_info.path
                    elif getattr(old_info, storage_type):
                        del getattr(self.settings, storage_type)[old_info.name]
                except:
                    print 'Failed on storage type %s'.format(storage_type)

        self.items[n] = self.make_line(new_info)

    def make_line(self, plugin_info):
        return [str(plugin_info.name),
                str(plugin_info.path),
                'x' if plugin_info.system else '',
                'x' if plugin_info.user else '',
                'x' if plugin_info.directory else '',
                'x' if plugin_info.idb else '',
                ]

    def OnInsertLine(self):
        plugin_info = ask_plugin()
        write_plugin(plugin_info, self.settings)
        self.n += 1
        self.items.append(self.make_line(plugin_info))

    def OnSelectLine(self, n):
        # self.selcount += 1
        Warning("[%02d] selectline '%s'" % (self.selcount, n))

    def OnGetLine(self, n):
        print("getline %d" % n)
        return self.items[n]

    def OnGetSize(self):
        n = len(self.items)
        print("getsize -> %d" % n)
        return n

    def OnDeleteLine(self, n):
        plugin_info = PluginInfo(*self.items[n])
        for storage_type in ('system', 'user', 'directory', 'idb'):
                try:
                    if getattr(plugin_info, storage_type):
                        del getattr(self.settings, storage_type)[plugin_info.name]
                except:
                    print 'Failed on storage type %s'.format(storage_type)
        print("del %d " % n)
        del self.items[n]
        return n

    def OnRefresh(self, n):
        print("refresh %d" % n)
        return n

    def OnCommand(self, n, cmd_id):
        if cmd_id == self.cmd_a:
            print "command A selected @", n
        elif cmd_id == self.cmd_b:
            print "command B selected @", n
        else:
            print "Unknown command:", cmd_id, "@", n
        return 1

    def OnGetIcon(self, n):
        r = self.items[n]
        t = self.icon + r[1].count("*")
        print "geticon", n, t
        return t

    def show(self):
        t = self.Show(self.modal)
        if t < 0:
            return False
        if not self.modal:
            self.cmd_a = self.AddCommand("command A")
            self.cmd_b = self.AddCommand("command B")
        print("Show() returned: %d\n" % t)
        return True

    def OnGetLineAttr(self, n):
        print("getlineattr %d" % n)
        # if n == 1:
        #     return [0xFF0000, 0]


y = MyChoose2("bla bla")
y.Show()
