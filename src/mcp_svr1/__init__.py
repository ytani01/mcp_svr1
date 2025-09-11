#
# (c) Yoichi Tanibayashi
#
from importlib.metadata import version

if __package__:
    __version__ = version(__package__)
else:
    __version__ = "_._._"


__all__ = [
     "__version__"
 ]
