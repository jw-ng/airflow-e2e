import os
import sys

from airflow_e2e import parser
from airflow_e2e.constants import BASIC_USAGE_INSTRUCTIONS, CONVENIENT_MAKE_COMMANDS
from airflow_e2e.composer import composer
from airflow_e2e.printer import print_to_screen


def main():
    args = parser.parse(sys.argv[1:])

    working_dir = os.getcwd()
    composer.setup(
        dags=args.dags,
        tests=args.tests,
        working_dir=working_dir,
        with_custom_airflow_packages=args.with_custom_airflow_packages,
        with_custom_test_packages=args.with_custom_test_packages,
        with_mongo=args.with_mongo,
    )

    print_to_screen(f"Airflow E2E test scripts generated in '{working_dir}/docker/'\n")
    print_to_screen(CONVENIENT_MAKE_COMMANDS)
    print_to_screen(BASIC_USAGE_INSTRUCTIONS)


if __name__ == "__main__":
    main()
