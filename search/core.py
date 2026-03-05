from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from typing import Deque, Dict, Generic, Iterable, List, Optional, Set, Tuple, TypeVar
import time

S = TypeVar("S")

@dataclass
class Result(Generic[S]):
    found: bool
    path: List[S]
    nodes_expanded: int
    max_frontier: int
    visited_count: int
    time_ms: float

class Problem(Generic[S]):
    def initial(self) -> S:
        raise NotImplementedError

    def is_goal(self, s: S) -> bool:
        raise NotImplementedError

    def neighbors(self, s: S) -> Iterable[S]:
        raise NotImplementedError

    def key(self, s: S) -> str:
        # must uniquely identify the state
        return str(s)

def _reconstruct(parent: Dict[str, Optional[str]], states: Dict[str, S], goal_k: str) -> List[S]:
    out: List[S] = []
    cur: Optional[str] = goal_k
    while cur is not None:
        out.append(states[cur])
        cur = parent[cur]
    out.reverse()
    return out

def bfs(problem: Problem[S]) -> Result[S]:
    start_t = time.perf_counter()
    s0 = problem.initial()
    k0 = problem.key(s0)

    q: Deque[str] = deque([k0])
    visited: Set[str] = {k0}
    parent: Dict[str, Optional[str]] = {k0: None}
    states: Dict[str, S] = {k0: s0}

    nodes_expanded = 0
    max_frontier = 1

    while q:
        max_frontier = max(max_frontier, len(q))
        ck = q.popleft()
        cs = states[ck]

        if problem.is_goal(cs):
            path = _reconstruct(parent, states, ck)
            return Result(True, path, nodes_expanded, max_frontier, len(visited),
                          (time.perf_counter() - start_t) * 1000)

        nodes_expanded += 1
        for ns in problem.neighbors(cs):
            nk = problem.key(ns)
            if nk not in visited:
                visited.add(nk)
                parent[nk] = ck
                states[nk] = ns
                q.append(nk)

    return Result(False, [], nodes_expanded, max_frontier, len(visited),
                  (time.perf_counter() - start_t) * 1000)

def dfs(problem: Problem[S]) -> Result[S]:
    start_t = time.perf_counter()
    s0 = problem.initial()
    k0 = problem.key(s0)

    stack: List[str] = [k0]
    visited: Set[str] = {k0}
    parent: Dict[str, Optional[str]] = {k0: None}
    states: Dict[str, S] = {k0: s0}

    nodes_expanded = 0
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        ck = stack.pop()
        cs = states[ck]

        if problem.is_goal(cs):
            path = _reconstruct(parent, states, ck)
            return Result(True, path, nodes_expanded, max_frontier, len(visited),
                          (time.perf_counter() - start_t) * 1000)

        nodes_expanded += 1
        for ns in problem.neighbors(cs):
            nk = problem.key(ns)
            if nk not in visited:
                visited.add(nk)
                parent[nk] = ck
                states[nk] = ns
                stack.append(nk)

    return Result(False, [], nodes_expanded, max_frontier, len(visited),
                  (time.perf_counter() - start_t) * 1000)

def depth_limited_dfs(problem: Problem[S], limit: int) -> Result[S]:
    start_t = time.perf_counter()
    s0 = problem.initial()
    k0 = problem.key(s0)

    stack: List[Tuple[str, int]] = [(k0, 0)]
    visited: Set[str] = {k0}
    parent: Dict[str, Optional[str]] = {k0: None}
    states: Dict[str, S] = {k0: s0}

    nodes_expanded = 0
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        ck, depth = stack.pop()
        cs = states[ck]

        if problem.is_goal(cs):
            path = _reconstruct(parent, states, ck)
            return Result(True, path, nodes_expanded, max_frontier, len(visited),
                          (time.perf_counter() - start_t) * 1000)

        if depth >= limit:
            continue

        nodes_expanded += 1
        for ns in problem.neighbors(cs):
            nk = problem.key(ns)
            if nk not in visited:
                visited.add(nk)
                parent[nk] = ck
                states[nk] = ns
                stack.append((nk, depth + 1))

    return Result(False, [], nodes_expanded, max_frontier, len(visited),
                  (time.perf_counter() - start_t) * 1000)

def iddfs(problem: Problem[S], max_depth: int) -> Result[S]:
    # Iterative Deepening DFS: run DLS for depth 0..max_depth until found
    last = None
    for d in range(max_depth + 1):
        last = depth_limited_dfs(problem, d)
        if last.found:
            return last
    return last if last else Result(False, [], 0, 0, 0, 0.0)