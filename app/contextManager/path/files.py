from __future__ import annotations
from os.path import exists
from os import remove
from uuid import uuid4
from typing import List


class PathFiles:
    def __init__(self, n_paths: int = 1, temp_dir: str = "/tmp/"):
        self.paths: List[str] = []
        self.dir: str = temp_dir
        self.names: List[str] = []
        for n in range(n_paths):
            self.names.append(f"{uuid4()}.png")
            self.paths.append(f"{temp_dir}{self.names[n]}")

    def __enter__(self) -> PathFiles:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for path in self.paths:
            if exists(path):
                remove(path)
