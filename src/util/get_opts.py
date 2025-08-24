import json


class Opts:
    def __init__(self, config_path):
        with open(config_path, "r") as f:
            dct = json.loads(f.read())

        self.BACKGROUND: str = dct["colors"]["background"]
        self.FOREGROUND: str = dct["colors"]["foreground"]
        self.PALETTE: list[str] = dct["colors"]["palette"]
        self.WIDTH: int = dct["dimensions"]["width"]
        self.HEIGHT: int = dct["dimensions"]["height"]
        self.SCALE: float = dct["dimensions"]["scale"]
