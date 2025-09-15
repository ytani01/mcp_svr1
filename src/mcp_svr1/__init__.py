#
# (c) Yoichi Tanibayashi
#
from importlib.metadata import version as get_version_from_metadata

# __package__ が定義されている場合（通常はパッケージ実行時）、
# importlib.metadata でバージョンを取得します。
if __package__:
    __version__ = get_version_from_metadata(__package__)
# 定義されていない場合（スクリプト直接実行時など）、
# 仮バージョンを設定します。
else:
    __version__ = "_._._"


__all__ = [
     "__version__"
 ]
