from pathlib import Path
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_project_path():
    return os.path.dirname(os.path.abspath(__file__))


def get_file_path(file_path=None):
    return os.path.join(get_project_path(), file_path)


def get_project_root() -> Path:
    return Path(__file__).parent.parent


print(get_project_root())
print(get_project_path())
