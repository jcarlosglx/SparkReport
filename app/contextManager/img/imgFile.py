from os.path import exists
from os import remove
from uuid import uuid4


class IMGFile:
    def __init__(self, temp_dir: str = "/tmp/"):
        self.img_name = f"{uuid4()}.png"
        self.temporal_dir = temp_dir
        self.path_img = f"{temp_dir}{self.img_name}"

    def __enter__(self) -> str:
        return self.path_img

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exists(self.path_img):
            remove(self.path_img)
