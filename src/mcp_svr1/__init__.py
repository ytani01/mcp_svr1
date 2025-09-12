#
# (c) Yoichi Tanibayashi
#
from importlib.metadata import version as get_version_from_metadata

if __package__:
    __version__ = get_version_from_metadata(__package__)
else:
    __version__ = "_._._"


__all__ = [
     "__version__"
 ]
