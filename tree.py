from manim import *
import random

CYBERDREAM = (
    # RGBA.from_hex("#16181a"),
    # RGBA.from_hex("#1e2124"),
    # RGBA.from_hex("#3c4048"),
    # RGBA.from_hex("#ffffff"),
    # RGBA.from_hex("#7b8496"),
    RGBA.from_hex("#5ea1ff"),
    RGBA.from_hex("#5eff6c"),
    RGBA.from_hex("#5ef1ff"),
    RGBA.from_hex("#ff6e5e"),
    RGBA.from_hex("#f1ff5e"),
    RGBA.from_hex("#ff5ef1"),
    RGBA.from_hex("#ff5ea0"),
    RGBA.from_hex("#ffbd5e"),
    RGBA.from_hex("#bd5eff"),
)
class MyTree(Scene):
    def construct(self):
        random.seed(42)
        # self.add(Line(ORIGIN - np.array([0, 2, 0]), ORIGIN, color=random.choice(CYBERDREAM)))
        self.tree_path(ORIGIN + 3.5 * DOWN + 1 * LEFT, 90 * DEGREES, 0)


    def tree_path(self, point, angle, depth):
        if depth > 10:
            return

        r = 2 * (0.75) ** depth
        p = np.array([
            point[0] + r * np.cos(angle),
            point[1] + r * np.sin(angle),
            0,
        ])
        self.add(Line(point, p, color=random.choice(CYBERDREAM)))

        self.tree_path(p, angle + 20 * DEGREES, depth + 1)
        self.tree_path(p, angle - 50 * DEGREES, depth + 1)

