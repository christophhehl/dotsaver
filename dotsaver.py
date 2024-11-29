from pathlib import Path


class Software:
    __name: str
    __install_info: str
    __is_custom_install: bool
    __config_folders: list[Path]

    def __init__(self, name: str):
        self.set_name(name)
        self.set_install_info("")
        self.set_is_custom_install(False)
        self.__config_folders = []

    def set_name(self, name: str):
        if name == "":
            raise ValueError("Name cannot be empty!")
        self.__name = name

    def get_name(self):
        return self.__name

    def set_install_info(self, info: str):
        if info == "":
            raise ValueError("Install info cannot be empty!")
        self.__install_info = info

    def get_install_info(self):
        return self.__install_info

    def set_is_custom_install(self, is_custom_install: bool):
        self.__is_custom_install = is_custom_install

    def get_is_custom_install(self):
        return self.__is_custom_install

    def add_config_folder(self, config_folder: Path):
        if config_folder in self.__config_folders:
            raise ValueError("Config folder already exists!")
        self.__config_folders.append(config_folder)

    def get_config_folders(self):
        return self.__config_folders


class Configuration:
    __git_link: Path
    __software_list: list[Software]

    def __init__(self, git_link: str):
        self.__git_link = Path(git_link)
        self.__software_list = []

    def set_git_link(self, git_link: str):
        if git_link == "":
            raise ValueError("Git link cannot be empty!")
        self.__git_link = Path(git_link)

    def get_git_link(self):
        return self.__git_link

    def add_software(self, software_name: str):
        self.__software_list.append(Software(software_name))

    def get_software_list(self):
        return self.__software_list
