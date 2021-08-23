from os.path import exists
from os import remove
from uuid import uuid4


class PDFFile:
    def __init__(self, temp_dir: str = "/tmp/"):
        self.img_pdf = f"{uuid4()}.pdf"
        self.temporal_dir = temp_dir
        self.path_pdf = f"{temp_dir}{self.img_pdf}"

    def __enter__(self) -> str:
        return self.path_pdf

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exists(self.path_pdf):
            remove(self.path_pdf)
