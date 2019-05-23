import glob
from pathlib import Path
from typing import List

from markdown2 import markdown_path, UnicodeWithAttrs


class SourceNode:
    def __init__(self, path: Path):
        self.path = Path(path).resolve()
        self.name = path.name

    def content(self):
        return markdown_path(self.path)


class Source:
    def __init__(self, source_path: Path):
        self.path = source_path

    def node_paths(self) -> List[Path]:
        return [Path(x) for x in glob.glob(f"{self.path}/*.md")]

    def nodes(self) -> List[SourceNode]:
        return [SourceNode(x) for x in self.node_paths()]
