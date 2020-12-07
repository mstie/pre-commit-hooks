import argparse
from typing import Optional
from typing import Sequence
import os


def main(argv: Optional[Sequence[str]] = None) -> int:

    scenes_dir = 'ErwinsRetreat/Assets/_Scenes'
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Scene files to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            filename, file_extension = os.path.splitext(filename)

            if file_extension == 'unity':
                print(filename)
        except Exception as exc:
            print(exc)
            retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
