from dataclasses import dataclass
from typing import Iterable, Tuple
from search.core import Problem

@dataclass(frozen=True)
class Q:
    cols: Tuple[int, ...]  # cols[row] = col chosen

class EightQueens(Problem[Q]):
    def __init__(self, n: int = 8):
        self.n = n

    def initial(self) -> Q:
        return Q(tuple())

    def is_goal(self, s: Q) -> bool:
        return len(s.cols) == self.n

    def key(self, s: Q) -> str:
        return ",".join(map(str, s.cols))

    def _safe(self, cols: Tuple[int, ...], new_col: int) -> bool:
        r = len(cols)
        for r2, c2 in enumerate(cols):
            if c2 == new_col:
                return False
            if abs(c2 - new_col) == abs(r2 - r):
                return False
        return True

    def neighbors(self, s: Q) -> Iterable[Q]:
        for c in range(self.n):
            if self._safe(s.cols, c):
                yield Q(s.cols + (c,))