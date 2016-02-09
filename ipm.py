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
        ida_path = arguments['<ida-path>']
        # Copy `plugin_loader.py` to IDA directory.

    if arguments['terminate']:
        # Remove `plugin_loader.py` from IDA directory.
        pass


if __name__ == '__main__':
    main()
