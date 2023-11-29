from pathlib import Path
from shutil import rmtree
import sys
import datetime

DAYS = 3


class Reaper:
    def __init__(self, path: Path) -> None:
        self.path = path

    def check(self):
        if not self.path.is_dir():
            raise ValueError(f"{self.path.as_posix()} is not a directory")
        for item in self.path.iterdir():
            if item.is_dir():
                mtime = datetime.datetime.fromtimestamp(item.stat().st_mtime)
                age = datetime.datetime.now() - mtime
                if age.seconds > DAYS * 3600 * 24:
                    rmtree(item.as_posix())


if __name__ == "__main__":
    r = Reaper(Path(sys.argv[1]))
    r.check()
