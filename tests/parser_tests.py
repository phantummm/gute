import unittest
from gute.parser import parser
from argparse import ArgumentTypeError
from pathlib import Path


class ParserTest(unittest.TestCase):
    def test_valid_path_arguments(self):
        args = parser.parse_args(["./tests/data/", "./tests/target/"])
        self.assertEqual(Path("./tests/data/").resolve(), args.source_path)
        self.assertEqual(Path("./tests/target/").resolve(), args.target_path)

    def test_invalid_source_argument(self):
        with self.assertRaises(ArgumentTypeError):
            parser.parse_args(["./blahblah", "./tests/target/"])

    def test_invalid_target_argument(self):
        with self.assertRaises(ArgumentTypeError):
            parser.parse_args(["./tests/data/", "./blahblah/"])
