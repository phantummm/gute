import argparse
from pathlib import Path
import os


class Readable(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        path = Path(values).resolve()

        if not os.access(path, os.R_OK):
            raise argparse.ArgumentTypeError(f"{path} is not readable.")

        setattr(namespace, self.dest, path)


class ReadableDirectory(Readable):
    def __call__(self, parser, namespace, values, option_string=None):
        super().__call__(parser, namespace, values)

        path = Path(values).resolve()

        if not path.is_dir():
            raise argparse.ArgumentTypeError(f"{path} is not a valid path.")


class WriteableDirectory(Readable):
    def __call__(self, parser, namespace, values, option_string=None):
        super().__call__(parser, namespace, values)

        path = Path(values).resolve()

        if not os.access(path, os.W_OK):
            raise argparse.ArgumentTypeError(f"{path} is not writeable.")


parser = argparse.ArgumentParser(
    prog="gute", description="A friendly tool for static content generation."
)

parser.add_argument(
    "source_path",
    action=ReadableDirectory,
    help="source folder from which to read markdown files",
)

parser.add_argument(
    "target_path",
    action=WriteableDirectory,
    help="target folder to which HTML should be rendered",
)

parser.add_argument(
    "--template",
    "-t",
    required=False,
    dest="template_path",
    action=Readable,
    default=None,
    help="template file to use",
)
