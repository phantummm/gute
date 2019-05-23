import unittest
from pathlib import Path
from gute.source import Source


class SourceTest(unittest.TestCase):
    def test_source_node_paths(self):
        source_path = Path("./tests/data/").resolve()
        source = Source(source_path)
        self.assertListEqual(
            [Path(f"{source_path}/post1.md"), Path(f"{source_path}/post2.md")],
            source.node_paths(),
        )

    def test_source_nodes(self):
        source_path = Path("./tests/data/").resolve()
        source = Source(source_path)
        self.assertEqual(
            "<h1>Hello, world</h1>\n\n<p>This is really great content. Let's make it static.</p>\n",
            source.nodes()[0].content(),
        )
