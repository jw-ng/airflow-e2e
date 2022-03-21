import os
import sys

from airflow_e2e import parser


def main():
    args = parser.parse(sys.argv[1:])

    working_dir = os.getcwd()
    generate(dags=args.dags, tests=args.tests, working_dir=working_dir)


if __name__ == "__main__":
    main()
