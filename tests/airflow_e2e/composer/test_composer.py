import tempfile
from pathlib import Path
from unittest.mock import MagicMock, call

import pytest as pytest

from airflow_e2e.composer import composer


def test_should_create_docker_base_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=False,
            with_custom_test_packages=False,
            with_mongo=False,
        )

        expected_docker_folder_path = Path(temp_dir) / "docker"

        assert expected_docker_folder_path.exists()


@pytest.mark.parametrize("with_custom_airflow_packages_flag", [True, False])
def test_setup_should_setup_airflow_core_services(
    mocker, with_custom_airflow_packages_flag: bool
):
    mock_composer_instance = MagicMock()
    spy_build = mocker.patch(
        "airflow_e2e.composer.composer.build_airflow_core_services_composer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=with_custom_airflow_packages_flag,
            with_custom_test_packages=False,
            with_mongo=False,
        )

        assert spy_build.call_count == 1
        assert spy_build.call_args == call(
            dags="some/dags/folder",
            with_custom_airflow_packages=with_custom_airflow_packages_flag,
        )

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


@pytest.mark.parametrize("with_custom_test_packages_flag", [True, False])
def test_setup_should_setup_e2e_test_runner_service(
    mocker, with_custom_test_packages_flag: bool
):
    mock_composer_instance = MagicMock()
    spy_build = mocker.patch(
        "airflow_e2e.composer.composer.build_e2e_test_runner_service_composer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=False,
            with_custom_test_packages=with_custom_test_packages_flag,
            with_mongo=False,
        )

        assert spy_build.call_count == 1
        assert spy_build.call_args == call(
            dags="some/dags/folder",
            tests="some/tests/folder",
            with_custom_test_packages=with_custom_test_packages_flag,
        )

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_should_setup_airflow_seeder_service_composer(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.AirflowSeederServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=False,
            with_custom_test_packages=False,
            with_mongo=False,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call()

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


@pytest.mark.parametrize("with_mongo_flag", [True, False])
def test_setup_should_setup_extra_services_composer_with_mongo_when_with_mongo_is_true(
    mocker, with_mongo_flag
):
    spy_build = mocker.patch(
        "airflow_e2e.composer.composer.build_extra_services_composer",
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=False,
            with_custom_test_packages=False,
            with_mongo=with_mongo_flag,
        )

        assert spy_build.call_count == 1
        assert spy_build.call_args == call(with_mongo=with_mongo_flag)


def test_setup_should_setup_manual_e2e_test_runner_service_composer(mocker):
    mock_composer_instance = MagicMock()
    spy_composer = mocker.patch(
        "airflow_e2e.composer.composer.ManualE2eTestRunnerServiceComposer",
        return_value=mock_composer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=False,
            with_custom_test_packages=False,
            with_mongo=False,
        )

        assert spy_composer.call_count == 1
        assert spy_composer.call_args == call()

        assert mock_composer_instance.setup.call_count == 1
        assert mock_composer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )


def test_setup_should_setup_envrc_file_writer(mocker):
    mocker_writer_instance = MagicMock()
    spy_writer = mocker.patch(
        "airflow_e2e.composer.composer.EnvrcFileWriter",
        return_value=mocker_writer_instance,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        composer.setup(
            dags="some/dags/folder",
            tests="some/tests/folder",
            working_dir=temp_dir,
            with_custom_airflow_packages=False,
            with_custom_test_packages=False,
            with_mongo=False,
        )

        assert spy_writer.call_count == 1
        assert spy_writer.call_args == call()

        assert mocker_writer_instance.setup.call_count == 1
        assert mocker_writer_instance.setup.call_args == call(
            working_dir=Path(temp_dir) / "docker"
        )
