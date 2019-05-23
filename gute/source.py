import glob
from pathlib import Path
from typing import List

from markdown2 import markdown_path, UnicodeWithAttrs


class Source:
    def __init__(self, source_path: Path):
        self.path = source_path

    def node_paths(self) -> List[str]:
        return glob.glob(f"{self.path}/*.md")

    def nodes(self) -> List[UnicodeWithAttrs]:
        return [markdown_path(x) for x in self.node_paths()]

