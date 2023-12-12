from typing import Set
from sortedcontainers import SortedSet
from robot_path_finder import *

def reconstruct_path(node: State) -> List[Tuple[int]]:
    path = []
    while node:
        path.append((node.row, node.column))
        node = node.parent
    path.reverse()
    return path

def a_star_search(world: RobotPathFinder, start: Set[int], goal: Set[int]) -> Optional[List[Tuple[int]]]:
    start = State(start[0], start[1])
    goal = State(goal[0], goal[1])

    if not world.check_if_in_map_range(start):
        raise ValueError(f'Start ({start}) is not in the map range: (0 - {world.map_rows - 1}, 0 - {world.map_columns - 1})!')
    if not world.check_if_in_map_range(goal):
        raise ValueError(f'Goal ({goal}) is not in the map range: (0 - {world.map_rows - 1}, 0 - {world.map_columns - 1})!')

    open_set = SortedSet()
    open_set.add(start)
    predecessores = set()

    while open_set:
        current = open_set.pop(0)

        if current.row == goal.row and current.column == goal.column:
            return reconstruct_path(current)

        predecessores.add((current.row, current.column))

        neighbor: State
        for neighbor in world.get_neighbors(current):
            if (neighbor.row, neighbor.column) in predecessores:
                continue

            neighbor.distance_from_start += 1
            neighbor.distance_to_goal = neighbor.get_heuristic_distance(goal)
            neighbor.parent = current
            open_set.add(neighbor)

    return None
