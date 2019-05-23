import unittest
from pathlib import Path

from gute.source import SourceNode
from gute.template import Template


class TemplateTest(unittest.TestCase):
    def test_bulk_constructor(self):
        nodes = ["<div>Hello</div>", "<div>World</div>"]
        templates = Template.from_nodes(nodes, None)
        self.assertEqual("<div>Hello</div>", templates[0].source_node)

    def test_target_filename(self):
        source_node = SourceNode(Path("./tests/data/post1.md"))
        template = Template(source_node, None)
        self.assertEqual("post1.html", template.target_filename())

    def test_hydrate_with_default_template(self):
        source_node = SourceNode(Path("./tests/data/post1.md"))
        template = Template(source_node, None)
        self.assertEqual(
            "<div><h1>Hello, world</h1>\n\n<p>This is really great content. Let's make it static.</p>\n</div>",
            template.hydrate(),
        )

