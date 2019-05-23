from pathlib import Path
import re
from typing import List, Optional, Union, TextIO

import jinja2

from .source import SourceNode

DEFAULT_TEMPLATE = "<div>{{ content }}</div>"


class Template:
    def __init__(self, source_node: SourceNode, template_path: Optional[Path]):
        self.source_node = source_node
        self.template_path = template_path

    def target_filename(self) -> str:
        return re.sub(r".md$", ".html", self.source_node.name)

    def get_template(self) -> Union[TextIO, str]:
        if self.template_path is not None:
            with open(self.template_path, "r") as template:
                return template.read()
        else:
            return DEFAULT_TEMPLATE

    def hydrate(self):
        template = jinja2.Template(self.get_template())
        return template.render(content=self.source_node.content())

    @classmethod
    def from_nodes(
        class_object, source_nodes: List[SourceNode], template_path: Optional[Path]
    ) -> List["Template"]:
        return [class_object(node, template_path) for node in source_nodes]
