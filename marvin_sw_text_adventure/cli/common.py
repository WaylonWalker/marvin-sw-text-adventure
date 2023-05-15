from marvin_sw_text_adventure.console import console


def verbose_callback(value: bool) -> None:
    if value:
        console.quiet = False
