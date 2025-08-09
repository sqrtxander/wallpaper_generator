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
        s = min(
            self.camera.frame_height * 2 / np.sqrt(3),
            self.camera.frame_width,
        ) - 1

        points = [
            ORIGIN + s / 2 * LEFT + s * np.sqrt(3) / 4 * DOWN,
            ORIGIN + s / 2 * RIGHT + s * np.sqrt(3) / 4 * DOWN,
            ORIGIN + s * np.sqrt(3) / 4 * UP,
        ]

        self.add(Line(points[0], points[1], color=random.choice(CYBERDREAM)))
        self.add(Line(points[1], points[2], color=random.choice(CYBERDREAM)))
        self.add(Line(points[2], points[0], color=random.choice(CYBERDREAM)))

        self.sierpinsify(points)

    def sierpinsify(self, points):
        s = np.linalg.norm(points[0] - points[1])
        if s < 0.5:
            return

        midpoints = [
            midpoint(points[0], points[1]),
            midpoint(points[1], points[2]),
            midpoint(points[2], points[0]),
        ]

        self.add(Line(midpoints[0], midpoints[1], color=random.choice(CYBERDREAM)))
        self.add(Line(midpoints[1], midpoints[2], color=random.choice(CYBERDREAM)))
        self.add(Line(midpoints[2], midpoints[0], color=random.choice(CYBERDREAM)))

        self.sierpinsify([points[0], midpoints[0], midpoints[2]])
        self.sierpinsify([midpoints[0], points[1],  midpoints[1]])
        self.sierpinsify([midpoints[2], midpoints[1],  points[2]])


