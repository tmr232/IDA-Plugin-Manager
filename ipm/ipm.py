'''
ipm - IDA Plugin Manager

Usage:
    ipm initialize <ida-path>
    ipm terminate <ida-path>
    ipm add [--user|--system|--dir=<dir>] <name> <path>
    ipm remove [--user|--system|--dir=<dir>] <name>
    ipm list [--user|--system|--dir=<dir>]
'''
from ida_settings import IDASettings
import docopt
import shutil
import os


def main():
    arguments = docopt.docopt(__doc__)
    directory = arguments['--dir']
    settings = IDASettings('PluginLoader', directory=directory)

    if arguments['add']:
        plugin_path = arguments['<path>']
        plugin_name = arguments['<name>']

        if arguments['--user']:
            settings.user[plugin_name] = plugin_path

        elif arguments['--system']:
            settings.system[plugin_name] = plugin_path

        elif arguments['--dir']:
            settings.directory[plugin_name] = plugin_path

        else:
            settings.user[plugin_name] = plugin_path

    if arguments['remove']:
        plugin_name = arguments['<name>']

        if arguments['--user']:
            del settings.user[plugin_name]

        elif arguments['--system']:
            del settings.system[plugin_name]

        elif arguments['--dir']:
            del settings.directory[plugin_name]

        else:
            del settings.user[plugin_name]

    if arguments['list']:
        for name, path in settings.iteritems():
            print name, path

    if arguments['initialize']:
        # Copy `plugin_loader.py` to IDA's plugin directory.
        ida_path = arguments['<ida-path>']
        target_path = os.path.join(ida_path, 'plugins', 'plugin_loader.py')
        source_path = os.path.join(os.path.dirname(__file__), 'plugin_loader.py')
        print 'Installing the plugin loader to {}'.format(target_path)
        shutil.copyfile(source_path, target_path)

    if arguments['terminate']:
        # Remove `plugin_loader.py` from the IDA plugins directory.
        ida_path = arguments['<ida-path>']
        target_path = os.path.join(ida_path, 'plugins', 'plugin_loader.py')
        os.unlink(target_path)


if __name__ == '__main__':
    main()
