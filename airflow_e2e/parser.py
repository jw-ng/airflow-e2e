import argparse
import typing


def parse(args: typing.List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dags", required=True)
    parser.add_argument("--tests", required=True)

    return parser.parse_args(args)
