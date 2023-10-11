from itertools import product
from typing import List

MAX_PREFIX_LEN = 10
MAX_SUFFIX_LEN = 10
SEP = '.'


class WordFilter:
    def __init__(self, words: List[str]):
        self.map = {}

        for idx, w in enumerate(words):
            for i, j in product(
                    range(1, min(MAX_PREFIX_LEN, len(w)) + 1),
                    range(1, min(MAX_SUFFIX_LEN, len(w)) + 1)
            ):
                self.map[w[:i] + SEP + w[-j:]] = idx

    def f(self, prefix: str, suffix: str) -> int:
        return self.map.get(prefix + SEP + suffix, -1)
	
