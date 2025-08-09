from manim import *
import random
import util.get_options as opts


config.background_color = opts.BACKGROUND
config.pixel_width = opts.WIDTH
config.pixel_height = opts.HEIGHT


class Sierpinski(Scene):
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

        self.add(Line(points[0], points[1], color=random.choice(opts.PALETTE)))
        self.add(Line(points[1], points[2], color=random.choice(opts.PALETTE)))
        self.add(Line(points[2], points[0], color=random.choice(opts.PALETTE)))

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

        self.add(Line(midpoints[0], midpoints[1], color=random.choice(opts.PALETTE)))
        self.add(Line(midpoints[1], midpoints[2], color=random.choice(opts.PALETTE)))
        self.add(Line(midpoints[2], midpoints[0], color=random.choice(opts.PALETTE)))

        self.sierpinsify([points[0], midpoints[0], midpoints[2]])
        self.sierpinsify([midpoints[0], points[1],  midpoints[1]])
        self.sierpinsify([midpoints[2], midpoints[1],  points[2]])


