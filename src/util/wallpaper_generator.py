import os
import util.get_opts as opts


class WallpaperGenerator:
    def __init__(self):
        self.out_dir: str = os.path.join(os.path.dirname(__file__), "../../output/")
        self.LINE_WIDTH: int = int(8 * opts.SCALE)
        self.CIRCLE_RADIUS: int = int(12 * opts.SCALE)

    def generate(self):
        ...

