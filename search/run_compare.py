from search.core import bfs, dfs, depth_limited_dfs, iddfs
from problems.eight_queens import EightQueens


def show(name, result):
    print("\n" + name)
    print("Nodes expanded:", result.nodes_expanded)
    print("Visited count:", result.visited_count)
    print("Max frontier:", result.max_frontier)
    print("Time (ms):", result.time_ms)

    if result.found:
        print("Solution depth:", len(result.path) - 1)


def main():
    problem = EightQueens()

    print("Running search algorithms on the Eight Queens problem")

    show("BFS", bfs(problem))
    show("DFS", dfs(problem))
    show("Depth Limited DFS", depth_limited_dfs(problem, 10))
    show("Iterative Deepening DFS", iddfs(problem, 10))


if __name__ == "__main__":
    main()