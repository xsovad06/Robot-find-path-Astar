from sys import maxsize
from functools import lru_cache
from typing import List, Tuple, NamedTuple, Optional

class State:
    @lru_cache(maxsize=maxsize)
    def __new__(cls, row: int, column: int, parent=None) -> 'State':
        instance = super().__new__(cls)
        instance.row = row
        instance.column = column
        instance.parent = parent
        instance.distance_from_start = 0
        instance.distance_to_goal = 0
        return instance

    def __eq__(self, other) -> bool:
        return self.f_score == other.f_score

    def __lt__(self, other) -> bool:
        return self.f_score < other.f_score
    
    def __hash__(self) -> int:
        return hash((self.row, self.column))
    
    def __repr__(self) -> str:
        return f'({self.row}, {self.column})'

    @property
    def f_score(self):
        return self.distance_from_start + self.distance_to_goal

    @lru_cache(maxsize=maxsize)
    def get_heuristic_distance(self, goal):
        return manhattan_distance(self, goal)

def manhattan_distance(state1: State, state2: State):
    """Naive distance approach, as the crow flies."""

    return abs(state1.row - state2.row) + abs(state1.column - state2.column)

class Obstacle(NamedTuple):
    row: int
    column: int
    name: str

    def __str__(self) -> str:
        return self.name

class RobotPathFinder:
    def __init__(self, row_count: int, column_count: int, obstacles: List[Obstacle]) -> None:
        self.map_rows = row_count
        self.map_columns = column_count
        self.map = []
        for _ in range(row_count):
            row = [None] * column_count
            self.map.append(row)

        obstacle: Obstacle
        for obstacle in obstacles:
            self.map[obstacle.row][obstacle.column] = obstacle

    def __str__(self) -> str:
        result = ""
        for r in range(self.map_rows):
            item = [f"{str(value):<{5}}" if value is not None else "     " for value in self.map[r]]
            result += "[" + "|".join(item) + "]\n"
        return result
    
    def print_map(self) -> None:
        print(str(self))

    def check_if_in_map_range(self, position: State) -> bool:
        return 0 <= position.row < self.map_rows and 0 <= position.column < self.map_columns

    def get_neighbors(self, current_state: State) -> List[State]:
        neighbors = []
        row, column = current_state.row, current_state.column

        # Cartesian neighbors
        if row > 0:                                                     # north neighbor
            next_row = row - 1
            if not isinstance(self.map[next_row][column], Obstacle):
                neighbors.append(State(next_row, column))
        if column < self.map_columns - 1:                                  # east neighbor
            next_column = column + 1
            if not isinstance(self.map[row][next_column], Obstacle):
                neighbors.append(State(row, next_column))
        if row < self.map_rows - 1:                                     # south neighbor
            next_row = row + 1
            if not isinstance(self.map[next_row][column], Obstacle):
                neighbors.append(State(next_row, column))
        if column > 0:                                                  # west neighbor
            next_column = column - 1
            if not isinstance(self.map[row][next_column], Obstacle):
                neighbors.append(State(row, next_column))

        # Diagonal neighbors
        if row > 0 and column < self.map_columns - 1:                   # northeast neighbor
            next_row = row - 1
            next_column = column + 1
            if not isinstance(self.map[next_row][next_column], Obstacle):
                neighbors.append(State(next_row, next_column))
        if row < self.map_rows - 1 and column < self.map_columns - 1:   # southeast neighbor
            next_row = row + 1
            next_column = column + 1
            if not isinstance(self.map[next_row][next_column], Obstacle):
                neighbors.append(State(next_row, next_column))
        if row < self.map_rows - 1 and column > 0:                   # soutwest neighbor
            next_row = row + 1
            next_column = column - 1
            if not isinstance(self.map[next_row][next_column], Obstacle):
                neighbors.append(State(next_row, next_column))
        if row > 0 and column > 0:                                      # norhtwest neighbor
            next_row = row - 1
            next_column = column - 1
            if not isinstance(self.map[next_row][next_column], Obstacle):
                neighbors.append(State(next_row, next_column))

        return neighbors
    
    def load_and_print_path(self, path: List[Tuple[int]]) -> None:
        if not path:
            print(f'Could not find the path to the goal.')
            return
    
        for idx, position in enumerate(path):
            if idx == 0:
                self.map[position[0]][position[1]] = "start"
            elif idx == len(path) - 1:
                self.map[position[0]][position[1]] = "goal "
            else:
                self.map[position[0]][position[1]] = "====="

        self.print_map()
