from manim import *
import random
import get_colors as colors


config.background_color = colors.BACKGROUND


class MyWalk(Scene):
    def construct(self):
        width = int(self.camera.frame_width + 0.5)
        height = int(self.camera.frame_height + 0.5)

        walls = get_walls(width, height)
        for (x1, y1), (x2, y2) in walls:
            self.add(Line(
                (x1 - width / 2 + 0.5, y1 - height / 2 + 0.5, 0),
                (x2 - width / 2 + 0.5, y2 - height / 2 + 0.5, 0),
                color=random.choice(colors.PALETTE)
            ))
        for x in range(width):
            for y in range(height):
                self.add(Dot(color=colors.FOREGROUND, radius=0.075).move_to(np.array([x - width / 2 + 0.5, y - height / 2 + 0.5, 0])))

def get_walls(width, height):
    def rec(x, y):
        seen.add((x, y))
        neighbours = [(nx, ny) for nx, ny in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ) if 0 <= nx < width - 1 and 0 <= ny < height - 1 and (nx, ny) not in seen]

        random.shuffle(neighbours)
        for nx, ny in neighbours:
            if (nx, ny) in seen:
                continue
            if nx == x:
                walls.remove(((x, max(y, ny)), (x + 1, max(y, ny))))
            if ny == y:
                walls.remove(((max(x, nx), y), (max(x, nx), y + 1)))
            rec(nx, ny)

    walls = set()
    for x in range(width):
        for y in range(height):
            if x < width - 1:
                walls.add(((x, y), (x + 1, y)))
            if y < height - 1:
                walls.add(((x, y), (x ,y + 1)))
    seen = set()
    rec(0, 0)
    return walls


