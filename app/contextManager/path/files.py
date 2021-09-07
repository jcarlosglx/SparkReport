from __future__ import annotations

from os import remove
from os.path import exists
from typing import List
from uuid import uuid4


class PathFiles:
    def __init__(self, n_paths: int = 1, temp_dir: str = "/tmp/", type_file: str = "txt"):
        self.paths: List[str] = []
        self.dir: str = temp_dir
        self.names: List[str] = []
        self.type_file: str = type_file
        for n in range(n_paths):
            self.names.append(f"{uuid4()}.{type_file}")
            self.paths.append(f"{temp_dir}{self.names[n]}")

    def __enter__(self) -> PathFiles:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for path in self.paths:
            if exists(path):
                remove(path)
