import argparse
import typing


def parse(args: typing.List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dags",
        required=True,
        help="DAGs folder path, relative from the root of the repository",
    )
    parser.add_argument(
        "--tests",
        required=True,
        help="E2E test suite folder path, relative from the root of the repository",
    )
    parser.add_argument(
        "--requirements",
        required=False,
        action="store_true",
        help="Indicate if a requirements.txt file is to be mounted for the Airflow services",
    )
    parser.add_argument(
        "--test-requirements",
        required=False,
        action="store_true",
        help="Indicate if a requirements-dev.txt file is to be mounted for the test runner service",
    )

    return parser.parse_args(args)
