def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:

    start = None
    end = None

    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = [r, c]
            elif maze[r][c] == 'E':
                end = [r, c]

    if start == None or end == None:
        return {"distance": -1, "path": []}

    queue = [[start, [start], 0]]
    visited = [start]

    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    index = 0

    while index < len(queue):
        current = queue[index]
        index += 1
        position = current[0]
        path = current[1]
        distance = current[2]
        r = position[0]
        c = position[1]

        if position == end:
            return {
                "distance": distance,
                "path": path
            }

        for d in directions:

            nr = r + d[0]
            nc = c + d[1]

            if nr < 0 or nr >= len(maze):
                continue

            if nc < 0 or nc >= len(maze[0]):
                continue

            if maze[nr][nc] == '#':
                continue

            new_path = path + [[nr, nc]]

            while (
                maze[nr][nc] == '>' or
                maze[nr][nc] == '<' or
                maze[nr][nc] == '^' or
                maze[nr][nc] == 'v'
            ):

                if maze[nr][nc] == '>':
                    nc += 1

                elif maze[nr][nc] == '<':
                    nc -= 1

                elif maze[nr][nc] == '^':
                    nr -= 1

                elif maze[nr][nc] == 'v':
                    nr += 1

                if nr < 0 or nr >= len(maze):
                    new_path = []
                    break

                if nc < 0 or nc >= len(maze[0]):
                    new_path = []
                    break

                if maze[nr][nc] == '#':
                    new_path = []
                    break

                new_path.append([nr, nc])

            if len(new_path) == 0:
                continue

            new_position = [nr, nc]
            if new_position not in visited:
                visited.append(new_position)
                queue.append([
                    new_position,
                    new_path,
                    distance + 1
                ])

    return {
        "distance": -1,
        "path": []
    }

if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}

    maze = [
        ['S', '.', '>', '#', 'E'],
        ['#', '#', '#', '#', '#']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}


    maze = [
        ['S', '.', 'v', '.', 'E'],
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}
