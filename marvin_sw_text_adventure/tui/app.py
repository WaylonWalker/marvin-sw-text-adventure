from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.css.query import NoMatches
from textual.widgets import Footer, Static

from marvin_sw_text_adventure.config import config

config["tui"] = {}
config["tui"]["bindings"] = {}


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield Container(
            Static("sidebar"),
            id="sidebar",
        )


class Tui(App):
    """A Textual app to manage requests."""

    CSS_PATH = Path("__file__").parent / "app.css"
    BINDINGS = [tuple(b.values()) for b in config["tui"]["bindings"]]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Container(Static("hello world"))
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_toggle_sidebar(self):
        try:
            self.query_one("PromptSidebar").remove()
        except NoMatches:
            self.mount(Sidebar())


def run_app():
    import os
    import sys

    from textual.features import parse_features

    dev = "--dev" in sys.argv
    features = set(parse_features(os.environ.get("TEXTUAL", "")))
    if dev:
        features.add("debug")
        features.add("devtools")

    os.environ["TEXTUAL"] = ",".join(sorted(features))
    app = Tui()
    app.run()


if __name__ == "__main__":
    run_app()
