# Robot trying to find a way from start to the goal
In the 2D world with obstacles, the robot is using A* algorithm to find the path from the start to the goal destination.

## Usage
Call the `walk.py` script to do the work. See the program arguments that are required:
- `-s`, `--start`           - Coordinates of starting point (rows, columns).
- `-g`, `--goal`            - Coordinates of goal point (rows, columns).
- `-r`, `--world-heigh`     - Number of rows.
- `-c`, `--world-width`     - Number of columns.
- `-o`, `--obstacles-count` - Number of obstacles to be added to the world randomly.

```bash
python3 walk.py -s 0 0 -g 14 8 -r 15 -c 9 -o 50
```

### Example output
For the previous command the following outputs can be expected. Keep in mind that the placement of the obstacles is random, so it will change with every run.
```
[start|     |     |wall |     |     |     |wall |     ]
[     |=====|     |     |     |     |tree |     |     ]
[tree |     |=====|     |     |     |wall |     |     ]
[tree |     |hole |=====|tree |     |tree |     |     ]
[     |     |     |     |=====|     |     |tree |tree ]
[tree |hole |     |     |     |=====|tree |     |hole ]
[hole |     |tree |     |hole |wall |=====|     |     ]
[     |     |hole |     |     |     |     |=====|     ]
[tree |tree |     |hole |     |     |     |wall |=====]
[tree |     |wall |wall |     |     |hole |     |=====]
[     |hole |hole |     |     |wall |     |     |=====]
[     |wall |     |     |     |     |     |=====|wall ]
[     |     |     |     |hole |     |wall |     |=====]
[     |     |     |     |tree |tree |wall |     |=====]
[     |tree |     |     |     |     |     |     | goal]
```