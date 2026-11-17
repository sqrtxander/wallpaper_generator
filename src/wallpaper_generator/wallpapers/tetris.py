import random
from PIL import Image, ImageDraw
from typing import TypeAlias, override
from wallpaper_generator import WallpaperGenerator, generate_wallpaper

Coord: TypeAlias = tuple[int, int]
Tetromino: TypeAlias = tuple[Coord, Coord, Coord, Coord]

TETROMINOS: list[Tetromino] = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # I
    ((0, 0), (1, 0), (0, 1), (1, 1)),  # O
    ((0, 0), (1, 0), (2, 0), (1, 1)),  # T
    ((0, 0), (1, 0), (2, 0), (2, 1)),  # L
    ((0, 0), (1, 0), (2, 0), (0, 1)),  # J
    ((0, 0), (1, 0), (1, 1), (2, 1)),  # S
    ((0, 1), (1, 1), (1, 0), (2, 0)),  # Z
]


class Tetris(WallpaperGenerator):
    @override
    def generate(self):
        img = Image.new(
            "RGB",
            (self.opts.WIDTH, self.opts.HEIGHT),
            self.opts.BACKGROUND,
        )
        draw = ImageDraw.Draw(img)
        # can't use integer division because SCREEN_SCALE can be a float
        rows = int(self.opts.HEIGHT / self.SCREEN_SCALE)
        cols = int(self.opts.WIDTH / self.SCREEN_SCALE)

        def point_to_coord(p: Coord) -> Coord:
            x, y = p
            mx, my = self.opts.WIDTH / 2, self.opts.HEIGHT / 2
            return (
                int(mx + (x - cols / 2) * self.SCREEN_SCALE),
                int(my + (y - rows / 2) * self.SCREEN_SCALE),
            )

        tetrominos = self.getTetris(cols, rows)

        for t, color in tetrominos:
            outline = get_tetromino_outline(t)
            coords = [point_to_coord(p) for p in outline]
            coords_closed = coords + [coords[0]]
            draw.polygon(coords, fill=color)

            gap = self.LINE_WIDTH
            for (x1, y1), (x2, y2) in zip(coords_closed, coords_closed[1:]):
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1
                draw.rectangle(
                    (x1 - gap, y1 - gap, x2 + gap, y2 + gap),
                    fill=self.opts.BACKGROUND,
                    width=self.LINE_WIDTH * 2,
                )

        img.save(self.out_path)

    def getTetris(self, cols: int, rows: int) -> set[tuple[Tetromino, str]]:
        def get_rotations(shape: Tetromino) -> list[Tetromino]:
            rotations: list[Tetromino] = [shape]
            current = shape
            for _ in range(3):
                rotated = [(-y, x) for x, y in current]
                current = (rotated[0], rotated[1], rotated[2], rotated[3])
                rotations.append(current)
            return rotations

        # Generate all rotations and normalize them
        colors = self.opts.PALETTE.copy()
        random.shuffle(colors)
        normalized_shapes: list[tuple[Tetromino, str]] = []
        for t in TETROMINOS:
            color = colors.pop()
            for rot in get_rotations(t):
                min_x = min(sx for sx, _ in rot)
                min_y = min(sy for _, sy in rot)
                normalized = [(sx - min_x, sy - min_y) for sx, sy in rot]
                normalized_shapes.append(
                    (
                        (
                            normalized[0],
                            normalized[1],
                            normalized[2],
                            normalized[3],
                        ),
                        color,
                    )
                )

        def find_empty_cell(occupied: set[Coord]) -> Coord | None:
            for y in range(rows - 1, -1, -1):
                for x in range(cols):
                    if (x, y) not in occupied:
                        return (x, y)
            return None

        def can_fill_tetromino(
            occupied: set[Coord], target: Coord
        ) -> list[tuple[Tetromino, str]]:
            valid_placements: list[tuple[Tetromino, str]] = []

            for shape, color in normalized_shapes:
                # Calculate actual bounds of this shape
                max_sx = max(sx for sx, _ in shape)
                max_sy = max(sy for _, sy in shape)

                # Only try offsets that make sense for this shape
                for dx in range(-max_sx, 1):
                    for dy in range(-max_sy, 1):
                        placed = tuple(
                            (target[0] + dx + sx, target[1] + dy + sy)
                            for sx, sy in shape
                        )

                        # Check if target is covered and placement is valid
                        if target in placed and all(
                            0 <= px < cols
                            and 0 <= py < rows
                            and (px, py) not in occupied
                            for px, py in placed
                        ):
                            valid_placements.append(
                                ((placed[0], placed[1], placed[2], placed[3]), color)
                            )

            return valid_placements

        def has_small_hole(occupied: set[Coord]) -> bool:
            empty_cells = {
                (x, y)
                for x in range(cols)
                for y in range(rows)
                if (x, y) not in occupied
            }

            if not empty_cells:
                return False

            # Find connected components of empty cells
            def get_region(start: Coord) -> set[Coord]:
                region = {start}
                stack = [start]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if (nx, ny) in empty_cells and (nx, ny) not in region:
                            region.add((nx, ny))
                            stack.append((nx, ny))
                return region

            visited: set[Coord] = set()
            for cell in empty_cells:
                if cell not in visited:
                    region = get_region(cell)
                    visited.update(region)
                    if 1 <= len(region) <= 3:
                        return True

            return False

        def solve(
            occupied: set[Coord], result: list[tuple[Tetromino, str]], depth: int = 0
        ) -> bool:
            if depth > 50:
                return False

            target = find_empty_cell(occupied)
            if target is None:
                return True  # Successfully filled

            total_empty = sum(
                1 for x in range(cols) for y in range(rows) if (x, y) not in occupied
            )

            if total_empty < 4:
                return True

            if has_small_hole(occupied):
                return False

            placements = can_fill_tetromino(occupied, target)
            random.shuffle(placements)

            for placement, color in placements:
                new_occupied = occupied | set(placement)
                result.append((placement, color))

                if solve(new_occupied, result, depth + 1):
                    return True

                _ = result.pop()

            return False

        result: list[tuple[Tetromino, str]] = []
        occupied: set[Coord] = set()

        max_attempts = 10
        for attempt in range(max_attempts):
            result.clear()
            occupied.clear()

            if solve(occupied, result):
                return set(result)

            # If failed, shuffle shapes and try again
            random.shuffle(normalized_shapes)

        # If we couldn't fill completely, return partial result
        return set(result)


def get_tetromino_outline(tetromino: Tetromino) -> list[Coord]:
    cells = set(tetromino)

    edges: list[tuple[Coord, Coord]] = []

    for x, y in cells:
        if (x, y - 1) not in cells:  # top edge
            edges.append(((x, y), (x + 1, y)))
        if (x + 1, y) not in cells:  # right edge
            edges.append(((x + 1, y), (x + 1, y + 1)))
        if (x, y + 1) not in cells:  # bottom edge
            edges.append(((x + 1, y + 1), (x, y + 1)))
        if (x - 1, y) not in cells:  # left edge
            edges.append(((x, y + 1), (x, y)))

    if not edges:
        return []

    outline = [edges[0][0], edges[0][1]]
    used = {0}

    while len(used) < len(edges):
        last_point = outline[-1]

        found = False
        for i, (start, end) in enumerate(edges):
            if i not in used and start == last_point:
                outline.append(end)
                used.add(i)
                found = True
                break

        if not found:
            break

    if outline[-1] == outline[0]:
        _ = outline.pop()

    return outline


if __name__ == "__main__":
    generate_wallpaper(Tetris)
