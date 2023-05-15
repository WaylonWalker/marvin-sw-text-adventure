import typer

from marvin_sw_text_adventure.cli.common import verbose_callback
from marvin_sw_text_adventure.tui.app import run_app

tui_app = typer.Typer()


@tui_app.callback(invoke_without_command=True)
def i(
    verbose: bool = typer.Option(
        False,
        callback=verbose_callback,
        help="show the log messages",
    ),
):
    "interactive tui"
    run_app()
