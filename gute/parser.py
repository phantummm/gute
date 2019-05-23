import argparse
from pathlib import Path
import os


class readable_path(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        path = Path(values).resolve()

        if not path.is_dir():
            raise argparse.ArgumentTypeError(f"{path} is not a valid path.")
        if os.access(path, os.R_OK):
            setattr(namespace, self.dest, path)
        else:
            raise argparse.ArgumentTypeError(f"{values} is not a readable directory.")


parser = argparse.ArgumentParser(
    prog="gute", description="A friendly tool for static content generation."
)

parser.add_argument(
    "source",
    action=readable_path,
    help="source folder from which to read markdown files",
)

parser.add_argument(
    "target",
    action=readable_path,
    help="target folder to which HTML should be rendered",
)
