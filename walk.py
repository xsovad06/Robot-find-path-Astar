from a_start import *
import random
import argparse

obstacle_types = ['tree', 'hole', 'wall']

def parse_arguments():
    """Argument parser."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', nargs='+', type=int, required=True,help='Coordinates of starting point (rows, columns).')
    parser.add_argument('-g', '--goal', nargs='+', type=int, required=True, help='Coordinates of goal point (rows, columns).')
    parser.add_argument('-r', '--world-heigh', type=int, required=True, help='Number of rows.')
    parser.add_argument('-c', '--world-width', type=int, required=True, help='Number of columns.')
    parser.add_argument('-o', '--obstacles-count', type=int, required=True, help='Number of obstacles to be added to the world randomly.')
    return parser.parse_args()

def generate_random_obstacles_placement(
    num_points: int,
    max_row: int,
    max_column: int,
    obstacle_types: List[str],
    exclude_points: List[Tuple[int]]) -> List[Obstacle]:
    """Generate list of random obstacles with random positions on the map."""

    obstacles = []
    i = 0
    while i < num_points:
        row = random.randint(0, max_row - 1)
        column = random.randint(0, max_column - 1)

        if (row, column) in exclude_points:
            continue

        name_idx = random.randint(0, len(obstacle_types) - 1)
        obstacles.append(Obstacle(row, column, obstacle_types[name_idx]))
        i += 1

    return obstacles
    
if __name__ == "__main__":
    
    args = parse_arguments()
    start = (args.start[0], args.start[1])
    goal = (args.goal[0], args.goal[1])

    rows = args.world_heigh
    columns = args.world_width
    print(f'Starting parameters: start: {start}, goal: {goal}, world size: ({rows}, {columns})')
    obstacles = generate_random_obstacles_placement(args.obstacles_count, rows, columns, obstacle_types, [start, goal])
    state_space = RobotPathFinder(rows, columns, obstacles)
    # state_space.print_map()
    path = a_star_search(state_space, start, goal)
    state_space.load_and_print_path(path)

