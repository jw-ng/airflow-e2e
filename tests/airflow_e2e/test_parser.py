from argparse import Namespace

import pytest as pytest

from airflow_e2e.parser import parse


def test_should_raise_error_when_dags_argument_is_not_specified():
    with pytest.raises(SystemExit):
        parse(["--dags", "dags/"])


def test_should_raise_error_when_tests_argument_is_not_specified():
    with pytest.raises(SystemExit):
        parse(["--tests", "tests/"])


def test_should_return_correct_namespace_containing_dags_and_tests_folder_when_specified():
    args = parse(["--dags", "dags/", "--tests", "tests/"])

    assert args == Namespace(dags="dags/", tests="tests/")
