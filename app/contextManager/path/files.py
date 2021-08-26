from os.path import exists
from os import remove
from uuid import uuid4
from typing import List


class PathFiles:
    def __init__(self, n_paths: int = 1, temp_dir: str = "/tmp/"):
        self.paths: List[str] = []
        for n in range(n_paths):
            self.paths.append(f"{temp_dir}{uuid4()}.png")
        self.temporal_dir = temp_dir

    def __enter__(self) -> List[str]:
        return self.paths

    def __exit__(self, exc_type, exc_val, exc_tb):
        for path in self.paths:
            if exists(path):
                remove(path)
