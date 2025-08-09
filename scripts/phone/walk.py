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
class MyWalk(Scene):
    def construct(self):
        random.seed(0)
        walls = get_walls()
        for (x1, y1), (x2, y2) in walls:
            self.add(Line((x1-1.5, y1-3.5, 0), (x2-1.5, y2-3.5, 0), color=random.choice(CYBERDREAM)))
        for x in range(4):
            for y in range(8):
                self.add(Dot(color=WHITE, radius=0.075).move_to(np.array([x-1.5, y-3.5, 0])))

def get_walls():
    def rec(x, y):
        seen.add((x, y))
        neighbours = [(nx, ny) for nx, ny in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ) if 0 <= nx < 3 and 0 <= ny < 7 and (nx, ny) not in seen]

        random.shuffle(neighbours)
        for nx, ny in neighbours:
            if (nx, ny) in seen:
                continue
            print(x, y, nx, ny)
            if nx == x:
                walls.remove(((x, max(y, ny)), (x + 1, max(y, ny))))
                print("removing:", (x, max(y, ny)), (x + 1, max(y, ny)))
            if ny == y:
                walls.remove(((max(x, nx), y), (max(x, nx), y + 1)))
                print("removing:", (max(x, nx), y), (max(x, nx), y + 1))
            rec(nx, ny)

    walls = set()
    for x in range(4):
        for y in range(8):
            if x < 3:
                walls.add(((x, y), (x + 1, y)))
            if y < 7:
                walls.add(((x, y), (x ,y + 1)))
    seen = set()
    rec(0, 0)
    return walls


