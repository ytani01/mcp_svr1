#
# (c) 2025 Yoichi Tanibayashi
#
"""
# 典型的な使用方法

## __init__.py
```python
from importlib.metadata import version
from .utils.click_utils import click_common_ops
from .utils.my_logger import get_logger

if __package__:
    __version__ = version(__package__)
else:
    __version__ = "_._._"

__all__ = [
    "__version__",
    "click_common_opts",
    "get_logger",
]
```

## __main__.py
```python
from . import click_common_ops

@click.group()
@click.option("--opt0", ...)
@click_common_opts(__version__)
def cli(ctx, debug):
    __log = get_logger(cmd_name, debug)
    __log.debug("cmd_name=%s", ctx.info_name)

    if subcmd_name is None:
        print(ctx.get_help())

@cli.command()
@click.argument("arg1", ...)
@click.option("--opt1", ...)
@click_common_opts(__version__)
def cmd1(ctx, debug):
    __log = get_logger(__name__, debug)
    __log.debug("cmd_name=%s, ctx.command.name)
```


"""
import click


def click_common_opts(
    ver_str: str = "_._._",
    use_h: bool = True,
    use_d: bool = True,
    use_v: bool = True,
):
    """共通オプションをまとめたメタデコレータ"""

    def _decorator(func):
        decorators = []

        # version option
        ver_opts = ["--version", "-V"]
        if use_v:
            ver_opts.append("-v")
        decorators.append(
            click.version_option(
                ver_str, *ver_opts, message="%(prog)s %(version)s"
            )
        )

        # debug option
        debug_opts = ["--debug"]
        if use_d:
            debug_opts.append("-d")
        decorators.append(
            click.option(*debug_opts, is_flag=True, help="debug flag")
        )

        # help option
        help_opts = ["--help"]
        if use_h:
            help_opts.append("-h")
        decorators.append(click.help_option(*help_opts))

        # decorators をまとめて適用
        for dec in reversed(decorators):
            func = dec(func)

        # context を最後に wrap
        return click.pass_context(func)

    return _decorator
