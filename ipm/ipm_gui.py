import idaapi
from ida_settings import IDASettings
import idc

idc.form()

class MyChoose2(idaapi.Choose2):

    def __init__(self, title, nb = 5, flags=0, width=None, height=None, embedded=False, modal=False):
        self.settings = IDASettings('PluginLoader')
        idaapi.Choose2.__init__(
            self,
            title,
            [ ['Name', 10], ['Path', 50], ['I', 2], ['D', 2], ['U', 2], ['S', 2]],
            flags = flags,
            width = width,
            height = height,
            embedded = embedded)
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