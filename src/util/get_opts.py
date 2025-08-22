import json
import os

_PATH = os.path.join(os.path.dirname(__file__), "../../config.json")

with open(_PATH, "r") as f:
    _dct = json.loads(f.read())

BACKGROUND: str = _dct["colors"]["background"]
FOREGROUND: str = _dct["colors"]["foreground"]
PALETTE: list[str] = _dct["colors"]["palette"]
WIDTH: int = _dct["dimensions"]["width"]
HEIGHT: int = _dct["dimensions"]["height"]
SCALE: float = _dct["dimensions"]["scale"]
