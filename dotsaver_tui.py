from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, HorizontalGroup, Center
from textual.widgets import Header, Footer, Collapsible, Button, Static, Label


class SoftwareWidget(Static):
    __name: str

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
    CSS_PATH = "dotsaver_tui.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_software", "Add"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with Center():
            yield Label(r"""
 /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$|__  $$__//$$__  $$ /$$__  $$| $$   | $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$   | $$  | $$  \__/| $$  \ $$| $$   | $$| $$      | $$  \ $$
| $$  | $$| $$  | $$   | $$  |  $$$$$$ | $$$$$$$$|  $$ / $$/| $$$$$   | $$$$$$$/
| $$  | $$| $$  | $$   | $$   \____  $$| $$__  $$ \  $$ $$/ | $$__/   | $$__  $$
| $$  | $$| $$  | $$   | $$   /$$  \ $$| $$  | $$  \  $$$/  | $$      | $$  \ $$
| $$$$$$$/|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$   \  $/   | $$$$$$$$| $$  | $$
|_______/  \______/    |__/   \______/ |__/  |__/    \_/    |________/|__/  |__/
                """)
        with VerticalScroll(id="software_list"):
            for i in sorted(["yay", "rg", "nvim"]):
                yield SoftwareWidget(i)

    def action_add_software(self) -> None:
        new_software = SoftwareWidget()
        self.query_one("#software_list").mount(new_software)
        new_software.scroll_visible()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == '__main__':
    app = DotsaverTui()
    app.run()
