import argparse
from typing import Any
from typing import Generator
from typing import NamedTuple
from typing import Optional
from typing import Sequence
import os

import ruamel.yaml

yaml = ruamel.yaml.YAML(typ='safe')


def _exhaust(gen: Generator[str, None, None]) -> None:
    for _ in gen:
        pass


def _parse_unsafe(*args: Any, **kwargs: Any) -> None:
    _exhaust(yaml.parse(*args, **kwargs))


def _load_all(*args: Any, **kwargs: Any) -> None:
    _exhaust(yaml.load_all(*args, **kwargs))


class Key(NamedTuple):
    multi: bool
    unsafe: bool


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
        except ruamel.yaml.YAMLError as exc:
            print(exc)
            retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
