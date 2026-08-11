from pathlib import Path
import time


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def artifact_path(folder: str, filename: str) -> str:
    p = Path(folder)
    ensure_dir(p)
    return str(p / filename)
