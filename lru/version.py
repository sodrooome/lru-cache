__version__ = '1.0.2'


def get_version():
    return __version__


def get_version_as_tuple():
    return tuple(map(int, __version__.split('.')))
