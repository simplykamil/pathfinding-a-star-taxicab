from mazecreator.Creator import Creator


class AStarPathfinder:
    @staticmethod
    def find_path():
        grid = Creator.get_grid()

        [print(x) for x in grid]


if __name__ == '__main__':
    AStarPathfinder.find_path()
