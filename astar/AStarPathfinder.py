from queue import PriorityQueue

import pygame

import mazecreator.picasso as picasso
import mazecreator.settings as settings
from mazecreator.Creator import Creator
from mazecreator.SquareState import SquareState


class AStarPathfinder:
    @staticmethod
    def find_path():
        def _get_valid_neighbours(r: int, c: int):
            """
            Find valid neighbours for a square:
            valid means it's not a wall, has not been visited
            :param r: row
            :param c: column
            :return: valid neighbours
            :rtype: list()
            """
            rs = r
            cs = c

            up_neighbour = (r, c + 1)
            down_neighbour = (r, c - 1)
            left_neighbour = (r - 1, c)
            right_neighbour = (r + 1, c)

            neighbours = [up_neighbour, down_neighbour, left_neighbour, right_neighbour]
            v_neighbours = list()

            for neighbour in neighbours:
                r, c = neighbour
                if r in range(settings.ROWS) and c in range(settings.ROWS):
                    if grid[r][c].state not in [SquareState.VISITED, SquareState.WALL, SquareState.START]:
                        v_neighbours.append(neighbour)

            return v_neighbours

        def _heuristic(p1: tuple, p2: tuple):
            """
            Get approximate distance to p2
            :param p1: position 1
            :param p2: end position
            :return: approximate distance
            :rtype: int
            """
            x1, y1 = p1
            x2, y2 = p2

            return abs(x1 - x2) + abs(y1 - y2)

        WINDOW = pygame.display.set_mode((800, 800))
        grid = Creator.get_grid()
        pq = PriorityQueue()
        pq.put(1)  # placeholder for now

        for row in grid:
            for square in row:
                if square.state == SquareState.START:
                    start_pos = square.row, square.col
                elif square.state == SquareState.END:
                    end_pos = square.row, square.col

        print()
        print(f'Starting position: {start_pos}')
        print(f'Ending position: {end_pos}')
        print()

        while not pq.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pq = PriorityQueue()

            picasso.draw(WINDOW, grid)


if __name__ == '__main__':
    AStarPathfinder.find_path()
