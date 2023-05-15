import typer

from marvin_sw_text_adventure.cli.common import verbose_callback
from marvin_sw_text_adventure.console import console
from marvin_sw_text_adventure.cli.game import game_app
# from marvin_sw_text_adventure.cli.config import config_app
# from marvin_sw_text_adventure.cli.tui import tui_app

app = typer.Typer(
    name="marvin_sw_text_adventure",
    help="a text adventure game leveraging @askmarvinai",
)
app.add_typer(game_app)
# app.add_typer(config_app)
# app.add_typer(tui_app)


def version_callback(value: bool) -> None:
    """Callback function to print the version of the marvin-sw-text-adventure package.

    Args:
        value (bool): Boolean value to determine if the version should be printed.

    Raises:
        typer.Exit: If the value is True, the version will be printed and the program will exit.

    Example:
        version_callback(True)
    """
    if value:
        from marvin_sw_text_adventure.__about__ import __version__

        typer.echo(f"{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
    ),
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
) -> None:
    return


if __name__ == "__main__":
    typer.run(main)
