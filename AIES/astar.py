from typing import List, Tuple, Dict

def h(a: Tuple[int, int], b: Tuple[int, int]) -> int:
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors(p: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
	x, y = p
	opts = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
	res = []
	for nx, ny in opts:
		if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
			if grid[nx][ny] == 0:
				res.append((nx, ny))
	return res


def astar(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
	open_list = [start]
	came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}

	g_score: Dict[Tuple[int, int], int] = {start: 0}
	f_score: Dict[Tuple[int, int], int] = {start: h(start, goal)}

	while open_list:
		current = open_list[0]
		for n in open_list:
			if f_score.get(n, 10**9) < f_score.get(current, 10**9):
				current = n

		if current == goal:
			path = [current]
			while current in came_from:
				current = came_from[current]
				path.append(current)
			path.reverse()
			return path

		open_list.remove(current)

		for n in neighbors(current, grid):
			temp_g = g_score[current] + 1
			if temp_g < g_score.get(n, 10**9):
				came_from[n] = current
				g_score[n] = temp_g
				f_score[n] = temp_g + h(n, goal)
				if n not in open_list:
					open_list.append(n)

	return []


if __name__ == "__main__":
	grid = [
		[0, 0, 0, 0, 0],
		[0, 1, 1, 1, 0],
		[0, 0, 0, 1, 0],
		[0, 1, 0, 0, 0],
		[0, 0, 0, 1, 0],
	]

	start = (0, 0)
	goal = (4, 4)

	path = astar(grid, start, goal)
	print("path:", path)
