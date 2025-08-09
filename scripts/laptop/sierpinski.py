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
class MySierpinski(Scene):
    def construct(self):
        random.seed(42)
        s = 8
        points = [
            ORIGIN + s / 2 * LEFT + s / 3 * DOWN + DOWN,
            ORIGIN + s / 2 * RIGHT + s / 3 * DOWN + DOWN,
            ORIGIN + np.sqrt(3) * s / 2 * UP + s / 3 * DOWN + DOWN,
        ]

        self.add(Line(points[0], points[1], color=random.choice(CYBERDREAM)))
        self.add(Line(points[1], points[2], color=random.choice(CYBERDREAM)))
        self.add(Line(points[2], points[0], color=random.choice(CYBERDREAM)))

        self.sierpinsify(points, 0)

    def sierpinsify(self, points, depth):
        if depth > 4:
            return

        midpoints = [
            midpoint(points[0], points[1]),
            midpoint(points[1], points[2]),
            midpoint(points[2], points[0]),
        ]

        self.add(Line(midpoints[0], midpoints[1], color=random.choice(CYBERDREAM)))
        self.add(Line(midpoints[1], midpoints[2], color=random.choice(CYBERDREAM)))
        self.add(Line(midpoints[2], midpoints[0], color=random.choice(CYBERDREAM)))

        self.sierpinsify([points[0], midpoints[0], midpoints[2]], depth + 1)
        self.sierpinsify([midpoints[0], points[1],  midpoints[1]], depth + 1)
        self.sierpinsify([midpoints[2], midpoints[1],  points[2]], depth + 1)


