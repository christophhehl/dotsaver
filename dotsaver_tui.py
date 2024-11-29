from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, HorizontalGroup, Center
from textual.widgets import Header, Footer, Collapsible, Button, Static, Label

from dotsaver import Software, Configuration

BANNER = r"""
 /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$|__  $$__//$$__  $$ /$$__  $$| $$   | $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$   | $$  | $$  \__/| $$  \ $$| $$   | $$| $$      | $$  \ $$
| $$  | $$| $$  | $$   | $$  |  $$$$$$ | $$$$$$$$|  $$ / $$/| $$$$$   | $$$$$$$/
| $$  | $$| $$  | $$   | $$   \____  $$| $$__  $$ \  $$ $$/ | $$__/   | $$__  $$
| $$  | $$| $$  | $$   | $$   /$$  \ $$| $$  | $$  \  $$$/  | $$      | $$  \ $$
| $$$$$$$/|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$   \  $/   | $$$$$$$$| $$  | $$
|_______/  \______/    |__/   \______/ |__/  |__/    \_/    |________/|__/  |__/
"""


class SoftwareWidget(Static):
    __name: str
    __software: Software

    def __lt__(self, other):
        return self.__name < other.__name

    def __init__(self, name):
        super().__init__()
        self.__name = name

    def compose(self) -> ComposeResult:
        with Collapsible(title=self.__name, collapsed=True):
            with HorizontalGroup():
                yield Label("Install_info: yay\nFolders: 5")
                yield Button("Edit Software", variant="primary", id="edit-software")
                yield Button("Remove Software", variant="error", id="remove-software")


class DotsaverTui(App):
    __config: Configuration
    __software_list = [SoftwareWidget("yay"), SoftwareWidget("rg"), SoftwareWidget("nvim")]
    CSS_PATH = "dotsaver_tui.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_software", "Add"),
    ]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            yield Label(BANNER)
        with VerticalScroll(id="software_list"):
            for i in sorted(self.__software_list):
                yield i
        yield Footer()

    def action_add_software(self) -> None:
        new_software = SoftwareWidget("new")
        self.__software_list.append(new_software)
        self.refresh(recompose=True)

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == '__main__':
    app = DotsaverTui()
    app.run()
