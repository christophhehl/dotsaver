from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TextArea


class DotsaverTui(App):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea()
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == '__main__':
    app = DotsaverTui()
    app.run()
