import json
import os

_COLORSCHEME_PATH = os.path.join(os.path.dirname(__file__), "../colorscheme.json")

with open(_COLORSCHEME_PATH, "r") as f:
    _dct = json.loads(f.read())

BACKGROUND = _dct["background"]
FOREGROUND = _dct["foreground"]
PALETTE = _dct["palette"]
