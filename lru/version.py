__version__ = '1.2.0'


def get_version():
    return __version__


def get_version_as_tuple():
    return tuple(map(int, __version__.split('.')))
