import datetime
from pathlib import Path
from PIL.Image import Image


class Recorder:
    def __init__(self, basedir: Path) -> None:
        now = datetime.datetime.now()
        now_str = now.strftime("%Y%m%d%H%M%S")
        runs = basedir.joinpath("runs", now_str)
        runs.mkdir(parents=True, exist_ok=True)
        self.base_path = runs

    def tell(self, outcome: str):
        self.base_path.joinpath(outcome.upper()).touch()

    def save(self, image: Image, name: str) -> None:
        tgt = self.base_path.joinpath(f"{name}.png")
        image.save(tgt)
