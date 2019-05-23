from argparse import ArgumentTypeError

from .parser import parser
from .source import Source
from .template import Template


def main():
    try:
        args = parser.parse_args()
    except ArgumentTypeError as err:
        print(err)
        print("type gute -h for help with syntax")

    source = Source(args.source_path)
    templates = Template.from_nodes(source.nodes(), args.template_path)

    for template in templates:
        new_path = args.target_path.joinpath(template.target_filename())
        with open(new_path, "w+") as f:
            f.write(template.hydrate())


if __name__ == "__main__":
    main()
