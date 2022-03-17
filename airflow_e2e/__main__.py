import sys

from airflow_e2e import parser


def main():
    args = parser.parse(sys.argv[1:])


if __name__ == "__main__":
    main()
