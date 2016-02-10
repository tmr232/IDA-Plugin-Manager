import idaapi
import ida_settings


def message(*messages):
    for msg in messages:
        for line in msg.splitlines():
            idaapi.msg("[PluginLoaderEx] {}\n".format(line))


class PluginLoaderEx(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "Plugin Loader"
    help = "Plugin Loader"
    wanted_name = "PluginLoader"
    wanted_hotkey = ""

    def init(self):
        settings = ida_settings.IDASettings("PluginLoader")
        message("Loading settings from IDASettings('PluginLoader')")


        for name, path in settings.iteritems():
            message('Loading {} from {}'.format(name, path))
            idaapi.load_plugin(plugin)

        return idaapi.PLUGIN_SKIP

    def term(self):
        pass

    def run(self, arg):
        pass


def PLUGIN_ENTRY():
    return PluginLoaderEx()
