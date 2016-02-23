from collections import namedtuple

import idaapi
from ida_settings import IDASettings
import idc
from cute import QtWidgets, QtGui, QtCore

import plugin_form

PluginInfo = namedtuple('PluginInfo', 'name path system user directory idb')


def checked(state):
    if state:
        return QtCore.Qt.Checked
    return QtCore.Qt.Unchecked


class MyDialog(QtWidgets.QDialog, plugin_form.Ui_PluginDialog):
    def __init__(self, plugin_info):
        super(MyDialog, self).__init__()
        self.setupUi(self)

        self.plugin_info = plugin_info

        QtCore.QObject.connect(self.browsePushButton, QtCore.SIGNAL("clicked()"), self.browse)


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
        write_plugin(self.plugin_info, IDASettings('PluginLoader'))
        super(MyDialog, self).accept(*args, **kwargs)

    def browse(self):
        path, selected_filter = QtWidgets.QFileDialog().getOpenFileName(self, 'Plugin Path', self.pathLineEdit.text(), filter='*.py')
        self.pathLineEdit.setText(path)


a = MyDialog(PluginInfo('name', 'path', True, True, True, True))
a.setModal(True)
a.show()


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
            [['Name', 10], ['Path', 50], ['I', 2], ['D', 2], ['U', 2], ['S', 2]],
            flags=flags,
            width=width,
            height=height,
            embedded=embedded)
        self.n = 0
        self.items = [[name,
                       path,
                       'x' if name in self.settings.idb else '',
                       'x' if name in self.settings.directory else '',
                       'x' if name in self.settings.user else '',
                       'x' if name in self.settings.system else ''] for name, path in self.settings.iteritems()]
        self.icon = 5
        self.selcount = 0
        self.modal = modal
        self.popup_names = ['Add', 'Remove', 'Edit', 'Refresh']

        print("created %s" % str(self))

    def OnClose(self):
        print "closed", str(self)

    def OnEditLine(self, n):
        self.items[n][1] = self.items[n][1] + "*"
        print("editing %d" % n)

    def OnInsertLine(self):
        self.items.append(self.make_item())
        print("insert line")

    def OnSelectLine(self, n):
        self.selcount += 1
        Warning("[%02d] selectline '%s'" % (self.selcount, n))

    def OnGetLine(self, n):
        print("getline %d" % n)
        return self.items[n]

    def OnGetSize(self):
        n = len(self.items)
        print("getsize -> %d" % n)
        return n

    def OnDeleteLine(self, n):
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
        if n == 1:
            return [0xFF0000, 0]


y = MyChoose2("bla bla")
y.Show()
