import json
import os

_PATH = os.path.join(os.path.dirname(__file__), "../../config.json")

with open(_PATH, "r") as f:
    _dct = json.loads(f.read())

BACKGROUND = _dct["colors"]["background"]
FOREGROUND = _dct["colors"]["foreground"]
PALETTE = _dct["colors"]["palette"]
WIDTH = _dct["dimensions"]["width"]
HEIGHT = _dct["dimensions"]["height"]
SCALE = _dct["dimensions"]["scale"]
