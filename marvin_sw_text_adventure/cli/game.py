from rich.console import Console
import typer

from marvin_sw_text_adventure.cli.common import verbose_callback
from marvin_sw_text_adventure.game import game as game_run

game_app = typer.Typer()


@game_app.callback()
def game(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
):
    "game cli"


@game_app.command()
def run(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
):
    from marvin_sw_text_adventure.console import console
    console.log("Starting game")
    game_run()
