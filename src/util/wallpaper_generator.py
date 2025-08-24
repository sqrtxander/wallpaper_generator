from util.get_opts import Opts


class WallpaperGenerator:
    def __init__(self, out_path: str, config_path: str):
        self.out_path: str = out_path
        self.opts = Opts(config_path)
        self.LINE_WIDTH: int = int(8 * self.opts.SCALE)
        self.CIRCLE_RADIUS: int = int(12 * self.opts.SCALE)
        self.SCREEN_SCALE: float = 150 * self.opts.SCALE


    def generate(self):
        ...

