from argparse import ArgumentTypeError

from .parser import parser


def main():
    try:
        args = parser.parse_args()
    except ArgumentTypeError as err:
        print(err)
        print("type gute -h for help with syntax")


if __name__ == "__main__":
    main()
