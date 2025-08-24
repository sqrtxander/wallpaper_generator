import util.get_opts as opts


class WallpaperGenerator:
    def __init__(self, out_path: str):
        self.out_path: str = out_path
        self.LINE_WIDTH: int = int(8 * opts.SCALE)
        self.CIRCLE_RADIUS: int = int(12 * opts.SCALE)
        self.SCREEN_SCALE: float = 150 * opts.SCALE

    def generate(self):
        ...

